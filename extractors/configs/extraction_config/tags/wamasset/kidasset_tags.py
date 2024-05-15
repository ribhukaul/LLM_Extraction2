from pydantic import BaseModel, Field


NFE = '0.0 €'
NFP = '0.0 %'
NF = 'N/A'


NFD = 'Per questo prodotto non si applicano le commissioni di performance'
NFD_ENG = 'There is no performance fee for this product.'


# Informazioni di base del KID
#BASE INFORMATION OF KID
#ITA
class InformazioniBase(BaseModel):
    indicatore_sintetico_rischio: int = Field(NF, description="Indicatore Sintetico di Rischio")
    periodo_detenzione_raccomandato: str = Field(NF, description="periodo di detenzione raccomandato in anni")
    date: str = Field(NF, description="data di realizzazione del documento (chiamata anche data di validità del KID")
    classe_fondo: str = Field(NF, description="""Classe del fondo, inserita come lettera (o lettere maiuscole) nel nome del prodotto. 
                              esempio di classi sono 'A', 'B', 'C', 'PIR', 'F2' etc. Può anche non essere espressa""")
#ENG
class BasicInformation(BaseModel):
    indicatore_sintetico_rischio: int = Field(NF, description="Synthetic Risk Indicator")
    periodo_detenzione_raccomandato: str = Field(NF, description="recommended holding period in years")
    date: str = Field(NF, description="date of creation of the document (also called KID validity date)in the format DD/MM/YYYY")
    classe_fondo: str = Field(NF, description="""share class, entered as a letter (or uppercase letters) in the product name.
                                example of classes are 'A', 'B', 'C', 'PIR', 'F2' etc. It may not be expressed""")

# PIC/PAC
#ITA
class PicPac(BaseModel):
    picpac: str = Field(NF, description="Indica se il prodotto è un PIC (Piano Individuale di Risparmio) o un PAC (Piano di Accumulo Capitale)",
                        enum=["PIC", "PAC", "N/A"]
                        )
#ENG
# class PicPacEng(BaseModel):
#     picpac: str = 'N/A'

#FUND CLASS
# class FundClass(BaseModel):
#     classe_fondo: str = Field(NF, description="""Classe del fondo, inserita come lettera (o lettere maiuscole) 
#                               esempio di classi sono 'A', 'B', 'C', 'PIR', 'F2' etc. Può anche non essere espressa""")

# COSTS
#ENTRY/EXIT COSTS DIRITTI FISSI
#ITA
class TabellaCostiIngressoDirttiFissi(BaseModel):
    costi_ingresso: str = Field(
        NFP, description="valore in PERCENTUALE % (nella prima colonna), '0%' se non presente"
    )
    costingresso_dirittifissi: str =Field(
          NFE, description="Diritti fissi di ingresso valore in EURO (è un valore unico), '0€' se non presente"
      )
    costi_uscita: str = Field(
        NFP, description="valore in PERCENTUALE% (nella  prima colonna), '0%' se non presente"
    )
    costiuscita_dirittifissi: str = Field(
          NFE, description="Diritti fissi d'uscita valore in Euro (è un valore unico), '0€' se non presente"
      )
#ENG
class TableEntryExitFixedRights(BaseModel):
    costi_ingresso: str = Field(
        NFP, description="value in PERCENTAGE % (in the first column), '0%' if not present"
    )
    costingresso_dirittifissi: str = '-'
    costi_uscita: str = Field(
        NFP, description="value in PERCENTAGE% (in the first column), '0%' if not present"
    )
    costiuscita_dirittifissi: str = '-'

# MANAGEMENT COSTS
#ITA
class TabellaCostiGestionePerformance(BaseModel):
    commissione_gestione: str = Field(NFP, description="Commissioni di gestione in PERCENTUALE % (prima colonna)")
    commissione_transazione: str = Field(NFP, description="Costi di transazione in PERCENTUALE % (prima colonna, esiste sempre un valore)")
    descrizione_performance: str = Field(NFD,description= "tutta la scritta relativa alle commmissioni di performance (prima colonna)")
    commissione_performance: str = Field(NFE, description="Commissioni di performance IN EURO (colonna più a destra)")
#ENG
class TableManagementPerformance(BaseModel):
    commissione_gestione: str = Field(NFP, description="Management fees in PERCENTAGE % (first column)")
    commissione_transazione: str = Field(NFP, description="Transaction costs in PERCENTAGE % (first column, there is always a value)")
    descrizione_performance: str = Field(NFD_ENG,description= "all the writing related to performance commissions (first column)")
    commissione_performance: str = Field(NFE, description="Performance fees IN EURO (rightmost column)")

