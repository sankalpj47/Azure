# Project Absola - Local Legal Document Analyzer

⚖️ **Privacy-First AI-Powered Legal Document Analysis**

[![CI/CD](https://github.com/Digvijay-x1/Azure/actions/workflows/ci.yml/badge.svg)](https://github.com/Digvijay-x1/Azure/actions/workflows/ci.yml)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)

## 🚀 Overview

Project Absola is a comprehensive local legal document analyzer built with Python and Streamlit. It provides AI-powered document analysis, summarization, Q&A, and legal research capabilities - all running **100% locally** with no cloud dependencies.

### Key Features

- 📄 **Document Processing**: Upload and analyze PDF/DOCX legal documents
- 🤖 **AI Summarization**: Powered by T5 transformer model
- 💬 **RAG-based Q&A**: Context-aware question answering using FAISS + LangChain
- 🌐 **Legal Web Scraping**: Access TLDR Legal and Indian Kanoon databases
- 🔒 **Privacy-First**: 100% local processing, no cloud, no telemetry
- ⚡ **Performance Optimized**: <60s/page processing, <10s query response
- 💾 **Memory Efficient**: Runs on 8GB VRAM/RAM
- 🐳 **Docker Ready**: Containerized deployment available

## 🔧 Installation

### Prerequisites

- Python 3.10 or higher
- 8GB RAM minimum
- CUDA-compatible GPU (optional, for faster processing)

### Standard Installation

```bash
# Clone the repository
git clone https://github.com/Digvijay-x1/Azure.git
cd Azure

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Docker Installation

```bash
# Build the Docker image
docker build -t project-absola .

# Run the container
docker run -p 8501:8501 project-absola
```

## 🚀 Quick Start

```bash
# Run Streamlit app
streamlit run app.py
```

The application will open in your browser at `http://localhost:8501`

### Basic Usage

1. **Upload Document**: Navigate to "Document Upload" and upload a PDF or DOCX file
2. **Summarize**: Click "Generate Summary" to get AI-powered summary
3. **Index for Q&A**: Click "Index Document" to enable question answering
4. **Ask Questions**: Go to "RAG Q&A" tab and ask questions about your document
5. **Legal Research**: Use "Legal Scraper" to search license info and case law

## ✨ Features

### Document Processing
- Supported Formats: PDF, DOCX
- Performance: <60 seconds per page

### AI Summarization
- Model: T5-base
- Speed: 5-15 seconds per summary

### RAG-Powered Q&A
- Vector Store: FAISS
- Embeddings: Sentence Transformers
- Query Response: <10 seconds

### Legal Web Scraping
- TLDR Legal: Software license summaries
- Indian Kanoon: Indian legal case database

## 🏗️ Architecture

```
Azure/
├── models/              # AI model loaders (T5, Llama3)
├── processor/           # Document processing
├── rag/                 # RAG system (FAISS + LangChain)
├── scraper/             # Web scraping utilities
├── tests/               # Test suite
├── app.py               # Main Streamlit application
├── requirements.txt     # Python dependencies
└── Dockerfile           # Docker configuration
```

## 🔒 Privacy & Security

✅ **100% Local Processing**  
✅ **No Cloud Dependencies**  
✅ **No Telemetry**  
✅ **Security Scanning** (Snyk)

## 🧪 Testing

```bash
pytest --cov=. --cov-report=html
```

CI/CD: GitHub Actions with pytest, black, flake8, mypy, Docker, Snyk

## 📄 License

MIT License

---

**Project Absola** - Built with ❤️ for privacy-conscious legal professionals.
