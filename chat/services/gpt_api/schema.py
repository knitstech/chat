from pydantic import BaseModel


class GPTModel(BaseModel):
    """Simple message model."""

    id: str
    object: str = "model"
    created_at: int  # will be transormed into datetime
    owned_by: str = "openai"
