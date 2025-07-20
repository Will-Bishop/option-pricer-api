from app.model import black_scholes
import pytest

def test_black_scholes_call():
    result = black_scholes(S=100, K=100, T=1, r=0.05, sigma=0.2, option_type="call")
    assert result > 0

def test_black_scholes_put():
    result = black_scholes(S=100, K=100, T=1, r=0.05, sigma=0.2, option_type="put")
    assert result > 0

def test_invalid_option_type():
    with pytest.raises(ValueError):
        black_scholes(S=100, K=100, T=1, r=0.05, sigma=0.2, option_type="banana")
