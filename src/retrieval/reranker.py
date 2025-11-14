import logging

from FlagEmbedding import FlagReranker

logger = logging.getLogger(__name__)


class Reranker:
    """
    Cross-encoder reranker for re-scoring retrieved chunks.
    """

    def __init__(
        self, model_name: str = "BAAI/bge-reranker-v2-m3", use_fp16: bool = False
    ):
        """
        Initialize reranker model.
        """
        logger.info(f"Loading reranker model: {model_name}")
        self.model = FlagReranker(model_name, use_fp16=use_fp16)
        logger.info("Reranker ready")

    def rerank(self, query: str, results: list[dict], top_k: int = 10) -> list[dict]:
        """
        Rerank retrieved results using cross-encoder.
        """
        if not results:
            return []

        logger.info(f"Reranking {len(results)} results (top_k={top_k})")

        # Prepare (query, document) pairs
        pairs = [[query, result["original_text"]] for result in results]

        # Get rerank scores
        scores = self.model.compute_score(pairs, normalize=True)

        # Handle single result case
        if isinstance(scores, float):
            scores = [scores]

        # Add rerank scores to results
        for result, score in zip(results, scores):
            result["rerank_score"] = float(score)

        # Sort by rerank score descending
        reranked = sorted(results, key=lambda x: x["rerank_score"], reverse=True)

        logger.info(f"Reranked to top {min(top_k, len(reranked))} results")
        return reranked[:top_k]
