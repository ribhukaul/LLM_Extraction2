#INFORMAZIONI GENERALI
#ITALIANO
general_info = """Dal documento seguente, estrai 
            - Periodo di detenzione raccomandato o per quanto tempo si presuppone di detenere il prodotto(anni), converti in anni se necessario
            - indicatore sintetico di rischio
            - Data di realizzazione del documento (può essere chiamata data di validità del KID)
            - la Classe del fondo, inserita come lettera (o lettere maiuscole) nel nome del prodotto. 
                              esempio di classi sono 'A', 'B', 'C', 'PIR', 'F2', 'D', 'L' etc. Può anche non essere espress
            DOCUMENTO:
            {context}"""
#INGLESE
general_info_eng = """From the following document, extract 
            - Recommended holding period or how long the product is assumed to be held (years), convert to years if necessary
            - synthetic risk indicator
            - Date of creation of the document (may be called KID validity date or the date the KID is accurate as at)
            - the share class, entered as a letter (or uppercase letters) in the product name.
                example of classes are 'A', 'B', 'C', 'PIR', 'F2', 'D', 'L' etc. It may not be expressed
            DOCUMENT:
            {context}"""

# # CLASSE FONDO (FORSE NON SERVE)
# # ITALIANO
# classe_fondo = """Dal documento seguente, estrai la classe del fondo (solitamente è espressa vicino al nome del prodotto come lettera maiusola oppure esplicitamente scritta come
# classe A, classe B, ecc.).
# DOCUMENTO:
# {}"""

# STRATEGIA DI INVESTIMENTO
#ITALIANO
strategia_fondo = """Riporta esattamente parola per parola quanto è scitto nel documento nella sezione "Cosa è questo prodotto?" dove viene 
descritta la strategia di investimento del fondo ovvero gli obiettivi e la politica di investimento. La sezione potrebbe anche chiamarsi Obiettivi e Politica di investimento.
Le informazioni presenti nella sezione desiderata sono "TIPO", "DURATA" "OBIETTIVI" "INVESTITORE AL DETTAGLIO.." "INDICE DI RIFERIMENTO" e "DEPOSITARIO"
------
DOCUEMNTO:
{input}
------
RSPOSTA:
Nel documento la porzione di testo richiesta è:
''' """
# ENGLISH
investment_strategy = """Report exactly word for word what is written in the document in the section "What is this product?" where it is
describes the investment strategy of the fund or the objectives and investment policy. The section could also be called "Objectives and Investment Policy".
There are also info about "TYPE", "TERM" "OBJECTIVE" "INTENDED RTAIL INVESTOR" "BENCHMARK" and "DEPOSITRY"
------
DOCUEMNT:
{input}
------
ANSWER:
In the document the requested portion of text is:
''' """





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

