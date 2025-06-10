# Retrival from pdf using RAG

This project indexes a PDF document using OpenAI embeddings and stores them in a Qdrant vector database using LangChain. It enables semantic search and retrieval for applications like chatbots, intelligent search, or document Q&A systems.

## 🚀 Features

- ✅ Load and process a PDF (`crime-and-punishment.pdf`)
- ✅ Split text into context-aware chunks
- ✅ Generate vector embeddings using OpenAI’s `text-embedding-3-small`
- ✅ Store embeddings in Qdrant for fast semantic search

## 🛠️ Installation

1. **Clone the repo**:
   ```bash
   git clone https://github.com/yourusername/pdf-vector-indexer.git
   cd pdf-vector-indexer
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up `.env`**:
   Create a `.env` file with your OpenAI API key:
   ```
   OPENAI_API_KEY=your_openai_api_key
   ```

4. **Start Qdrant locally**:
   You can use Docker:
   ```bash
   docker run -p 6333:6333 -p 6334:6334 qdrant/qdrant
   ```

## 🧾 Usage

Make sure `crime-and-punishment.pdf` is in the same directory as the script.

Run the script:

```bash
python main.py
```

You should see:

```
indexing done
```

This indicates that your PDF content has been embedded and stored in Qdrant.

## 🧠 Technologies Used

- [LangChain](https://github.com/langchain-ai/langchain)
- [OpenAI API](https://platform.openai.com/docs/guides/embeddings)
- [Qdrant](https://qdrant.tech/)
