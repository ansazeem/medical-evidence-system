# medical-evidence-system

A RAG pipeline for answering medical and public health queries, with a focus on Pakistan-specific epidemiological data. It retrieves evidence from the web and a local vector store, scores source reliability, reranks results, and answers with citations. When exact data is missing, it expands the query geographically and says so.

Built with LangChain, ChromaDB, Groq API (Llama-3.3-70B) and Gemini embeddings. 

## Setup
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env   # then add your keys
```

## Usage
```bash
python query.py
python -m streamlit run app.py
python eval.py --pak
```

## Files
- `pipeline.py`: core pipeline
- `eval.py`: evaluation harness
- `baseline.py`: plain Llama-3.3-70B answers with no retrieval, used as a comparison
- `pak_test_set.py`: 35 Pakistan-specific QA pairs
- `app.py`: Streamlit interface
- `server.py` and `static/`: custom HTTP server and frontend
- `query.py`: single query runner
