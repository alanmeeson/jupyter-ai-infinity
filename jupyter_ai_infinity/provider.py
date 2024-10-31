import os
import json
from typing import ClassVar, List

from jupyter_ai_magics.embedding_providers import BaseEmbeddingsProvider
from langchain_community.embeddings import InfinityEmbeddings


class InfinityEmbeddingsProvider(BaseEmbeddingsProvider, InfinityEmbeddings):
    id = "infinity-embeddings"
    name = "Infinity API"
    model_id_key = "model"
    models = json.loads(os.getenv("INFINITY_EMBEDDING_MODELS", '["*"]'))
    infinity_api_url: ClassVar[str] = os.getenv("INFINITY_API_URL")
