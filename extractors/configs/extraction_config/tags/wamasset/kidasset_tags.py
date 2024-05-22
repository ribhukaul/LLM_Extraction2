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
# Not used for the time being
# manufact =["21 Invest","3i Infrastructure",
# "8a+","Aberdeen Standard","ABN Amro","Acadian","AcomeA","Adaxia Capital Partners","Adepa AM","Advam Partners",
#            "Advanced Capital","Aedes BPM Real Estate","Aegon Asset Management","Aew Europe","AF Mezzanine","AG Capital","Agora","Aksìa Group","Alantra PE",
#            "Albemarle","Albermarle","Alcedo","Alcentra","Aletti Gestielle","Algebris Investments","Alger","Alha Private Equity","Alisei","Alken","Alkimis",
#            "Alliance Bernstein","Allianz GI","Allspring","AlpenBank","Alpi Fondi","Alta CM","Alternitave Capital Partners","Alto Partners","Amber Capital ",
#            "Ambienta","Amundi","Anacap Financial","Anavon Capital","Anaxis","Ancala Partners LLP","Anima","Anima Alternative","Anthilia Capital Partners",
#            "Antin Infrastructure Partner","Antirion","Apax Partners","Apollo Global Management","AQR","Aquila  Group","Arc AM","Arca Fondi","Arcadia","Arcano",
#            "Archer Daniels Asset Management","Arcus Investment Partners","Ardian","Area Group","ARK Invest","Armonìa","Artisan Partners",
#            "Ashmore Investment Management","Aspect Capital","Assietta PE","Aviva Investors","Avm Associati","Axa IM","Axiom","Azimut Capital Management",
#            "Baillie Gifford","Bain Capital","Bamboo Capital Partners","Banca Aletti","Banca Finnat","Banca Generali","Banca Passadore & C.","Banca Profilo",
#            "Bancoposta Fondi","Banor","Banque de Luxembourg","Bantleon", "Barclays Capital","Barings","Bayes Investments","BCC Risparmio&Previdenza",
#            "Beechbrook","Bellevue AM","BennBridge","Bestinver","Black Toro Capital","BlackRock","BlackStone","Blue","BlueBay","BlueOrchard Finance",
#            "BMO Global AM","BNP Paribas AM","BNP Paribas REIM","BNY Mellon","Boston Partners","BPER Sicav","Brandes Investment","Brandywine Global",
#            "Breakwater Management","Bridge Capital","Bridge Investment Group Partners LLC","Brigade Capital","Broadlight CM","Brookfield","BWG",
#            "CA Indosuez AM","Candriam","Capital Four Management","Capital Group","Capzanine","Carlyle","Carmignac","CarVal Investors","Casa4Funds",
#            "Cassa Centrale Banca","Castello","CBRE Investment Management","CentroBanca Sviluppo Impresa","Ceresio Group","Charterhouse Capital Partners",
#            "Chenavari Investment Managers","Chorus Capital","CIFC AM","Cinven","Circuitus Capital LLLP","Citibank","Clearbridge Investments",
#            "Clearvue Partners","Cliff","Cobas AM","Coima","Columbia Threadneedle","Comgest","Commonfund","Comoi","Compass AM","Connect Ventures",
#            "Consultinvest","Controlfida","Corbin Capital Partners","Cordiant Capital","C-Quadrat","Credem Private Equity","Credit Suisse AM",
#            "Credit Value Partners","Crescent Capital Group","Cromwell Property Group","Cross Ocean Partners","Cubera PE","CVC","Daiwa AM","DeA Capital Alternative","DeA Capital Real Estate","Decalia SIM","Degroof Petercam","DELFF","Diaman Sicav","DIF","DJE Investment","DNCA Invest","Domain Capital Group","Dorval","Dpixel Venture Capital","DRC Capital","Duet EMIM","DWM AM","DWS","Eagle CM","EarlyBird","East Capital AM","ECM AM","Ecosystem Integrity Fund","ECPI AM","ECRA","Edgewood Management","Edmond de Rothschild","EFG AM","EI Sturdza","Eiser Infrastructure Partner","Eleva Capital","Ellipsis","Emerald Management","Emisys Capital","EMZ Partners","Endeka","EnTrust Global","Epsilon","EQT","Equinox Investments","Equita Capital","Equitix","Ersel AM","Est Capital (non più attiva)","Ethenea","Etica","Euregio Plus","Eureka Venture","Eurizon Capital","Eurizon Capital Real Asset","Euromobiliare","Europa Capital Partners","Europa Risorse","European and Global Investments",
#            "European Investment Fund","Evli","Exane","F2i","Fabrica Immobiliare","Fasanara Capital","Federated Hermes","Fidelity International",
#            "Fideuram AM","Financiere de l'Echiquier","Finanziaria Internazionale","Fineco AM","Fireside Financial","First State Investments Limited",
#            "First Trust","Fisher Investments","Fondaco","Fondo Italiano d'Investimento","Fondo Italiano per l'Efficienza Energetica","Foresight Group",
#            "FourWinds Capital Management","Franklin Templeton","FSI","Fundsmith","FvS Invest","Gam","GAMCO","GaveKal Capital","Gemini CM","GemWay",
#            "Generali Global Infrastructure","Generali Insurance AM","Generali Investments","Generali Real Estate","Global X Management","Glouston Capital Partners"
#            ,"Goldman Sachs AM","Green Arrow Capital","GreenOak Real Estate","Greenspring","Groupama AM","Groupe Financier de Gestion",
#            "GSA Global Student Accomodation","GSO Capital Partners","Guinness AM","H2O","Hamilton Lane","HANetf","Harbert Management Corporation",
#            "HarbourVest Partners","Hastings","Hauck & Aufhauser","Hayfin","Hedge Invest","Highbridge PS","Highland CM","HighPost Capital",
#            "Hines Italia S.p.A./COIMA","Hope SICAF","Horizon Capital Asset Management","HSBC Global AM","Iccrea Banca","iCON Infrastructure LLP",
#            "Idinvest Partners","IM Global Partners","Impact Bridge Asset Management","Impact SIM","Impax","InBetween","Incanto","Indigo Capital SAS",
#            "Infusive AM","ING","Innocap","Insight Investment","Intermede","Intermediate Capital Group","Intermonte","Invesco","InvesteQ Capital",
#            "InvestiRE","Investlinx","ITALGLOBAL PARTNERS","J O Hambro CM","Janus Henderson","JCM Capital Management ","Jennison Associates","JLL",
#            "JP Morgan AM","JSS","Julius Baer","Jupiter","Kairos Partners","KBI","Kempen","Kennedy Lewis Capital","Kervis","KGAL GMBH & Co. KG","KKR",
#            "Kryalos","La Francaise","Lazard","LBO France","Legg Mason","Lemanik","LendInvest","LFIS Capital","LGIM","LGT European Capital Partners",
#            "Lion River","Lionstone Investments","Liontrust","Lombard Odier","Loomis Sayles","Lord Abbett","LUCE Capital","Luxcara","Lyxor AM","M&G Investments",
#            "Macquarie Infrastructure and Real Assets","Main Capital","MainFirst","Man Group","Mandarin Capital Partners","Mandarine Gestion","March AM",
#            "Marguerite","Marshall Wace","Martin Currie","Maybank AM","Medalist Partners","Mediobanca","Mediolanum AM","Mediolanum Gestione Fondi",
#            "Merian Global Investors","Merieux Equity Partners","Metropolis Capital","MFM Investment","MFS Meridian","Micro Kapital","MicroVest Capital Management",
#            "Mirabaud","Mirae AM","Mirova","Mittel","Mondrian","Montpensier","Montreux Capital","Morgan Stanley IM","MP Venture","Muzinich & Co","Namira","Natixis",
#            "Negentropy Capital Partners","Neuberger Berman","Neva","New Forests Asset management","Newcore Capital Management",
#            "Newton IM","Next Energy Capital","Nextam","NIAM","Niche AM","Nine Capital Partners","Ninety One","NN IP","Nomura AM",
#            "Nord Est AM","Nordea AM","Northwood Investors",'Nova IM','NREP','NS Partners','NTR Asset Management Europe DAC','Numen Capital','Numeria',
#            "O1","Oaktree Capital Management","Obligo","October Factory","Oddo","OFI","Open CP","Optima SIM","Optimum Asset Management","Orefici","Orizzonte","Ossiam",
#            "Ostrum","P101","Palladio Finanziaria","Pantheon","Partners Group","Patrimonium","Patrizia","Payden","Pemberton Asset Management","Pensplan",
#            "Performance Equity Management","Permira Debt Managers","PGIM","Pharus","Pi Labs","Pictet AM","Pimco","PineBridge Investments","Plenisfer Investments",
#            "PM & Partners","Polar Capital","Polen Capital","Polen Capital","Polis","Portfolio Advisors","Prelios","Principal Real Estate Europe","Principia IM",
#            "Private Equity Partners","Progressio","Prologis Inc.","Pzena IM","Quaestio Capital","Quantitative Management Associates","Quercus Asset Selection",
#            "Quinta Capital","Quoniam","Raiffeisen CM","RAM","Rantum Capital","Realterm","REAM","Resona AM","Resource Management Service","ResponsAbility Investments",
#            "Riello Investimenti","Rigsave Capital","RiverRock LLP","Rize ETF","Robeco","Rockefeller","Rocket Internet Capital Partners","Rothschild & Co.",
#            "RoundShield Partners","Rubrics AM","Russell Investments","Ruvercap","RWC Partners","Sagitta","Sarona Asset Management","Sator Immobiliare",
#            "Savills Investment Management","Schroders","SCOR Investment Partners","Seamax LLC","Searchligth Capital","SEB AM","Sectoral Asset Management",
#            "Seilern IM","Selectra Group","Sella","Sella Gestioni","Sella Venture Partners","SerendipEquity","Serenissima","Sibilla CM","Smart Lenders AM",
#            "Solar Investment Group","Soprarno","Sorgente","Sound Bioventures","Springrowth AM","Sprott AM","Spur Capital partners","Stafford Capital Partners",
#            "State Street Global Advisors","Stonepeak Infrastructure Partners","Structured Invest","Sumus AM","Sustainable Growth Advisers",
#            "Swiss & Global Asset Management","Swiss Life","Swisscanto","Sycomore","Symphonia","Synergo","T. Rowe Price","Tabula IM","Tages","TCW",
#            "TD Asset Management","TeamSystem Capital@Work","Tellworth Investments","Tenax Capital","Tendercapital","Terra Nova AM","Three Hills Capital Partners",
#            "Three Rock CM","Threestone Capital","TIIC Management","Tikehau Capital","Timberland Investment","Torre","Trea AM","Trilantic Capital Partners",
#            "Triodos IM","Trium","Trocadero Capital Partners","Trusteam","TwentyFour AM","Twin Haven LLC","Tyndaris LLP","Tyrus Capital","UBP AM","UBS AM",
#            "Unigestion","Unigrains Développement","Union Investment","Universal Investment","Vaneck","Vanguard","Vantage","Vela Imprese ","Ver Capital","Vertis",
#            "Vickers Venture Partners","Victory Park Capital","Vontobel AM","Voya IM","Walter Scott & Partners","Waystone","Wellington","Western AM",
#            "WisdomTree","Wise","Yarpa Investimenti","Zadig AM","Zenit","Zephir Capital Partners","Zest AM","Zurich Invest"]
class Naming(BaseModel):
    nome_fondo: str = Field(..., description="nome del fondo o del prodotto considerando anche classe eucits e share class (se presenti) e se specificato acc o dist")
    manufacturer: str = Field(..., description="nome del manufacturer (gestore del fondo)")
    #enum=manufact)
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

