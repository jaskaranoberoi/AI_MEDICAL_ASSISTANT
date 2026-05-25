import fitz  # PyMuPDF
from typing import List, Dict


def extract_text_from_pdf(pdf_path: str) -> Dict[str, str]:
    """
    Extract raw text from a PDF file.

    Returns:
    {
        "text": "...",
        "source": "filename.pdf"
    }
    """

    doc = fitz.open(pdf_path)
    pages_text: List[str] = []

    for page in doc:
        text = page.get_text()
        if text:
            pages_text.append(text)

    full_text = "\n".join(pages_text)

    return {
        "text": full_text.strip(),
        "source": pdf_path.split("/")[-1]
    }
