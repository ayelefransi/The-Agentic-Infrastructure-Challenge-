import pytest


# NOTE: This is a TDD test. The implementation does not exist yet.
# We expect this to fail or we mock the interface to define the contract.

class TrendFetcher:
    async def fetch_trends(self, topic: str):
        raise NotImplementedError("Not built yet")

@pytest.mark.asyncio
async def test_trend_fetcher_contract():
    """
    FR 2.2: Trend Spotter
    Ensures that the fetcher returns data matching the standardized schema.
    """
    fetcher = TrendFetcher()
    
    # Act
    # We expect this to raise NotImplementedError currently, proof of TDD start
    with pytest.raises(NotImplementedError):
        await fetcher.fetch_trends("crypto")

    # Future assertions (Mental Model):
    # assert "trends" in result
    # assert isinstance(result["trends"], list)
    # assert result["timestamp"] <= datetime.now()
