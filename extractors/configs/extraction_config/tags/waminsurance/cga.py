from pydantic import BaseModel, Field


class IsVitaIntera(BaseModel):
    is_vita_intera: str = Field(False, description="Il contratto è a vita intera e dunque termina con il decesso dell'assicurato o è a tempo determinato con una scadenza?",
                                enum=["vita intera", "tempo determinato"])


class Durata(BaseModel):
    durata: str = Field(None, description="Durata del contratto, si può inserire un numero minimo e massimo di anni. Non considerare quello che è scritto in 'durata del piano'")


# PREMIUM
class IsUnico(BaseModel):
    is_unico: bool = Field(None, description="""Il premio è unico ? - premi unici aggiuntivi sono premi ricorrenti
                          - i premi riconducibili a garanzie aggiuntive non sono da considerare per la risposta(e.g. premi unici per garanzia caso morte)""")

class IsPremioRicorrente(BaseModel):
    is_premio_ricorrente: bool = Field(None, description="""Il premio è ricorrente ?
        - premi integrativi non sono premi ricorrenti
        - premi unici aggiuntivi sono premi ricorrenti""")
    # is_premio_annuo: bool = Field(None, description="""Il premio è annuo? se il premio è ricorrente, ci interessa sapere se 
    #     è annuo o meno (anno se pagato ogni anno)""")

class PremiumType(BaseModel):

    premium_type: str = Field(
        None, 
        description="""Tipologia di premio pagato dal cliente. Unico se il versamento è unico o unico aggiuntivo, ricorrente se riorrente o periodico.
        A scelta nel caso in cui si possa decidere si investire in soluzione unica o in soluzione ricorrente.
        
        - premi unici aggiuntivi sono premi ricorrenti
        - i premi riconducibili a garanzie aggiuntive non sono da considerare per la risposta(e.g. premi unici per garanzia caso morte)""", 
        enum=["unico", "periodico", "a scelta"]
        )

class PremiumBoundaries(BaseModel):
    min_premium: float = Field(None, description="Premio minimo, limite inferiore")
    max_premium: float = Field(None, description="Premio massimo, limite superiore")

    