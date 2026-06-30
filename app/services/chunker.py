def chunk_text(text: str, chunk_size: int = 500, overlap: int = 100):
    """
    Split text into overlapping chunks.

    Why overlap?
    → So sentences that span boundaries are not lost.
    """

    chunks = []

    start = 0
    text_length = len(text)

    while start < text_length:
        end = start + chunk_size

        chunk = text[start:end]

        chunks.append(chunk)

        # move window forward with overlap
        start += chunk_size - overlap

    return chunks