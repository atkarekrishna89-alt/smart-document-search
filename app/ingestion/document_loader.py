import fitz
from pathlib import Path


def extract_pdf(file_path: str) -> list[dict]:
    """Extract text from a PDF while preserving page numbers."""

    path = Path(file_path)

    if not path.is_file():
        raise FileNotFoundError(f"PDF file not found: {file_path}")

    pages = []

    try:
        with fitz.open(path) as pdf:
            for page_number, page in enumerate(pdf, start=1):
                text = page.get_text("text").strip()

                pages.append({
                    "page_number": page_number,
                    "text": text
                })

    except (fitz.FileDataError, ValueError) as exc:
        raise ValueError(f"Unable to read PDF: {file_path}") from exc

    return pages