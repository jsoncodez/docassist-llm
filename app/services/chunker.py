def chunk_text(text: str, chunk_size: int = 500, overlap: int = 100):

    # Note, overlap int = 100.  reason for overlap is to prevent breaking up mid sentence.

    chunks = []

    start = 0
    text_length = len(text)

    while start < text_length:
        end = start + chunk_size

        chunk = text[start:end]

        chunks.append(chunk)


        start += chunk_size - overlap

    return chunks