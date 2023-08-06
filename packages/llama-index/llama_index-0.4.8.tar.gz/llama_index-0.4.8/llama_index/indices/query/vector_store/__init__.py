"""Query classes for vector store indices."""

from llama_index.indices.query.vector_store.faiss import GPTFaissIndexQuery
from llama_index.indices.query.vector_store.simple import GPTSimpleVectorIndexQuery
from llama_index.indices.query.vector_store.weaviate import GPTWeaviateIndexQuery

__all__ = ["GPTFaissIndexQuery", "GPTSimpleVectorIndexQuery", "GPTWeaviateIndexQuery"]
