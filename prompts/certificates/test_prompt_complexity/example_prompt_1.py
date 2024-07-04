from models.gemini.gemini_multimodal import get_file




text_1 = "Ciao, sei un estrattore dati. Questo è un documento d'esempio :"

text_2 = """Da quì voglio che vengano estratte le seguenti informazioni che ti passo come esempio per l'estrazione successiva:
        ISIN: CH1336243352
        Emittente (o ideatore): Leonteq Securities AG, Guernsey Branch
        Mercato di quotazione: EuroTLX
        Valuta di Emissione: EUR (La valuta del prezzo di emissione)
        ValoreNominale: 1000 (indipendentemente dalla valuta)
        Data del Fixing Iniziale 08/05/2024
        Data di Emissione 14/05/2024
        Data del Fixing Finale 07/05/2027
        Data di Rimborso 14/05/2027
        Effetto Memoria: Sì (Nel testo è menzionato 'Cedola con effetto memoria')
        Autocallability: Sì (è possibile che in caso in cui il prezzo di chiusura ufficiale di ciascun Sottostante sia superiore al rispettivo Autocall Trigger Level, si verificherà un Rimborso
        Anticipato e il prodotto verrà immediatamente estinto)
        Garanzia: 0% (corrisponde al rimborso minimo garantito come quota percentuale rispetto al ValoreNominale, indipendentemente dalla performance del sottostante e dal verificarsi o meno dell'evento barriera. In questo caso non viene menzionato quindi sarà pari a 0% poichè il capitale è completamente a rischio in caso di evento barriera)
        Livello Barriera: 60.00%
        Livello di Attivazione della Cedola: 60%
        LevaCedolare: None (None quando non menzionata 'Partecipazione' nel testo. Rappresenta la Partecipazione alla performance positiva del sottostante. Se il pagamento a scadenza, in una delle diverse casistiche, dipende da partecipazione * performance, indipendentemente dal CAP, e la partecipazione è maggiore al 100%, estrai 'partecipazione'. Ogni volta che trovi Partecipazione quello sarà sicuramente il campo da estrarre)
        Cap: None (Se il titolo prevede un rimborso superiore all'importo nominale a scadenza, ma con un limite, ad esempio 120% del valore nominale, estrai 120%. In questo caso non è menzionato quindi None)
        Callability: None  (Se l'emittente ha il diritto ma non l'obbligo di rimborsare anticipatamente il prodotto allora sì, Se trovi Softcallable nel testo allora Sì, Se è presente Autocallability allora None, Se non menzionato allora None)
        Sottostanti: Dataframe con Sottostante - ISIN - Livello di Fixing Iniziale, in questo caso 4 righe
        Dataframe con Data di Osservazione della Cedola, Coupon Trigger Level (Livello di Attivazione della Cedola), Data di Pagamento della Cedola Condizionale, Importo della Cedola Condizionale,Importo della cedola Garantita (se presente), Autocall Trigger Level (Livello di Attivazione Autocall), Importo della cedola in caso di Rimborso Anticipato (Pagamento della cedola condizionale).
        (Attenzione che non in tutte le date di osservazione della cedola corrisponde una data di autocall, in questo caso solo dalla seconda data è possibile un richiamo anticipato(autocall), siccome nel primo caso i campi sono valorizzati con un''-', quindi in corrispondenza della prima data gli ultimi due campi andranno valorizzati con None. Attenzione poi che l'ultimo campo non è presente in tutti i documenti, se non dovesse esserci tutta la colonna dovrà essere valorizzata come None. Se presente Callability la colonna Autocall Trigger Level tutte le righe valorizzate None in quanto il rimborso è discrezionale e non dipende dalla performance dei sottostanti)
        TipoBarriera: Europea (Se Barrier level non è valorizzato questo campo sarà None, se invece è valorizzato ci sono due possibilità per la valorizzazione di questo campo, e dipendono dalle modalità di rimborso a scadenza. Se l'evento barriera dipende solamente dal Livello di Fixing Finale allora la barriera sarà europea, se invece la valutazione è nel continuo, solitamente giornaliera tra fixing iniziale e fixing finale, il TipoBarrierasarà Americana)
        
        Secondo documento di esempio:"""

