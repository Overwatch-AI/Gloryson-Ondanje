import sys
from pathlib import Path
import logging

sys.path.insert(0, str(Path(__file__).parent.parent))

from src.config import settings
from src.ingestion.pdf_parser import PDFParser, group_by_page
from src.ingestion.chunker import Chunker
from src.ingestion.contextualizer import Contextualizer

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')
logger = logging.getLogger(__name__)


def main():
    # Parse PDF
    pdf_path = Path(settings.raw_pdf_path)
    if not pdf_path.exists():
        logger.error(f"PDF not found: {pdf_path}")
        sys.exit(1)
    
    parser = PDFParser(str(pdf_path))
    elements = parser.parse()
    
    parsed_path = Path(settings.processed_chunks_path).parent / "parsed_elements.json"
    parser.save(elements, str(parsed_path))
    
    # Group by page
    pages = group_by_page(elements)
    logger.info(f"Grouped into {len(pages)} pages")
    
    # Create chunks
    chunker = Chunker(chunk_size=settings.chunk_size, overlap=settings.chunk_overlap)
    chunks = chunker.chunk_pages(pages)
    
    # Add context
    contextualizer = Contextualizer(settings.gemini_api_key)
    chunks = contextualizer.add_context(chunks)
    
    # Save
    chunker.save(chunks, settings.processed_chunks_path)
    
    logger.info(f"✓ Complete: {len(chunks)} contextualized chunks from {len(pages)} pages")


if __name__ == "__main__":
    main()