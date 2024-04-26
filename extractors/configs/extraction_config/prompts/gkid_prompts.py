general_info_gkid = """Dal documento seguente, estrai
            - Periodo di detenzione raccomandato 
            - valore indicatore sintetico di rischio minimo o peggiore(da:)(il primo)
            - valore indicatore sintetico di rischio massimo o migliore(a:)(il secondo)
            - Data di realizzazione del documento
            ----
            L'indicatore sintetico di rischio è espresso come numero intero su una scala da 1 a 7.
            l'indicatore sintetico di rischio può essere indicato anche come 'classe di rischio'. 
            Indicalo senza il 'di 7' nel caso in cui sia presente 
            esempio se è '4 di 7' indicalo come '4'
            ----
            DOCUMENTO:
            {context}"""


market_gkid =  """"Dal documento seguente cita ciò che si dice sugli investitori al dettaglio cui si intende commercializzare il prodotto
        ---ritorna solamente la citazione niente introduzione
        ---dovrebbero essere multiple lunghe frasi
        ---ritorna solamente ciò che è riportato nel documento non rifrasare, non puoi aggiungere niente,non voglio introduzione, fornisci la risposta esatta
        ---se non trovi la citazione, la frase da cercare potrebbe essere leggermente diversa
        

            DOCUMENTO:
            {context}"""

