🚀 GenAI Engineering Projects – From RAG to Agents
A hands-on collection of Generative AI engineering modules covering:

LLM integration
Structured output generation
RAG (Retrieval Augmented Generation)
AI Evaluation
AI Agents
Web deployment using Streamlit
Built using Python, LiteLLM, Groq API, and Streamlit

📂 Project Structure
m1-ai-explainer/               → Basic LLM integration
m2-structured-ans-generator/   → Structured output generation
m3-architecture/               → LLM system architecture                
m5-ragintro/                   → Retrieval Augmented Generation (RAG)
m6-agents/                     → Resume Evaluation AI Agent (Web App)

🧠 Module Overview
🔹 Module 1 – AI Explainer
Basic LLM interaction using LiteLLM and Groq API.

Connect model
Send prompt
Get response
🔹 Module 2 – Structured Answer Generator
Generate structured responses using system prompts.

Controlled output format
Step-by-step reasoning
Structured responses
🔹 Module 3 – Architecture
Understanding:

LLM Layer
Prompt Engineering
Separation of logic
Clean project structure
🔹 Module 4 – Evaluation
Evaluate AI responses based on:

Accuracy
Completeness
Structure
Score-based assessment
🔹 Module 5 – RAG Intro
Implementation of Retrieval Augmented Generation.

Pipeline:

User Question
    ↓
Retrieve Relevant Context
    ↓
Send Context + Question to LLM
    ↓
Generate Answer
Features:

Context retrieval
Chunk-based processing
LLM answer generation
🔹 Module 6 – AI Resume Evaluation Agent
An intelligent agent that:

Compares resume with job description
Identifies matched skills
Identifies missing skills
Generates improvement suggestions
Provides final score out of 10
Includes:

Agent brain
Tool functions
LLM reasoning layer
Streamlit Web Interface
🛠️ Tech Stack
Python
LiteLLM
Groq API
Streamlit
python-dotenv
Modular AI Architecture
⚙️ Setup Instructions
1️⃣ Clone Repository
git clone <your-repo-url>
cd day-2-engg-main
2️⃣ Install Dependencies
python -m pip install -r requirements.txt
Or manually:

pip install litellm streamlit python-dotenv
3️⃣ Add Environment Variables
Create .env file:

GROQ_API_KEY=your_groq_api_key
MODEL_NAME=groq/llama-3.1-8b-instant
▶️ Run Modules
Run RAG
cd m5-ragintro
python main.py
Run Resume Agent Web App
cd m6-agents
python -m streamlit run app.py
Open in browser:

http://localhost:8501
🎯 Learning Outcomes
After completing these modules, you understand:

How to integrate LLM APIs
How to build RAG systems
How to build AI agents
How to structure AI projects professionally
How to deploy AI systems as web apps
📈 Future Improvements
Add vector database (FAISS / Pinecone)
Add semantic skill matching
Add PDF resume upload
Add deployment to Render / Railway
Add Docker support
