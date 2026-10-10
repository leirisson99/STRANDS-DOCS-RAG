from strands.models.openai import OpenAIModel
from app import config

def build_model() -> OpenAIModel:
    return OpenAIModel(
        client_args={"api_key": config.OPENAI_API_KEY},
        model_id=config.MODEL_ID,
        params={"temperature":0.2, "max_tokens":1000}
    )
    
