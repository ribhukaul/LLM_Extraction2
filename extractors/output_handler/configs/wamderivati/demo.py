# typeof
INT = "Integer"
FLOAT = "Float"
STRING = "String"
DATE= "Date"
BOOL = "Boolean"
#model of
PERCENT = "%"
EURO = "€"
YEARS = "anni"
CAPS = "CAPS"

TRUE = "true"
FALSE = "false"
NA = "N/A"

PERCENT_RANGE = []
ISIN_RANGE = []
DATE_RANGE = []

SRI_RANGE = []
NO_RANGE = []


demo = {
    "fields": {
        "isin": {
            "field_name": "cod_100isin",
            "renaming": "Isin",
            "allow_null": FALSE,
            "type_of": STRING,
            "model_of": NA,
            "decimals_of": NA,
            "range_of": NO_RANGE
        },
        "descrizione": {
            "field_name": "cod_101descrizione",
            "renaming": "Descrizione",
            "allow_null": FALSE,
            "type_of": STRING,
            "model_of": NA,
            "decimals_of": NA,
            "range_of": NO_RANGE
        },
        "tipotitolo": {
            "field_name": "cod_102tipotitolo",
            "renaming": "TipoTitolo",
            "allow_null": FALSE,
            "type_of": STRING,
            "model_of": NA,
            "decimals_of": NA,
            "range_of": NO_RANGE
        },
        "emittente": {
            "field_name": "cod_103emittente",
            "renaming": "Emittente",
            "allow_null": FALSE,
            "type_of": STRING,
            "model_of": NA,
            "decimals_of": NA,
            "range_of": NO_RANGE
        },
        # #"idemittente": {
        #     "field_name": "cod_idemittente",
        #     "renaming": "IdEmittente",
        #     "allow_null": FALSE,
        #     "type_of": STRING,
        #     "model_of": NA,
        #     "decimals_of": NA,
        #     "range_of": NO_RANGE
        # },
        "divisa": {
            "field_name": "cod_104divisa",
            "renaming": "Divisa",
            "allow_null": FALSE,
            "type_of": STRING,
            "model_of": NA,
            "decimals_of": NA,
            "range_of": NO_RANGE
        },
        "mercato": {
            "field_name": "cod_105mercato",
            "renaming": "Mercato",
            "allow_null": FALSE,
            "type_of": STRING,
            "model_of": NA,
            "decimals_of": NA,
            "range_of": NO_RANGE
        },
        # #"quotato": {
        #     "field_name": "cod_quotato",
        #     "renaming": "Quotato",
        #     "allow_null": FALSE,
        #     "type_of": STRING,
        #     "model_of": NA,
        #     "decimals_of": NA,
        #     "range_of": NO_RANGE
        # },
        "valorenominale": {
            "field_name": "cod_106valorenominale",
            "renaming": "ValoreNominale",
            "allow_null": FALSE,
            "type_of": STRING,
            "model_of": NA,
            "decimals_of": NA,
            "range_of": NO_RANGE
        },
        "garanziaminimaperc": {
            "field_name": "cod_107garanziaminimaperc",
            "renaming": "GaranziaMinimaPerc",
            "allow_null": FALSE,
            "type_of": STRING,
            "model_of": NA,
            "decimals_of": NA,
            "range_of": NO_RANGE
        },
        # #"garantito": {
        #     "field_name": "cod_garantito",
        #     "renaming": "Garantito",
        #     "allow_null": FALSE,
        #     "type_of": STRING,
        #     "model_of": NA,
        #     "decimals_of": NA,
        #     "range_of": NO_RANGE
        # },
        "protezionecondizionataperc": {
            "field_name": "cod_108protezionecondizionataperc",
            "renaming": "ProtezioneCondizionataPerc",
            "allow_null": FALSE,
            "type_of": STRING,
            "model_of": NA,
            "decimals_of": NA,
            "range_of": NO_RANGE
        },
        "barrieraprotezioneperc": {
            "field_name": "cod_109barrieraprotezioneperc",
            "renaming": "BarrieraProtezionePerc",
            "allow_null": FALSE,
            "type_of": STRING,
            "model_of": NA,
            "decimals_of": NA,
            "range_of": NO_RANGE
        },
        "tipobarrieraprotezione": {
            "field_name": "cod_110tipobarrieraprotezione",
            "renaming": "TipoBarrieraProtezione",
            "allow_null": FALSE,
            "type_of": STRING,
            "model_of": NA,
            "decimals_of": NA,
            "range_of": NO_RANGE
        },
        # #"levacapitale": {
        #     "field_name": "cod_levacapitale",
        #     "renaming": "LevaCapitale",
        #     "allow_null": FALSE,
        #     "type_of": STRING,
        #     "model_of": NA,
        #     "decimals_of": NA,
        #     "range_of": NO_RANGE
        # },
        # #"levaperccapitale": {
        #     "field_name": "cod_levaperccapitale",
        #     "renaming": "LevaPercCapitale",
        #     "allow_null": FALSE,
        #     "type_of": STRING,
        #     "model_of": NA,
        #     "decimals_of": NA,
        #     "range_of": NO_RANGE
        # },
        # #"levacedolare": {
        #     "field_name": "cod_levacedolare",
        #     "renaming": "LevaCedolare",
        #     "allow_null": FALSE,
        #     "type_of": STRING,
        #     "model_of": NA,
        #     "decimals_of": NA,
        #     "range_of": NO_RANGE
        # },
        # #"levaperccedolare": {
        #     "field_name": "cod_levaperccedolare",
        #     "renaming": "LevaPercCedolare",
        #     "allow_null": FALSE,
        #     "type_of": STRING,
        #     "model_of": NA,
        #     "decimals_of": NA,
        #     "range_of": NO_RANGE
        # },
        "cedolagarantitaperc": {
            "field_name": "cod_111cedolagarantitaperc",
            "renaming": "CedolaGarantitaPerc",
            "allow_null": FALSE,
            "type_of": STRING,
            "model_of": NA,
            "decimals_of": NA,
            "range_of": NO_RANGE
        },
        "cedolacondizionataperc": {
            "field_name": "cod_112cedolacondizionataperc",
            "renaming": "CedolaCondizionata",  #abbiamo cambiato il nome da CedolaCondizionataPerc a CedolaCondizionata
            "allow_null": FALSE,
            "type_of": STRING,
            "model_of": NA,
            "decimals_of": NA,
            "range_of": NO_RANGE
        },
        "barrieracedolacondizionataperc": {
            "field_name": "cod_113barrieracedolacondizionataperc",
            "renaming": "BarrieraCedolaCondizionataPerc",
            "allow_null": FALSE,
            "type_of": STRING,
            "model_of": NA,
            "decimals_of": NA,
            "range_of": NO_RANGE
        },
        "memorycoupon": {
            "field_name": "cod_114memorycoupon",
            "renaming": "MemoryCoupon",
            "allow_null": FALSE,
            "type_of": STRING,
            "model_of": NA,
            "decimals_of": NA,
            "range_of": NO_RANGE
        },
        # #"cedolacapperc": {
        #     "field_name": "cod_cedolacapperc",
        #     "renaming": "CedolaCapPerc",
        #     "allow_null": FALSE,
        #     "type_of": STRING,
        #     "model_of": NA,
        #     "decimals_of": NA,
        #     "range_of": NO_RANGE
        # },
        # #"codicesottostante": {
        #     "field_name": "cod_codicesottostante",
        #     "renaming": "CodiceSottostante",
        #     "allow_null": FALSE,
        #     "type_of": STRING,
        #     "model_of": NA,
        #     "decimals_of": NA,
        #     "range_of": NO_RANGE
        # },
        # #"nomesottostante": {
        #     "field_name": "cod_nomesottostante",
        #     "renaming": "NomeSottostante",
        #     "allow_null": FALSE,
        #     "type_of": STRING,
        #     "model_of": NA,
        #     "decimals_of": NA,
        #     "range_of": NO_RANGE
        # },
        # #"divisasottostante": {
        #     "field_name": "cod_divisasottostante",
        #     "renaming": "DivisaSottostante",
        #     "allow_null": FALSE,
        #     "type_of": STRING,
        #     "model_of": NA,
        #     "decimals_of": NA,
        #     "range_of": NO_RANGE
        # },
        # #"tiposottostante": {
        #     "field_name": "cod_tiposottostante",
        #     "renaming": "TipoSottostante",
        #     "allow_null": FALSE,
        #     "type_of": STRING,
        #     "model_of": NA,
        #     "decimals_of": NA,
        #     "range_of": NO_RANGE
        # },
        # #"sottostantebasket": {
        #     "field_name": "cod_sottostantebasket",
        #     "renaming": "SottostanteBasket",
        #     "allow_null": FALSE,
        #     "type_of": STRING,
        #     "model_of": NA,
        #     "decimals_of": NA,
        #     "range_of": NO_RANGE
        # },
        # #"numerosottostanti": {
        #     "field_name": "cod_numerosottostanti",
        #     "renaming": "NumeroSottostanti",
        #     "allow_null": FALSE,
        #     "type_of": STRING,
        #     "model_of": NA,
        #     "decimals_of": NA,
        #     "range_of": NO_RANGE
        # },
        # #"sottostante_1(anagraficasottostanti)": {
        #     "field_name": "cod_sottostante_1(anagraficasottostanti)",
        #     "renaming": "Sottostante_1(AnagraficaSottostanti)",
        #     "allow_null": FALSE,
        #     "type_of": STRING,
        #     "model_of": NA,
        #     "decimals_of": NA,
        #     "range_of": NO_RANGE
        # },
        # #"sottostante_2(anagraficasottostanti)": {
        #     "field_name": "cod_sottostante_2(anagraficasottostanti)",
        #     "renaming": "Sottostante_2(AnagraficaSottostanti)",
        #     "allow_null": FALSE,
        #     "type_of": STRING,
        #     "model_of": NA,
        #     "decimals_of": NA,
        #     "range_of": NO_RANGE
        # },
        # #"sottostante_3(anagraficasottostanti)": {
        #     "field_name": "cod_sottostante_3(anagraficasottostanti)",
        #     "renaming": "Sottostante_3(AnagraficaSottostanti)",
        #     "allow_null": FALSE,
        #     "type_of": STRING,
        #     "model_of": NA,
        #     "decimals_of": NA,
        #     "range_of": NO_RANGE
        # },
        # #"sottostante_4(anagraficasottostanti)": {
        #     "field_name": "cod_sottostante_4(anagraficasottostanti)",
        #     "renaming": "Sottostante_4(AnagraficaSottostanti)",
        #     "allow_null": FALSE,
        #     "type_of": STRING,
        #     "model_of": NA,
        #     "decimals_of": NA,
        #     "range_of": NO_RANGE
        # },
        # #"sottostante_5(anagraficasottostanti)": {
        #     "field_name": "cod_sottostante_5(anagraficasottostanti)",
        #     "renaming": "Sottostante_5(AnagraficaSottostanti)",
        #     "allow_null": FALSE,
        #     "type_of": STRING,
        #     "model_of": NA,
        #     "decimals_of": NA,
        #     "range_of": NO_RANGE
        # },
        # #"tipocalcolobasketperf": {
        #     "field_name": "cod_tipocalcolobasketperf",
        #     "renaming": "TipoCalcoloBasketPerf",
        #     "allow_null": FALSE,
        #     "type_of": STRING,
        #     "model_of": NA,
        #     "decimals_of": NA,
        #     "range_of": NO_RANGE
        # },
        # #"sottostanteopaco": {
        #     "field_name": "cod_sottostanteopaco",
        #     "renaming": "SottostanteOpaco",
        #     "allow_null": FALSE,
        #     "type_of": STRING,
        #     "model_of": NA,
        #     "decimals_of": NA,
        #     "range_of": NO_RANGE
        # },
        "posizionelongshortsusottostante": {
            "field_name": "cod_115posizionelongshortsusottostante",
            "renaming": "PosizioneLongShortSuSottostante",
            "allow_null": FALSE,
            "type_of": STRING,
            "model_of": NA,
            "decimals_of": NA,
            "range_of": NO_RANGE
        },
        "strategialongshort": {
            "field_name": "cod_116strategialongshort",
            "renaming": "StrategiaLongShort",
            "allow_null": FALSE,
            "type_of": STRING,
            "model_of": NA,
            "decimals_of": NA,
            "range_of": NO_RANGE
        },
        # #"isquanto": {
        #     "field_name": "cod_isquanto",
        #     "renaming": "IsQuanto",
        #     "allow_null": FALSE,
        #     "type_of": STRING,
        #     "model_of": NA,
        #     "decimals_of": NA,
        #     "range_of": NO_RANGE
        # },
        # #"pathdependent": {
        #     "field_name": "cod_pathdependent",
        #     "renaming": "PathDependent",
        #     "allow_null": FALSE,
        #     "type_of": STRING,
        #     "model_of": NA,
        #     "decimals_of": NA,
        #     "range_of": NO_RANGE
        # },
        "tiporilevazione": {
            "field_name": "cod_117tiporilevazione",
            "renaming": "TipoRilevazione",
            "allow_null": FALSE,
            "type_of": STRING,
            "model_of": NA,
            "decimals_of": NA,
            "range_of": NO_RANGE
        },
        # #"finecollocamento": {
        #     "field_name": "cod_finecollocamento",
        #     "renaming": "FineCollocamento",
        #     "allow_null": FALSE,
        #     "type_of": STRING,
        #     "model_of": NA,
        #     "decimals_of": NA,
        #     "range_of": NO_RANGE
        # },
        "dataemissione": {
            "field_name": "cod_118dataemissione",
            "renaming": "DataEmissione",
            "allow_null": FALSE,
            "type_of": STRING,
            "model_of": NA,
            "decimals_of": NA,
            "range_of": NO_RANGE
        },
        "datascadenza": {
            "field_name": "cod_119datascadenza",
            "renaming": "DataScadenza",
            "allow_null": FALSE,
            "type_of": STRING,
            "model_of": NA,
            "decimals_of": NA,
            "range_of": NO_RANGE
        },
        "automaticearlyredemption": {
            "field_name": "cod_120automaticearlyredemption",
            "renaming": "AutomaticEarlyRedemption",
            "allow_null": FALSE,
            "type_of": STRING,
            "model_of": NA,
            "decimals_of": NA,
            "range_of": NO_RANGE
        },
        # #"tipopayoff": {
        #     "field_name": "cod_tipopayoff",
        #     "renaming": "TipoPayoff",
        #     "allow_null": FALSE,
        #     "type_of": STRING,
        #     "model_of": NA,
        #     "decimals_of": NA,
        #     "range_of": NO_RANGE
        # },
        # #"datainserimento": {
        #     "field_name": "cod_datainserimento",
        #     "renaming": "DataInserimento",
        #     "allow_null": FALSE,
        #     "type_of": STRING,
        #     "model_of": NA,
        #     "decimals_of": NA,
        #     "range_of": NO_RANGE
        # },
        # #"classeeusipa": {
        #     "field_name": "cod_classeeusipa",
        #     "renaming": "ClasseEUSIPA",
        #     "allow_null": FALSE,
        #     "type_of": STRING,
        #     "model_of": NA,
        #     "decimals_of": NA,
        #     "range_of": NO_RANGE
        # },
        # #"tipo_idemittente": {
        #     "field_name": "cod_tipo_idemittente",
        #     "renaming": "Tipo_IdEmittente",
        #     "allow_null": FALSE,
        #     "type_of": STRING,
        #     "model_of": NA,
        #     "decimals_of": NA,
        #     "range_of": NO_RANGE
        # },
        "bailin": {
            "field_name": "cod_121bailin",
            "renaming": "BailIn",
            "allow_null": FALSE,
            "type_of": STRING,
            "model_of": NA,
            "decimals_of": NA,
            "range_of": NO_RANGE
        },
        # #"rankingbailin": {
        #     "field_name": "cod_rankingbailin",
        #     "renaming": "RankingBailIn",
        #     "allow_null": FALSE,
        #     "type_of": STRING,
        #     "model_of": NA,
        #     "decimals_of": NA,
        #     "range_of": NO_RANGE
        # },
        # #"strike": {
        #     "field_name": "cod_strike",
        #     "renaming": "Strike",
        #     "allow_null": FALSE,
        #     "type_of": STRING,
        #     "model_of": NA,
        #     "decimals_of": NA,
        #     "range_of": NO_RANGE
        # },
        # #"cedolafloorperc": {
        #     "field_name": "cod_cedolafloorperc",
        #     "renaming": "CedolaFloorPerc",
        #     "allow_null": FALSE,
        #     "type_of": STRING,
        #     "model_of": NA,
        #     "decimals_of": NA,
        #     "range_of": NO_RANGE
        # },
        # #"openend": {
        #     "field_name": "cod_openend",
        #     "renaming": "OpenEnd",
        #     "allow_null": FALSE,
        #     "type_of": STRING,
        #     "model_of": NA,
        #     "decimals_of": NA,
        #     "range_of": NO_RANGE
        # },       
        # #"callable": {
        #     "field_name": "cod_callable",
        #     "renaming": "Callable",
        #     "allow_null": FALSE,
        #     "type_of": STRING,
        #     "model_of": NA,
        #     "decimals_of": NA,
        #     "range_of": NO_RANGE
        # },
        # #"putable": {
        #     "field_name": "cod_putable",
        #     "renaming": "Putable",
        #     "allow_null": FALSE,
        #     "type_of": STRING,
        #     "model_of": NA,
        #     "decimals_of": NA,
        #     "range_of": NO_RANGE
        # },
        # #"creditlinked": {
        #     "field_name": "cod_creditlinked",
        #     "renaming": "CreditLinked",
        #     "allow_null": FALSE,
        #     "type_of": STRING,
        #     "model_of": NA,
        #     "decimals_of": NA,
        #     "range_of": NO_RANGE
        # },
        # #"decodifica": {
        #     "field_name": "cod_decodifica",
        #     "renaming": "Decodifica",
        #     "allow_null": FALSE,
        #     "type_of": STRING,
        #     "model_of": NA,
        #     "decimals_of": NA,
        #     "range_of": NO_RANGE
        # },
        # #"retail": {
        #     "field_name": "cod_retail",
        #     "renaming": "Retail",
        #     "allow_null": FALSE,
        #     "type_of": STRING,
        #     "model_of": NA,
        #     "decimals_of": NA,
        #     "range_of": NO_RANGE
        # },
        # #"defaulted": {
        #     "field_name": "cod_defaulted",
        #     "renaming": "Defaulted",
        #     "allow_null": FALSE,
        #     "type_of": STRING,
        #     "model_of": NA,
        #     "decimals_of": NA,
        #     "range_of": NO_RANGE
        # },
        # #"note": {
        #     "field_name": "cod_note",
        #     "renaming": "Note",
        #     "allow_null": FALSE,
        #     "type_of": STRING,
        #     "model_of": NA,
        #     "decimals_of": NA,
        #     "range_of": NO_RANGE
        # },
        # #"fare": {
        #     "field_name": "cod_fare",
        #     "renaming": "Fare",
        #     "allow_null": FALSE,
        #     "type_of": STRING,
        #     "model_of": NA,
        #     "decimals_of": NA,
        #     "range_of": NO_RANGE
        # },
        # #"farebailin": {
        #     "field_name": "cod_farebailin",
        #     "renaming": "FareBailIn",
        #     "allow_null": FALSE,
        #     "type_of": STRING,
        #     "model_of": NA,
        #     "decimals_of": NA,
        #     "range_of": NO_RANGE
        # }
    },
    "sections": 
    {
        "section0": {
            "name": "Informazioni di base",
            "list": ['cod_100isin', 'cod_101descrizione', 'cod_102ipotitolo', 'cod_103emittente', 
                    #  'cod_idemittente',
                        'cod_104divisa', 'cod_105mercato',
                    #  'cod_quotato',
                        'cod_106valorenominale', 'cod_107garanziaminimaperc',
                    #  'cod_garantito',
                        'cod_108protezionecondizionataperc', 'cod_109barrieraprotezioneperc', 'cod_110tipobarrieraprotezione',
                    #  'cod_levacapitale', 'cod_levaperccapitale', 'cod_levacedolare', 'cod_levaperccedolare',
                        'cod_111cedolagarantitaperc', 'cod_112cedolacondizionataperc', 'cod_113barrieracedolacondizionataperc',
                    #  'cod_cedolacapperc', 'cod_codicesottostante', 'cod_nomesottostante', 'cod_divisasottostante', 'cod_tiposottostante',
                    #  'cod_sottostantebasket', 'cod_numerosottostanti', 'cod_tipocalcolobasketperf', 'cod_sottostanteopaco',
                        'cod_115posizionelongshortsusottostante', 'cod_116strategialongshort',
                     #  'cod_isquanto', 'cod_pathdependent',
                        'cod_117tiporilevazione',
                    #  'cod_finecollocamento',
                        'cod_118dataemissione', 'cod_119datascadenza', 'cod_120automaticearlyredemption',
                    #  'cod_tipopayoff', 'cod_datainserimento', 'cod_classeeusipa', 'cod_tipo_idemittente',
                        'cod_121bailin',       
                    #  'cod_rankingbailin', 
                    #  'cod_strike', 'cod_cedolafloorperc', 'cod_openend', 'cod_callable', 'cod_putable', 'cod_creditlinked', 'cod_decodifica', 
                    #  'cod_retail', 'cod_defaulted', 'cod_note', 'cod_fare', 'cod_farebailin'
                     ]
        },
        #tolgi seconda sezioone
        #"section1": {
            # "name": "Anagrafica Sottostanti",
            # "list": ['cod_sottostante_1(anagraficasottostanti)', 'cod_sottostante_2(anagraficasottostanti)', 'cod_sottostante_3(anagraficasottostanti)', 'cod_sottostante_4(anagraficasottostanti)', 'cod_sottostante_5(anagraficasottostanti)']

    }
}
