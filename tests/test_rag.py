"""Tests for RAG system."""

import pytest
from rag import RAGSystem


def test_rag_system_init():
    """Test RAGSystem initialization."""
    rag = RAGSystem()
    assert rag is not None
    assert rag.vector_store is None
    assert rag.embeddings is None


def test_rag_system_custom_model():
    """Test RAG with custom embedding model."""
    rag = RAGSystem(embedding_model="sentence-transformers/all-MiniLM-L6-v2")
    assert rag.embedding_model_name == "sentence-transformers/all-MiniLM-L6-v2"


def test_get_stats_empty():
    """Test stats for empty index."""
    rag = RAGSystem()
    stats = rag.get_stats()
    assert stats["indexed_chunks"] == 0


def test_clear_index():
    """Test clearing index."""
    rag = RAGSystem()
    rag.clear_index()
    assert rag.vector_store is None


def test_search_no_index():
    """Test search with no indexed documents."""
    rag = RAGSystem()
    results = rag.search("test query", k=5)
    assert results == []