text_3 = """Da quì le informazioni da estrarre sono le seguenti:
        ISIN: CH1336242602
        Emittente (o ideatore): Leonteq Securities AG, Guernsey Branch
        Mercato di quotazione: EuroTLX
        Valuta di Emissione: EUR
        Valore Nominale: 1000
        Data del Fixing Iniziale: 25/04/2024
        Data di Emissione: 02/05/2024
        Data del Fixing Finale: 25/04/2028
        Data di Rimborso: 02/05/2028
        Effetto Memoria: Sì
        Autocallability: Sì
        Garanzia: 0%
        Livello Barriera: 60.00%
        Livello di Attivazione della Cedola: 60%
        Tipo Barriera: Europea
        LevaCedolare: None
        Cap: None
        Callability: None
        Dataframe con sottostanti come nel caso precedente
        Dataframe cedole/autocall come nel caso precedente. (In questo caso il formato appare diverso, ma è riconducibile al primo caso:
        Nelle prime 5 date di osservazione della cedola i campi relativi all'autocall non sono valorizzati, quindi nel dataframe estratto dovranno essere valorizzati come None, e l'ultima colonna in questo caso non è presente, quindi tutta la colonna andrà valorizzata come None).

        Fammi vedere che hai capito, estrai questi stessi campi dal seguenti documento:"""

# Prompt edited by Jacopo
text_4 = """dal documento, trovare le seguenti informazioni, tutte le informazioni sono presenti nel documento: 
                -Data di creazione del documento contenente le informazioni
                -ISIN
                -periodo di detenzione raccomandato in anni
                -livello dell’indicatore sintetico di rischio
                -nella sezione SCENARI DI PERFORMANCE, cerca il rendimento dello scenario moderato, restituisci il rendimento per il caso di uscita dopo 1 anno e per l'uscita dopo il periodo di detenzione raccomandato
                -l'impatto dei costi nel tempo (dopo 1 anno e dopo 1 anno e al periodo di detenzione raccomandato)

        """
# Prompt edited by Ribhu to improve extraction
text_5 = """dal documento, trovare le seguenti informazioni, tutte le informazioni sono presenti nel documento: 
                -Data di creazione del documento contenente le informazioni
                -ISIN
                -indicatore di rischio sintetico ovvero il livello di rischio
                -periodo di detenzione raccomandato in anni
                -Estrai le percentuali per ciascuno scenario nella tabella intitolata "Scenari di prestazioni", inclusi i valori per entrambi "Se uscita dopo 1 anno" rispetto a "Se uscita dopo il periodo di detenzione proposto". Tieni presente che "Minimo" non ha un valore percentuale
                -l'impatto dei costi nel tempo (dopo 1 anno e dopo 1 anno e al periodo di detenzione raccomandato)

        """

# -Scenari di prformance moderata Rendimento medio dopo il periodo di detenzione consigliato  (this works fine in text 5)
#{ Estrai le percentuali per ciascuno scenario nella tabella intitolata "Scenari di performance", inclusi i valori sia per 
# "Se disinvesti dopo 1 anno" che per "Se disinvestisci dopo il periodo di detenzione raccomandato". 
# Tieni presente che "Minimo" non ha un valore percentuale} this works fine but fails for docs with 3 columns


text_6 = """ Dal documento, trovare le seguenti informazioni:
        - Quante pagine ha il documento?
        -questo documento è di quale azienda?
        -quale pagina fornisce informazioni sulle commissioni di gestione annuali addebitate per i fondi esterni e interni?
        -Quali sono i tipi di fondi che un cliente può scegliere di investire?
        -Elencare tutti i fondi interni, se presenti, ed etichettarli come = fondi interni, estrarre e scrivere accanto a ciascun nome estratto la relativa classe di attività
        -elencare tutti i fondi esterni, se presenti, ed etichettarli = fondi esterni e scrivere accanto a ciascun nome estratto la relativa classe di attività
        -elencare tutti i fondi gestiti separatamente, se presenti, etichettandoli come = gestiti separatamente e scrivere accanto a ciascun nome estratto la loro classe di attività
        """


# This one extracts the names of the funds perfectly
text_6B = """ From the document, find the following information:
 - How many pages does the document have?
 -this document is from which company?
 -which page provides information on annual management fees charged for external and internal funds?
 -What are the types of funds a client can choose to invest?
 -List all internal funds, if any, and label them as = internal funds, extract and write the relevant asset class next to each extracted name
 - list all external funds, if any, and label them = external funds and write the relevant asset class next to each extracted name
 -list all separately managed funds, if any, labeling them as = separately managed and write their asset class next to each extracted name
 """



text_6A = """ From the document, find the following information:
        - How many pages does the document have?
        -this document is from which company?
        -what is seperate management? what is the name given to it in the document?
        -which page provides information on annual management fees charged for external and internal funds?
        -What are the types of funds a client can choose to invest?
        -from the section Costi gravanti sui Fondi esterni ed interni, List all internal funds, if any, and label them as = internal funds, extract and write the relevant asset class and annual management fee charged next to each extracted name
        - from the section Costi non gravanti direttamente sul Contraente: list all external funds, if any, and label them = external funds and write the relevant asset class and annual management fee charged next to each extracted name
         -from the section Costi gravanti sulla Gestione Separata, list all separate management funds (known as Gestione Separata), if any, labeling them as = separately managed and write their asset class and annual management fee charged next to each extracted name
        """

