"""Base vector store index query."""


from typing import Any, Generic, Optional, TypeVar

from llama_index.data_structs.data_structs import IndexStruct
from llama_index.embeddings.base import BaseEmbedding
from llama_index.indices.query.base import BaseGPTIndexQuery

BID = TypeVar("BID", bound=IndexStruct)


class BaseGPTVectorStoreIndexQuery(BaseGPTIndexQuery[BID], Generic[BID]):
    """Base vector store query."""

    def __init__(
        self,
        index_struct: BID,
        embed_model: Optional[BaseEmbedding] = None,
        similarity_top_k: Optional[int] = 1,
        **kwargs: Any,
    ) -> None:
        """Initialize params."""
        super().__init__(index_struct=index_struct, embed_model=embed_model, **kwargs)
        self.similarity_top_k = similarity_top_k
