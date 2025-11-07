"""Tests for document processor."""

import pytest
from pathlib import Path
from processor import DocumentProcessor


def test_document_processor_init():
    """Test DocumentProcessor initialization."""
    processor = DocumentProcessor()
    assert processor is not None
    assert len(processor.supported_formats) == 2
    assert ".pdf" in processor.supported_formats
    assert ".docx" in processor.supported_formats


def test_is_supported():
    """Test file format support checking."""
    processor = DocumentProcessor()

    assert processor.is_supported("test.pdf") is True
    assert processor.is_supported("test.docx") is True
    assert processor.is_supported("test.PDF") is True
    assert processor.is_supported("test.txt") is False
    assert processor.is_supported("test.doc") is False


def test_chunk_text():
    """Test text chunking."""
    processor = DocumentProcessor()

    text = "a" * 1000
    chunks = processor.chunk_text(text, chunk_size=300, overlap=50)

    assert len(chunks) > 1
    assert all(len(chunk) <= 300 for chunk in chunks)


def test_preprocess_text():
    """Test text preprocessing."""
    processor = DocumentProcessor()

    # Test whitespace cleanup
    text = "Hello    World  \n\n  Test"
    cleaned = processor.preprocess_text(text)
    assert "  " not in cleaned
    assert "\n\n" not in cleaned

    # Test null character removal
    text_with_null = "Hello\x00World"
    cleaned = processor.preprocess_text(text_with_null)
    assert "\x00" not in cleaned
