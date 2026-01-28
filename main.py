from chatbot import loader, chunker, embeddings, engine


def main():
    print("Starting LinkedIn Chatbot...\n")

    print("Loading LinkedIn profile...")
    profile_text = loader.load_profile('data/linkedin_profile.txt')

    print("Chunking text...")
    text_chunks = chunker.chunker(profile_text)
    print(f"Created {len(text_chunks)} chunks\n")

    print("Creating embeddings and building search index...")
    embeddings.create_embeddings(text_chunks)
    print("Ready!\n")

    chat = engine.ChatbotEngine()

    print("Ask me anything about the LinkedIn profile! (type 'quit' to exit)\n")

    while True:
        question = input("You: ").strip()

        if question.lower() in ['quit', 'exit', 'q']:
            print("Chat closing...\n")
            break

        if not question:
            continue

        print("\nThinking...\n")
        answer = chat.ask(question)
        print(f"Bot: {answer}\n")


if __name__ == "__main__":

    main()
