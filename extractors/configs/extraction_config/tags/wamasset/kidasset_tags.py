from pydantic import BaseModel, Field


NFE = '0€'
NFP = '0%'
NF = 'N/A'


NFD = 'Per questo prodotto non si applicano le commissioni di performance'


# Informazioni di base del KID
class InformazioniBase(BaseModel):
    indicatore_sintetico_rischio: int = Field(NF, description="Indicatore Sintetico di Rischio")
    periodo_detenzione_raccomandato: str = Field(NF, description="periodo di detenzione raccomandato in anni")
    date: str = Field(NF, description="data di realizzazione del documento (chiamata anche data di validità del KID")

class PicPac(BaseModel):
    picpac: str = Field(NF, description="Indica se il prodotto è un PIC (Piano Individuale di Risparmio) o un PAC (Piano di Accumulo Capitale)",
                        enum=["PIC", "PAC", "N/A"]
                        )

# Tabella costi di ingresso e uscita e diritti fissi entrata uscita
class TabellaCostiIngressoDirttiFissi(BaseModel):
    costi_ingresso: str = Field(
        NFP, description="valore in PERCENTUALE % (nella prima colonna)"
    )
    costingresso_dirittifissi: str =Field(
          NFE, description="Diritti fissi di ingresso valore in EURO (è un valore unico)"
      )
    costi_uscita: str = Field(
        NFP, description="valore in PERCENTUALE% (nella  prima colonna)"
    )
    costiuscita_dirittifissi: str = Field(
          NFE, description="Diritti fissi d'uscita valore in Euro"
      )

# Tabella costi di gestione/transazione/performance e descrizione performance 
class TabellaCostiGestionePerformance(BaseModel):
    commissione_gestione: str = Field(NFP, description="Commissioni di gestione in PERCENTUALE % (prima colonna)")
    commissione_transazione: str = Field(NFP, description="Costi di transazione in PERCENTUALE % (prima colonna, esiste sempre un valore)")
    descrizione_performance: str = Field(NFD,description= "tutta la scritta relativa alle commmissioni di performance (prima colonna)")
    commissione_performance: str = Field(NFE, description="Commissioni di performance IN EURO (colonna più a destra)")

