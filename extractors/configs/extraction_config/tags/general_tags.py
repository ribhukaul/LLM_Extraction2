from langchain_core.pydantic_v1 import BaseModel, Field


class DocLanguage(BaseModel):
    language: str = Field('it', description="language of the document, can be Italin (it) or English (en)", enum=["it", "en"])

class IsFirstPage(BaseModel):
    is_first_page: bool = Field(..., description="True if the page is the first one, False otherwise")

