

rettifichebi_system = "Ciao sei un estrattore di dati. Vorrei estraessi nel seguente modo"

rettifichebi_human = """questo è un documento PDF di esempio:
    ---- ESEMPIO ----
    'Page 1 of 6\nCORPORATE EVENT NOTICE: Modifica delle caratteristiche del sottostante\nBARCLAYS BANK P.L.C.\nSEDE DI NEGOZIAZIONE: Milan\nDISPOSIZIONE: MIL_20240402_07431_TLX\nDATA: 02/04/2024\nMERCATO: EuroTLX\nOGGETTO: RETTIFICA MEDIANTE APPLICAZIONE DEL K FACTOR AVENTE A OGGETTO \nGENERAL ELECTRIC CO / US3696043013 A DECORRERE DAL 03/04/2024\n1. Informazioni inerenti la Corporate action\n: General Electric Co. has announced to spin off GE Vernova as an independent company. Shareholders of General DESCRIZIONE\nElectric Co. shall be entitled to receive for every 4 General Electric Co. shares 1 share of the new company. General Electric Co will \nchange name to GE Aerospace.\n 02/04/2024 DATA DI EFFICACIA:\n2. Dettagli sulla modalità di rettifica\n: EUREX MERCATO DERIVATI\n: 0,797531 FATTORE DI RETTIFICA\n: General Electric Co. will spin off GE Vernova as an independent company. Shareholders shall be CRITERIO DI RETTIFICA\nentitled to receive for every 4 General Electric Co.shares 1 share of the new company. General Electric Co will change name to GE \nAerospace\n: 02/04/2024 DATA DI EFFICACIA EMITTENTE\n 3.Caratteristiche degli strumenti oggetto di rettifica\nISIN CODE XS2366971690 CODICE\nEURONEXTNSCIT2366978 MARKETING\nPRODUCT\nNAMEBonus Cap SEGMENTO DI\nNEGOZIAZIONEEuroTLX - Cert-\nX - Investment \nCertificates \nSegment\nVALORI CORRENTI VALORI POST RETTIFICA\nSTRIKE STRIKE\nPARITY PARITY\nLOWER BARRIER LEVEL LOWER BARRIER LEVEL'"
    le informazioni che voglio estrarre dal testo che ti ho appena passato sono queste: 
    Emittente = Codice = 'US3696043013', 
    Ex_Date = '03/04/2024' (queste due informazioni si trovano nella stringa di 'OGGETTO', il primo è un codice di 12 caratteri, il secondo una data), 
    'Adj_Factor' = 0,797531 (preso subito dopo 'FATTORE DI RETTIFICA:' nella sezione '2. Dettagli sulla modalità di rettifica' )
    --------------------
    Dammi le stesse 3 informazioni dal testo di questo nuovo PDF
    ------ NUOVO DOCUMENTO --------
    {input} 
    ---------
    (ovviamente saranno diverse essendo il testo diverso)"""

