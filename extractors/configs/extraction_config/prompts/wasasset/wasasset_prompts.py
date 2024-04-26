
general_info = """Dal documento seguente, estrai 
            - Periodo di detenzione raccomandato o per quanto tempo si presuppone di detenere il prodotto(anni), converti in anni se necessario
            - indicatore sintetico di rischio
            - Data di realizzazione del documento (può essere chiamata data di validità del KID)
            DOCUMENTO:
            {context}"""


costi_ingresso_diritti_fissi = """Considerando la seguente tabella, 
Estrai i valori % dopo {rhp} anni ed i diritti fissi (possono essere n/a):
TABELLA: {context}"""

costi_gestione_performance = """Considerando la seguente tabella, 
estrai il valore % dei costi correnti e dei costi di transazione:
TABELLA: {context}"""

