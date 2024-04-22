from typing import Required
from pydantic import BaseModel, Field


class RettificheBIInfo(BaseModel):
        isin_sottostante: Required[str] = Field(
        description="Unico codice di 12 cifre presente nell'OGGETTO del testo"
    )
        fattore_rettifica: Required[str] = Field(
            description="Fattore di rettifica",
    )
        ex_date: Required[str] = Field(
        description = "Data di efficacia della rettifica",
    )

