import ollama


def generate_answer(question: str, context_chunks: list[str]) -> str:


    context = "\n\n".join(context_chunks)

    prompt = f"""
You are a helpful assistant.

Answer the question using ONLY the context below.

If the answer is not in the context, say "I don't know based on the document."

---

Context:
{context}

---

Question:
{question}
"""

    response = ollama.chat(
        model="llama3.2",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response["message"]["content"]