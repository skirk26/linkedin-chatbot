SYSTEM_PROMPT = """You are helpful chatbot that answers questions about a Linkedin profile. Use the given context to answer questions accurately and quickly. If the answer is not available, say the answer cant be found"""

def prompt_format(question, answer):
    formatted_answer = "\n\n".join([chunk for chunk, score in answer])

    prompt = f"""{SYSTEM_PROMPT}

    Context from LinkedIn profile:
    {formatted_answer}

    Question: {question}

    Answer:"""

    return prompt