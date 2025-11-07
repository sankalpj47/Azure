"""Tests for model loader."""

import pytest
from models import ModelLoader


def test_model_loader_init():
    """Test ModelLoader initialization."""
    loader = ModelLoader(max_memory_gb=8.0)
    assert loader is not None
    assert loader.max_memory_gb == 8.0
    assert loader.device in ["cuda", "cpu"]


def test_model_loader_memory_limit():
    """Test custom memory limits."""
    loader = ModelLoader(max_memory_gb=4.0)
    assert loader.max_memory_gb == 4.0


def test_unload_models():
    """Test model unloading."""
    loader = ModelLoader()
    loader.unload_models()
    # Should not raise an error even if no models loaded
    assert loader.t5_model is None
    assert loader.llama_model is None
