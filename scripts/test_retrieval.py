import sys
from pathlib import Path
import logging

sys.path.insert(0, str(Path(__file__).parent.parent))

from src.config import settings
from src.retrieval.hybrid_search import HybridRetriever
from src.retrieval.reranker import Reranker
from src.retrieval.page_aggregator import PageAggregator

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


def test_retrieval():
    """Test the retrieval pipeline with sample queries."""
    
    # Sample queries from eval dataset
    test_queries = [
        "What is the first action after positive rate of climb?",
        "What does the amber STAIRS OPER light indicate?",
        "Where is the ISOLATION VALVE switch set during After Start Procedure?",
    ]
    
    # Initialize retrieval components
    logger.info("Initializing retrieval pipeline...")
    retriever = HybridRetriever(
        persist_dir=settings.chroma_persist_dir,
        embedding_model=settings.embedding_model
    )
    
    reranker = Reranker(model_name=settings.reranker_model)
    
    # Test each query
    for query in test_queries:
        logger.info("\n" + "="*80)
        logger.info(f"QUERY: {query}")
        logger.info("="*80)
        
        # Hybrid search
        results = retriever.search(query, top_k=settings.hybrid_top_k)
        logger.info(f"Hybrid search returned {len(results)} results")
        
        # Rerank
        reranked = reranker.rerank(query, results, top_k=settings.rerank_top_k)
        logger.info(f"Reranked to top {len(reranked)} results")
        
        # Extract pages
        pages = PageAggregator.extract_pages(
            reranked,
            max_pages=settings.max_pages_default,
            score_key='rerank_score'
        )
        
        # Display results
        logger.info(f"\nTop 3 results:")
        for i, result in enumerate(reranked[:3], 1):
            logger.info(f"\n  [{i}] Page {result['page_number']} "
                       f"(RRF: {result['rrf_score']:.4f}, "
                       f"Rerank: {result['rerank_score']:.4f})")
            logger.info(f"      {result['original_text'][:200]}...")
        
        logger.info(f"\nExtracted pages: {pages}")
        logger.info("="*80 + "\n")


if __name__ == "__main__":
    test_retrieval()
