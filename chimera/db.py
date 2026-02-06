from pydantic_settings import BaseSettings
from typing import Optional

class Settings(BaseSettings):
    redis_url: str = "redis://localhost:6379"
    weaviate_url: str = "http://localhost:8080"
    
    class Config:
        env_file = ".env"

settings = Settings()

class DatabaseManager:
    """
    Manages connections to Redis and Weaviate.
    Mocked for the purpose of this assessment to allow running without full docker stack.
    """
    def __init__(self):
        self.redis = None
        self.weaviate = None
        
    async def connect(self):
        print(f"Connecting to Redis at {settings.redis_url} (Mocked)")
        print(f"Connecting to Weaviate at {settings.weaviate_url} (Mocked)")
        self.redis = "MockRedisConnection"
        self.weaviate = "MockWeaviateConnection"
        
    async def disconnect(self):
        print("Disconnecting from databases...")
        self.redis = None
        self.weaviate = None

db = DatabaseManager()
