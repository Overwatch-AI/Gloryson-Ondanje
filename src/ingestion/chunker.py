import json
from pathlib import Path
from typing import List, Dict
from dataclasses import dataclass, asdict
import logging

logger = logging.getLogger(__name__)


@dataclass
class Chunk:
    """Child chunk with parent page reference."""
    chunk_id: str
    text: str
    contextualized_text: str
    page_number: int
    parent_page_text: str


class Chunker:
    """Create small searchable chunks with page-level parents."""
    
    def __init__(self, chunk_size: int = 400, overlap: int = 50):
        self.chunk_size = chunk_size
        self.overlap = overlap
    
    def chunk_pages(self, pages: Dict[int, str]) -> List[Chunk]:
        """Create child chunks from parent pages."""
        logger.info(f"Chunking {len(pages)} pages (size={self.chunk_size}, overlap={self.overlap})")
        
        all_chunks = []
        for page_num, page_text in pages.items():
            page_chunks = self._split_text(page_text, page_num, page_text)
            all_chunks.extend(page_chunks)
        
        logger.info(f"Created {len(all_chunks)} chunks")
        return all_chunks
    
    def _split_text(self, text: str, page_num: int, parent: str) -> List[Chunk]:
        """Split text into overlapping chunks."""
        chunks = []
        words = text.split()
        
        if len(words) <= self.chunk_size:
            chunks.append(Chunk(
                chunk_id=f"p{page_num}_c0",
                text=text,
                contextualized_text=text,
                page_number=page_num,
                parent_page_text=parent
            ))
            return chunks
        
        start = 0
        chunk_idx = 0
        while start < len(words):
            end = min(start + self.chunk_size, len(words))
            chunk_text = " ".join(words[start:end])
            
            chunks.append(Chunk(
                chunk_id=f"p{page_num}_c{chunk_idx}",
                text=chunk_text,
                contextualized_text=chunk_text,
                page_number=page_num,
                parent_page_text=parent
            ))
            
            chunk_idx += 1
            start += self.chunk_size - self.overlap
        
        return chunks
    
    def save(self, chunks: List[Chunk], path: str):
        """Save chunks to JSON."""
        Path(path).parent.mkdir(parents=True, exist_ok=True)
        with open(path, 'w') as f:
            json.dump([asdict(c) for c in chunks], f, indent=2)
        logger.info(f"Saved {len(chunks)} chunks to {path}")
    
    @staticmethod
    def load(path: str) -> List[Chunk]:
        """Load chunks from JSON."""
        with open(path, 'r') as f:
            data = json.load(f)
        return [Chunk(**item) for item in data]