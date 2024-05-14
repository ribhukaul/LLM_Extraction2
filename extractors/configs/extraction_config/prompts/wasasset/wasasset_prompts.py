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
costi_ingresso_diritti_fissi = """'Estrazione deve dare i soli numeri come risposta, Estrai i valori % ed i diritti fissi in €
TABELLA: {}"""
#INGLESE
entry_exit_costs_fixed_rights = """'The extraction must give only numbers as an answer, Extract the % values and the fixed rights in €
TABLE: {}"""

#COSTI DI GESTIONE E PERFORMANCE
#ITALIANO
costi_gestione_performance = """l'Estrazione deve dare i soli numeri come risposta, Estrai il valore % dei costi correnti e dei costi di transazione e
in € per i costi di performance:
TABELLA: {}"""
#INGLESE
management_costs_performance = """The extraction must give only numbers as an answer, Extract the % value of the current costs and transaction costs and
in € for performance costs:
TABLE: {}"""

