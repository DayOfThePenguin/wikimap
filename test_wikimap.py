import wikimap
import pytest

def test_base36_encode():
    assert shortly.base36_encode(1) == "1"
    assert shortly.base36_encode(40) == "14"
