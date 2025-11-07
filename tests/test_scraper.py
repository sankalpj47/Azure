"""Tests for web scraper."""

import pytest
from scraper import LegalScraper, TLDRLegalScraper, IndianKanoonScraper


def test_legal_scraper_init():
    """Test LegalScraper initialization."""
    scraper = LegalScraper(delay=1.0)
    assert scraper is not None
    assert scraper.tldr_scraper is not None
    assert scraper.kanoon_scraper is not None


def test_tldr_scraper_init():
    """Test TLDRLegalScraper initialization."""
    scraper = TLDRLegalScraper(delay=0.5)
    assert scraper is not None
    assert scraper.delay == 0.5
    assert scraper.BASE_URL == "https://tldrlegal.com"


def test_kanoon_scraper_init():
    """Test IndianKanoonScraper initialization."""
    scraper = IndianKanoonScraper(delay=0.5)
    assert scraper is not None
    assert scraper.delay == 0.5
    assert scraper.BASE_URL == "https://indiankanoon.org"
