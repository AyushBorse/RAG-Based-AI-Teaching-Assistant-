🎓 RAG AI Teaching Assistant for Python Lectures
Built with Llama 3.2








An AI-powered Retrieval Augmented Generation (RAG) Teaching Assistant that answers questions from Python lecture videos.

This project processes lecture videos and converts them into searchable knowledge. Users can ask questions, and the system retrieves the most relevant lecture segments and generates answers using Llama 3.2.

This allows students to interact with lecture content like a chatbot instead of manually searching through videos.

🚀 Features

📹 Process Python lecture videos

🎧 Convert videos into MP3 audio

📝 Generate JSON transcripts

🧠 Create vector embeddings

🔎 Retrieve relevant lecture content

🤖 Generate contextual answers using Llama 3.2

📚 Works like a personal AI tutor for Python

🧠 System Architecture
Video Lectures
      │
      ▼
Convert Video → MP3
      │
      ▼
Speech to Text
(JSON Transcripts)
      │
      ▼
Generate Embeddings
      │
      ▼
Store in Vector Dataset
(Joblib DataFrame)
      │
      ▼
User Question
      │
      ▼
Retrieve Relevant Context
      │
      ▼
Generate Answer with Llama 3.2
📂 Project Pipeline
Step 1 — Collect Videos

Move all Python lecture videos into the videos/ folder.

videos/
   python_lecture1.mp4
   python_lecture2.mp4
Step 2 — Convert Videos to MP3

Run the script:

python video_to_mp3.py

This converts all videos into audio files.

Output:

audio/
   python_lecture1.mp3
   python_lecture2.mp3
Step 3 — Convert MP3 to JSON Transcript

Run:

python mp3_to_json.py

This converts audio into text transcripts and stores them as JSON.

Example output:

transcripts/
   lecture1.json
   lecture2.json

Example JSON structure:

{
  "timestamp": "00:01:23",
  "text": "In Python, lists are used to store multiple items in a single variable."
}
Step 4 — Generate Vector Embeddings

Run:

python preprocess_json.py

This script:

Reads all transcript JSON files

Converts text into vector embeddings

Stores embeddings in a DataFrame

Saves the result as a Joblib pickle file

Output:

embeddings.pkl
Step 5 — Query the AI Assistant

When a user asks a question:

Load the embeddings file

Retrieve the most relevant transcript segments

Create a prompt with context

Send it to Llama 3.2

Generate an answer

Example:

User: What is a Python list?

The assistant searches lecture transcripts and returns the most relevant explanation.

📁 Project Structure
rag-python-teaching-assistant
│
├── videos/
│
├── audio/
│
├── transcripts/
│
├── video_to_mp3.py
├── mp3_to_json.py
├── preprocess_json.py
│
├── embeddings.pkl
│
└── README.md
⚙️ Installation

Clone the repository:

git clone https://github.com/yourusername/rag-python-teaching-assistant.git

Navigate into the project folder:

cd rag-python-teaching-assistant

Install required dependencies:

pip install -r requirements.txt
🧰 Technologies Used

Python

Llama 3.2

Retrieval Augmented Generation (RAG)

Speech-to-Text

Embeddings

Joblib

Pandas

💡 Use Cases

AI tutor for Python programming

Lecture Q&A assistant

Educational chatbot

Knowledge retrieval system for courses

Interactive learning tool

🔮 Future Improvements

Add FAISS / Chroma vector database

Web interface using Streamlit

Upload YouTube lectures automatically

Add real-time question answering

Multi-course support (Python, ML, Data Science)

👨‍💻 Author

Ayush Borse

Electronics and Telecommunication Engineering
Interested in AI, Data Science, and Intelligent Systems

📧 Email: ayushborse40@gmail.com

⭐ If you found this project useful, consider starring the repository.