text_6C = """
                from the document,
                - extract all the names of internal funds or fondi interni or denominazione fondo
                - extract all the names of external funds or fondi esterni, or "denominazione fondo
                - extract all the names of the separate management funds (known as Gestione Separata) or "denominazione fondo
                - if none of the prompts find anything search for "denominazione or denominazione fondo and return/extract the funds name given
        """
text_6c_1 = """Di seguito è presentato un documento riguardante un prodotto assicurtativo con la lista di tutti i sottostanti in cui il prodotto può essere investito.
Estrai in maniera strutturata tutti i fondi interni, fondi esterni e gestioni separate in cui il prodotto può investire fornendo un dizionartio come ouput, cpn il nome del fondo come chiave e la tipologia di fondo
(fondo interno, fodno esterno o gestione separata) come chiave. Di seguito anche un esempio di ouput
-----
ESEMPIO
{
'FONDO 1 NOME' : 'fondo interno',
'FONDO 2 NAMO' : 'fondo esterno',
'FODNO 3 NAME' : 'gestione separata'.
etc
}
------
DOCUMENTO

"""


text_6c_2 = """ Di seguito è riportato un documento relativo ad un prodotto assicurativo con l'elenco di tutti gli asset sottostanti in cui è possibile investire il prodotto.
Estrarre in modo strutturato tutti i fondi interni, i fondi esterni e le gestioni separate in cui il prodotto può investire fornendo in output un dizionario, con come chiave il nome del fondo e la tipologia di fondo (fondo interno, fondo esterno o separato gestione) come valore . I nomi dei fondi POSSONO ESSERE TROVATI NELLA colonna con l'intestazione "denominazione fondo" o "Denominazione". Di seguito è riportato anche un esempio di output:
-----
ESEMPIO
{
'BOTTOM 1 NAME': 'fondo interno',
'BOTTOM 2 NAME': 'fondo esterno',
'NOME FONDO 3': 'gestione separata',
eccetera.
}
------
DOCUMENTO

"""


text_6E = """
                Task: Extract all names of funds listed in the document.


                        From the document:
                        Specifics:
                        Extract include names of both internal funds (also known as fondi interni) and external funds (also known as fondi esterni).
                        Funds may be listed along with codes, categories, and SFDR classifications.
                        Extract all the names of the separate management funds (known as Gestione Separata), if available in the document.
                        Each fund name may be preceded by an ISIN code and followed by category information.
                        If nothing is found, then check if the funds names are in the columns with col names  denominazione fondo or denominazione.
                        Expected Output:

                        Provide a list of all fund names extracted from the document.
                        Ensure no other details (like codes or categories) are included in the names list.
                        Additional Notes:

                        If a fund name spans across multiple lines, ensure the complete name is captured as a single entry.
                        Check for and correct any potential OCR misreads or typos in fund names.
                        Make sure to extract all the names from the file, regardless of how many they are.


"""

# -list all separate management funds (known as Gestione Separata), if any, labeling them as = separately managed and write their asset class and annual management fee charged next to each extracted name
        
text_7 = """ Dal documento, trovare le seguenti informazioni:
                -quale pagina fornisce informazioni sulle commissioni di gestione annuali addebitate per i fondi esterni e interni?
                
                -qual è la commissione di gestione annua addebitata per il fondo interno Vol cap 8%, puoi trovarla nella sezione Costi sostenuti da fondi esterni e interni
        """
                

text_7A = """   
                what is seperate management? what is the name given to it in the document?
                
                list all separate management funds (known as Gestione Separata), if any, labeling them as = separately managed and write their asset class and annual management fee charged next to each extracted name

        """

text_7B = """
                which page number has the information on annual management fees charged for external and internal funds?
                from that page, extract all the annual management fees for 
                        - internal funds
                        - external funds
                        - separately managed funds 
        """

# -quali sono le informazioni fornite alla pagina numero 17, qual è il punto chiave che la differenzia dal resto del documento? (for text_7)


text_8 = """
                       what is the total population of Cisterna di Latina?
                       Which is greater for Arezzo, male or female population? There may be more than one location (row) with this name, return answer for each
                       Quali sono le città le più popolose della provincia di Torino?, descending order
"""


text_9 = """
        there may be some error in the json_str, correct all the errors so that we can use it for extractio
        return the correct json

"""

prompt_example_1 = [text_1]
prompt_example_2 = [text_4]
prompt_example_3 = [text_5]
prompt_example_4 = [text_6c_2]
#prompt_example_5 = [text_9]
prompt_example_6 = [text_7B]
prompt_example_7 = [text_8]





