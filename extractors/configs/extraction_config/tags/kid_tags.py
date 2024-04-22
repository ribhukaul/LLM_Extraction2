"""
This file contains the tags used to extract the data from the KID and GKID documents.
"""

from typing import List
from pydantic import BaseModel, Field
from pydantic.fields import Optional

NF = "not found"
NA = "N/A"
###########
# GENERAL #
###########
class IsDisclaimerThere(BaseModel):
    is_disclaimer_there: bool = Field(False, description="è presente il disclaimer 'State per acquistare un prodotto che non è semplice e può essere di difficile comprensione'")
    

#######
# KID #
#######
# Informazioni di base del KID
class InformazioniBase(BaseModel):
    indicatore_sintetico_rischio: int = Field(NF, description="Indicatore Sintetico di Rischio")
    periodo_detenzione_raccomandato: str = Field(NF, description="periodo di detenzione raccomandato in anni")
    date: str = Field(NF, description="data di realizzazione del documento")

# Tabella scenati di performance in % + caso morte (1year e RHP)
class TabellaScenariPerformance(BaseModel):
    stress_return: str = Field(NF, description="Rendimento percetuale(%) o '-' 1 anno scenario di stress")
    sfavorevole_return: str = Field(NF, description="Rendimento percentuale(%) o '-'  a 1 anno scenario sfavorevole ")
    moderato_return: str = Field(NF, description="Rendimento percentuale(%) o '-'  1 anno scenario moderato")
    favorable_return: str = Field(NF, description="Rendimento percentuale(%) o '-'  a 1 anno scenario favorevole")
    stress_return_rhp: str = Field(NF, description="Rendimento percetuale(%) a RHP anni scenario di stress")
    sfavorevole_return_rhp: str = Field(NF, description="Rendimento percentuale(%) a RHP anni scenario sfavorevole")
    moderato_return_rhp: str = Field(NF, description="Rendimento percentuale(%) a RHP anni scenario moderato")
    favorable_return_rhp: str = Field(NF, description="Rendimento percentuale(%) a RHP anni scenario favorevole")
    scenario_morte_1: str = Field(NF, description="scenario morte o decesso, Valore in euro(€) o '-'  a 1 anno scenario moderato")
    scenario_morte_rhp: str = Field(NF, description="scenario morte o decesso, Valore in euro(€) a RHP anni scenario moderato")

# Tabella scenari di performance in € (1year e RHP)
class ScenariPerformanceAbsoluteEuro(BaseModel):
    stress_amount: str = Field(NF, description="Ammontare in € o '-' 1 anno(prima colonna) scenario di stress")
    sfavorevole_amount: str = Field(NF, description="Ammontare in € o '-'  a 1 anno(prima colonna) scenario sfavorevole ")
    moderato_amount: str = Field(NF, description="Ammontare in € o '-'  1 anno(prima colonna) scenario moderato")
    favorable_amount: str = Field(NF, description="Ammontare in € o '-'  a 1 anno(prima colonna) scenario favorevole")
    stress_amount_rhp: str = Field(NF, description="Ammontare in € a RHP anni(ultima colonna) scenario di stress")
    sfavorevole_amount_rhp: str = Field(NF, description="Ammontare in € a RHP anni(ultima colonna) scenario sfavorevole")
    moderato_amount_rhp: str = Field(NF, description="Ammontare in € a RHP anni(ultima colonna) scenario moderato")
    favorable_amount_rhp: str = Field(NF, description="Ammontare in € a RHP anni(ultima colonna) scenario favorevole")

# Tabella scenari di performance in % ed € + MORTE (RHP/2)
class ScenariPerformanceRHP2(BaseModel):
    stress_amount_x: str = Field(NF, description="Ammontare in € a X anni(ultima colonna) scenario di stress")
    sfavorevole_amount_x: str = Field(NF, description="Ammontare in € a X anni(ultima colonna) scenario sfavorevole")
    moderato_amount_x: str = Field(NF, description="Ammontare in € a X anni(ultima colonna) scenario moderato")
    favorable_amount_x: str = Field(NF, description="Ammontare in € a X anni(ultima colonna) scenario favorevole")
    stress_return_x: str = Field(NF, description="Rendimento percetuale(%) a X anni scenario di stress")
    sfavorevole_return_x: str = Field(NF, description="Rendimento percentuale(%) a X anni scenario sfavorevole")
    moderato_return_x: str = Field(NF, description="Rendimento percentuale(%) a X anni scenario moderato")
    favorable_return_x: str = Field(NF, description="Rendimento percentuale(%) a X anni scenario favorevole")
    scenario_morte_x: str = Field(NF, description="scenario morte o decesso, Valore in euro(€) a X anni scenario moderato")

