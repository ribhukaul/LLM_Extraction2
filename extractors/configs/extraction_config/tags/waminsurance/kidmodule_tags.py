from typing import List

from pydantic import BaseModel, Field

NF = "not found"
NA = "N/A"

class InformazioniPremio(BaseModel):
    indicatore_sintetico_rischio: int = Field(NF, description="Indicatore Sintetico di Rischio")
    periodo_detenzione_raccomandato: str = Field(NF, description="periodo di detenzione raccomandato in anni")
    date: str = Field(NF, description="data di realizzazione del documento")
    premio: int = Field(NF,description="Esempio di Investimento")

class SottostanteInfo(BaseModel):
    nome_sottostante: str = Field(NF, description="Nome proprio della denominazione della gestione o del fondo")
    tipo_gestione: str = Field(NF,description="Tipo di gestione", enum=['Fondo Intero', 'Gestione Separata'])