import pytest

from pywinos import WinOSClient


def test_session():
    """Host and credentials are mandatory"""

    with pytest.raises(TypeError):
        assert WinOSClient()._session
