import sys
from pathlib import Path
import logging
import numpy as np

sys.path.insert(0, str(Path(__file__).parent.parent))

from src.config import settings
from src.retrieval.hybrid_search import HybridRetriever
from src.retrieval.reranker import Reranker
from src.generation.answer_generator import AnswerGenerator

logging.basicConfig(level=logging.WARNING)

# Test cases
TESTS = [
    {"q": "I'm calculating our takeoff weight for a dry runway. We're at 2,000 feet pressure altitude, and the OAT is 50°C. What's the climb limit weight?", "pages": [83]},
    {"q": "We're doing a Flaps 15 takeoff. Remind me, what is the first flap selection we make during retraction, and at what speed?", "pages": [41]},
    {"q": "We're planning a Flaps 40 landing on a wet runway at a 1,000-foot pressure altitude airport. If the wind-corrected field length is 1,600 meters, what is our field limit weight?", "pages": [99]},
    {"q": "Reviewing the standard takeoff profile: After we're airborne and get a positive rate of climb, what is the first action we take?", "pages": [39, 51]},
    {"q": "Looking at the panel scan responsibilities for when the aircraft is stationary, who is responsible for the forward aisle stand?", "pages": [6]},
    {"q": "For a standard visual pattern, what three actions must be completed prior to turning base?", "pages": [56]},
    {"q": "If the PF is making entries into the CDU during flight, what must the PF do prior to execution?", "pages": [5]},
    {"q": "I see an amber 'STAIRS OPER' light illuminated on the forward attendant panel; what does that light indicate?", "pages": [126]},
    {"q": "We've just completed the engine start. What is the correct configuration for the ISOLATION VALVE switch during the After Start Procedure?", "pages": [35]},
    {"q": "During the Descent and Approach procedure, what action is taken with the AUTO BRAKE select switch, and what is the Pilot Flying's final action regarding the autobrake system during the Landing Roll procedure?", "pages": [43, 47]},
]


def main():
    """Run evaluation."""
    
    print("Initializing...")
    retriever = HybridRetriever(settings.chroma_persist_dir, settings.embedding_model)
    reranker = Reranker(settings.reranker_model)
    generator = AnswerGenerator(settings.gemini_api_key)
    
    print("\n" + "="*80)
    print("EVALUATION RESULTS")
    print("="*80)
    
    hit_1 = hit_3 = hit_10 = 0
    mrr_scores = []
    ndcg_scores = []
    total_relevant = total_returned = correct = 0
    
    for i, test in enumerate(TESTS, 1):
        question = test["q"]
        expected = set(test["pages"])
        
        # Retrieve
        results = retriever.search(question, top_k=100)
        reranked = reranker.rerank(question, results, top_k=20)
        
        # Get top 10
        top_10 = [r['page_number'] for r in reranked[:10]]
        
        # Hit Rate
        if any(p in expected for p in top_10[:1]): hit_1 += 1
        if any(p in expected for p in top_10[:3]): hit_3 += 1
        if any(p in expected for p in top_10[:10]): hit_10 += 1
        
        # MRR: Reciprocal rank of first relevant page
        mrr = 0.0
        for rank, page in enumerate(top_10, 1):
            if page in expected:
                mrr = 1.0 / rank
                break
        mrr_scores.append(mrr)
        
        # nDCG@10: Discounted cumulative gain
        dcg = sum(
            (1.0 if page in expected else 0.0) / np.log2(rank + 1)
            for rank, page in enumerate(top_10, 1)
        )
        idcg = sum(1.0 / np.log2(rank + 1) for rank in range(1, min(len(expected), 10) + 1))
        ndcg = dcg / idcg if idcg > 0 else 0.0
        ndcg_scores.append(ndcg)
        
        # Generate
        answer, returned = generator.generate(question, reranked, max_chunks=5)
        returned_set = set(returned)
        
        # Page accuracy
        overlap = expected & returned_set
        total_relevant += len(expected)
        total_returned += len(returned)
        correct += len(overlap)
        
        # Show result
        match = "✓" if overlap else "✗"
        print(f"\n{match} Query {i}")
        print(f"  Expected: {sorted(expected)}")
        print(f"  Returned: {sorted(returned)}")
        if not overlap:
            print(f"  Top 3: {top_10[:3]}")
    
    # Metrics
    n = len(TESTS)
    recall = correct / total_relevant if total_relevant > 0 else 0
    precision = correct / total_returned if total_returned > 0 else 0
    
    print("\n" + "="*80)
    print("METRICS")
    print("="*80)
    print(f"Hit Rate@1:       {hit_1}/{n} = {hit_1/n:.1%}")
    print(f"Hit Rate@3:       {hit_3}/{n} = {hit_3/n:.1%}")
    print(f"Hit Rate@10:      {hit_10}/{n} = {hit_10/n:.1%}")
    print(f"MRR@10:           {np.mean(mrr_scores):.3f}")
    print(f"nDCG@10:          {np.mean(ndcg_scores):.3f}")
    print(f"Page Recall:      {correct}/{total_relevant} = {recall:.1%}")
    print(f"Page Precision:   {correct}/{total_returned} = {precision:.1%}")
    print(f"Avg Pages/Query:  {total_returned/n:.1f}")
    print("="*80)


if __name__ == "__main__":
    main()
