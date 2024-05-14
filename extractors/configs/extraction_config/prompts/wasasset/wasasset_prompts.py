#INFORMAZIONI GENERALI
#ITALIANO
general_info = """Dal documento seguente, estrai 
            - Periodo di detenzione raccomandato o per quanto tempo si presuppone di detenere il prodotto(anni), converti in anni se necessario
            - indicatore sintetico di rischio
            - Data di realizzazione del documento (può essere chiamata data di validità del KID)
            DOCUMENTO:
            {context}"""
#INGLESE
general_info_eng = """From the following document, extract 
            - Recommended holding period or how long the product is assumed to be held (years), convert to years if necessary
            - synthetic risk indicator
            - Date of creation of the document (may be called KID validity date)
            DOCUMENT:
            {context}"""

#COSTI DI INGRESSO E USCITA
#ITALIANO
costi_ingresso_diritti_fissi = """Considerando la seguente tabella, 
Estrai i valori % dopo {rhp} anni ed i diritti fissi (possono essere n/a):
TABELLA: {context}"""
#INGLESE
entry_exit_costs_fixed_rights = """Considering the following table,
Extract the % values after {rhp} years and the fixed rights (can be n/a):
TABLE: {context}"""

#COSTI DI GESTIONE E PERFORMANCE
#ITALIANO
costi_gestione_performance = """Considerando la seguente tabella, 
estrai il valore % dei costi correnti e dei costi di transazione:
TABELLA: {context}"""
#INGLESE
management_costs_performance = """Considering the following table,
extract the % value of current costs and transaction costs:
TABLE: {context}"""