# Tabella costi di ingresso e uscita
class TabellaCostiIngresso(BaseModel):
    costi_ingresso: str = Field(NF, description="Costi di ingresso in PERCENTUALE %(nella colonna più a destra, può essere n/a)")
    costi_uscita: str = Field(NF, description="Costi di uscita in PERCENTUALE %(nella colonna più a destra, può essere n/a)")

# Tabella costi di ingresso e uscita e diritti fissi entrata uscita
class TabellaCostiIngressoDirttiFissi(BaseModel):
    costi_ingresso: str = Field(
        NF, description="valore in PERCENTUALE% (nella prima colonna,può essere n/a)"
    )
    costingresso_dirittifissi: str =Field(
          NF, description="Diritti fissi d'uscita valore in EURO (è un valore unico)"
      )
    costi_uscita: str = Field(
        NF, description="valore in PERCENTUALE% (nella  prima colonna,può essere n/a)"
    )
    costiuscita_dirittifissi: str = Field(
          NF, description="Diritti fissi d'uscita valore in Euro (è un valore unico)"
      )

# Tabella costi di gestione/transazione/performance
class TabellaCostiGestione(BaseModel):
    commissione_gestione: str = Field(NF, description="Commissioni di gestione in PERCENTUALE % (colonna di destra)")
    commissione_transazione: str = Field(NF, description="Costi di transazione in PERCENTUALE % (colonna di destra)")
    commissione_performance: str = Field(NF, description="Commissioni di performance IN PERCENTUALE % (colonna a destra)")

# Tabella costi di gestione/transazione/performance e descrizione performance 
class TabellaCostiGestionePerformance(BaseModel):
    commissione_gestione: str = Field(NF, description="Commissioni di gestione in PERCENTUALE % (prima colonna)")
    commissione_transazione: str = Field(NF, description="Costi di transazione in PERCENTUALE % (prima colonna, esiste sempre un valore)")
    descrizione_performance: str = Field(NF,description= "tutta la scritta relativa alle commmissioni di performance(prima colonna)")
    commissione_performance: str = Field(NF, description="Commissioni di performance IN EURO  (colonna a destra)")


# Tabella RIY (Reduction in Yield) con costo totale e incidenza % (1year e RHP)
class TabellaRiy(BaseModel):
    # 1 ANNO
    incidenza_costo_perc_1year: Optional[str] = Field(
        NF, description="Impatto sul rendimento annuale dei costi in caso di uscida dopo 1 anno in PERCENTUALE%"
    )
    costi_totali_eur_1year: Optional[str] = Field(
        NF, description="Costi totali dopo 1 anno in EURO €"
    )
    # RHP
    incidenza_costo_perc_rhp: str = Field(
        NF, description="Impatto sul rendimento annuale dei costi in caso di uscida dopo RHP anni in PERCENTUALE%"
    )
    costi_totali_eur_rhp: float = Field(
        NF, description="Costi totali dopo RHP anni in EURO €"
    )

# Tabella RIY (Reduction in Yield) con incidenza % (1year e RHP)
class TabellaRiySmall(BaseModel):
    # 1 ANNO
    incidenza_costo_perc_1year: Optional[str] = Field(
        NF, description="Impatto sul rendimento annuale dei costi in caso di uscida dopo 1 anno in PERCENTUALE%"
    )
    # RHP
    incidenza_costo_perc_rhp: str = Field(
        NF, description="Impatto sul rendimento annuale dei costi in caso di uscida dopo RHP anni in PERCENTUALE%"
    )

class TabellaRiyRHP2(BaseModel):
    # 1 YEAR
    incidenza_costo_perc_1year: Optional[str] = Field(
        NF, description="Impatto sul rendimento annuale dei costi in caso di uscida dopo 1 anno in PERCENTUALE%"
    )
    costi_totali_eur_1year: Optional[str] = Field(NF, description="Costi totali dopo 1 anno in EURO €")
    # RHP/2
    incidenza_costo_perc_xyear: str = Field(
        NF, description="Impatto sul rendimento annuale dei costi in caso di uscida dopo X anni in PERCENTUALE%"
    )
    costi_totali_eur_xyear: float = Field(NF, description="Costi totali dopo X anni in EURO €")
    # RHP
    incidenza_costo_perc_rhp: str = Field(
        NF, description="Impatto sul rendimento annuale dei costi in caso di uscida dopo RHP anni in PERCENTUALE%"
    )
    costi_totali_eur_rhp: float = Field(NF, description="Costi totali dopo RHP anni in EURO €")




