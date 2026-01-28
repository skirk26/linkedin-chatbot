This is an AI powered chatbot that answers questions about a 
Linkedin profile using a semantic search and natural language generation.
The system loads my Linkedin profile from a text file, separates it into
chunks manageable for the AI, and converts those chunks into
numerical vectors using Sentence Transformers. These vectors
are stored in a FAISS index for fast similarity search, allowing
the chatbot to quickly find relevant information when users ask questions

When a question is asked, the chatbot looks through all the relevant chunks
from the Linkedin profile. Once it has done that, it uses Groq's LLM API
to generate natural human-like answers based on the retrieved context.
I used free tier API's and local processing, which made it a more cost effective and
easy way to learn about AI. I was able to learn a lot about the practical applications
of Retrieval-Augmented Generation for AI assistants

To use the chatbot, simply add your LinkedIn information to data/linkedin_profile.txt, 
get a free API key from Groq, install the dependencies, and run python main.py. 
The chatbot works best with specific questions that include keywords from your profile, 
such as "What projects has Sam worked on?" or "Tell me about Sam's Python experience."


Prereqs:
    Python 3.11+,
    pip  
Dependencies:
    pip install -r requirements.txt  
Groq API key:
    https://console.groq.com/keys  
Tips for best chat results:
    Be very specific with questions, 
    Use keywords from profile, 
    Ask concrete, simple questions
