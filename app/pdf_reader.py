from pypdf import PdfReader


def extract_text(pdf_path: str) -> str:
    """
    Extract all text from a PDF file.

    Args:
        pdf_path: Path to the PDF file.

    Returns:
        A string containing the text from every page.
    """

    reader = PdfReader(pdf_path)

    text = ""

    for page in reader.pages:
        page_text = page.extract_text()

        if page_text:
            text += page_text + "\n"

    return text