class ProductUnderlyingInfo(BaseModel):
    #premium_type: str = Field(NF, description="Tipo di premio, può essere 'unico iniziale' o 'premi ricorrenti'", enum=["unico iniziale", "premi ricorrenti"])
    #underlyings: List[Sottostanti] = Field(NF, description="Lista di sottostanti in cui il prodotto investe")
    is_gestione_separata: bool = Field(NF, description="True se l'opzione di investimento (non il prodotto) investe in gestione separata, False altrimenti")
    is_fondo_interno: bool = Field(NF, description="True se l'opzione di investimento (non il prodotto) investe in fondo interno, False altrimenti")
    # underlyng_type: str = Field(NF, description="Tipo di sottostante in cui il prodotto investe, combinazione se più di un tipo di sottostante", enum=["fondo interno","gestione separata", "combinazione"])
    # underlyng_name: List[str] = Field(NF, description="Nome della/e opzione/i di investimento, sono massimo due.")#@validator("underlyings")





### ENGLISH
class PerformanceScenarios(BaseModel):
    # 1 Year
    stress_return: str = Field(NF, description="1-year stress scenario percentage return")
    # stress_valore: str = Field(NF, description="1-year stress scenario monetary value")
    sfavorevole_return: str = Field(NF, description="Unfavorable scenario percentage return")
    # sfavorevole_valore: str = Field(NF, description="Unfavorable scenario 1-year monetary value")
    moderato_return: str = Field(NF, description="Moderate scenario percentage return")
    moderato_valore: str = Field(NF, description="Moderate scenario 1-year monetary value")
    favorable_return: str = Field(NF, description="Favorable scenario percentage return")
    # favorable_valore: str = Field(NF, description="Favorable scenario 1-year monetary value")

    # RHP (presumably referring to Risk-Adjusted Horizon Period)
    stress_return_rhp: str = Field(NF, description="RHP stress scenario percentage return")
    # stress_valore_rhp: str = Field(NF, description="RHP stress scenario monetary value")
    sfavorevole_return_rhp: str = Field(NF, description="RHP unfavorable scenario percentage return")
    # sfavorevole_valore_rhp: str = Field(NF, description="RHP unfavorable scenario monetary value")
    moderato_return_rhp: str = Field(NF, description="RHP moderate scenario percentage return")
    moderato_valore_rhp: str = Field(NF, description="RHP moderate scenario monetary value")
    favorable_return_rhp: str = Field(NF, description="RHP favorable scenario percentage return")
    favorable_valore_rhp: str = Field(NF, description="RHP favorable scenario monetary value")


class TableRiy(BaseModel):
    # 1 Year
    costo_1: str = Field(NF, description="Cost after 1 year")
    incidenza_costo_1: str = Field(NF, description="Cost incidence in percentage after 1 year")
    # RHP
    costo_thp: str = Field(NF, description="Cost after RHP years")
    incidenza_costo_rhp: str = Field(NF, description="Cost incidence in percentage after 1 year")
    costo_3: str = Field(NF, description="Cost after RHP years")



### ENGLISH
class PerformanceScenarios(BaseModel):
    # 1 Year
    stress_return: str = Field(NF, description="1-year stress scenario percentage return")
    # stress_valore: str = Field(NF, description="1-year stress scenario monetary value")
    sfavorevole_return: str = Field(NF, description="Unfavorable scenario percentage return")
    # sfavorevole_valore: str = Field(NF, description="Unfavorable scenario 1-year monetary value")
    moderato_return: str = Field(NF, description="Moderate scenario percentage return")
    moderato_valore: str = Field(NF, description="Moderate scenario 1-year monetary value")
    favorable_return: str = Field(NF, description="Favorable scenario percentage return")
    # favorable_valore: str = Field(NF, description="Favorable scenario 1-year monetary value")

    # RHP (presumably referring to Risk-Adjusted Horizon Period)
    stress_return_rhp: str = Field(NF, description="RHP stress scenario percentage return")
    # stress_valore_rhp: str = Field(NF, description="RHP stress scenario monetary value")
    sfavorevole_return_rhp: str = Field(NF, description="RHP unfavorable scenario percentage return")
    # sfavorevole_valore_rhp: str = Field(NF, description="RHP unfavorable scenario monetary value")
    moderato_return_rhp: str = Field(NF, description="RHP moderate scenario percentage return")
    moderato_valore_rhp: str = Field(NF, description="RHP moderate scenario monetary value")
    favorable_return_rhp: str = Field(NF, description="RHP favorable scenario percentage return")
    favorable_valore_rhp: str = Field(NF, description="RHP favorable scenario monetary value")


class TableRiy(BaseModel):
    # 1 Year
    costo_1: str = Field(NF, description="Cost after 1 year")
    incidenza_costo_1: str = Field(NF, description="Cost incidence in percentage after 1 year")
    # RHP
    costo_thp: str = Field(NF, description="Cost after RHP years")
    incidenza_costo_rhp: str = Field(NF, description="Cost incidence in percentage after 1 year")
    costo_3: str = Field(NF, description="Cost after RHP years")

    