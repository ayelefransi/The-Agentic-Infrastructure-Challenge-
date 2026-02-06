from chimera.skills.trend_fetcher import TrendFetcher
import pytest

@pytest.mark.asyncio
async def test_trend_fetcher_contract():
    """
    FR 2.2: Trend Spotter
    Ensures that the fetcher returns data matching the standardized schema.
    """
    fetcher = TrendFetcher()
    
    # Act
    result = await fetcher.fetch_trends("crypto")

    # Assert
    assert "timestamp" in result
    assert "trends" in result
    assert isinstance(result["trends"], list)
    assert len(result["trends"]) > 0
    assert result["trends"][0]["name"] == "AI Agents in crypto"

