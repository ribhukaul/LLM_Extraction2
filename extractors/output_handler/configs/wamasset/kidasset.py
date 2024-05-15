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

kidasset = {
    "fields":{
        "isin": {
            "field_name": "cod_100isin",
            "renaming": "ISIN",
            "allow_null": FALSE,
            "type_of": STRING,
            "model_of": NA,
            "decimals_of": NA,
            "range_of": ISIN_RANGE
        },
        'date': {
            "field_name": "cod_101date",
            "renaming": "Data di validità",
            "allow_null": FALSE,
            "type_of": DATE,
            "model_of": NA,
            "decimals_of": NA,
            "range_of": DATE_RANGE
        },
        "picpac": {
            "field_name": "cod_102picpac",
            "renaming": "PIC o PAC",
            "allow_null": FALSE,
            "type_of": STRING,
            "model_of": NA,
            "decimals_of": NA,
            "range_of": NO_RANGE
        },
        "classe_fondo": {
            "field_name": "cod_103classe_fondo",
            "renaming": "Classe Fondo",
            "allow_null": FALSE,
            "type_of": STRING,
            "model_of": NA,
            "decimals_of": NA,
            "range_of": NO_RANGE
        },
        "strategia": {
            "field_name": "cod_104strategia",
            "renaming": "Strategia",
            "allow_null": FALSE,
            "type_of": STRING,
            "model_of": NA,
            "decimals_of": NA,
            "range_of": NO_RANGE
        },
        "periodo_detenzione_raccomandato": {
            "field_name": "cod_105rhp",
            "renaming": "RHP (anni)",
            "allow_null": FALSE,
            "type_of": INT,
            "model_of": YEARS,
            "decimals_of": NA,
            "range_of": PERCENT_RANGE        
            },
        "indicatore_sintetico_rischio": {
            "field_name": "cod_106sri",
            "renaming": "SRI",
            "allow_null": FALSE,
            "type_of": INT,
            "model_of": YEARS,
            "decimals_of": NA,
            "range_of": SRI_RANGE        
            },
        "costi_ingresso": {
            "field_name": "cod_107costi_ingresso",
            "renaming": "Costi ingresso (%)",
            "allow_null": TRUE,
            "type_of": FLOAT,
            "model_of": PERCENT,
            "decimals_of": 2,
            "range_of": PERCENT_RANGE        
            },
        "costingresso_dirittifissi": {
            "field_name": "cod_108costingresso_dirittifissi",
            "renaming": "Costi di ingresso diritti fissi (€)",
            "allow_null": TRUE,
            "type_of": FLOAT,
            "model_of": EURO,
            "decimals_of": 1,
            "range_of": NO_RANGE        
            },
        "costi_uscita": {
            "field_name": "cod_109costi_uscita",
            "renaming": "Costi uscita (%)",
            "allow_null": TRUE,
            "type_of": FLOAT,
            "model_of": PERCENT,
            "decimals_of": 2,
            "range_of": PERCENT_RANGE        
            },
        "costiuscita_dirittifissi": {
            "field_name": "cod_110costiuscita_dirittifissi",
            "renaming": "Costi di uscita diritti fissi (€)",
            "allow_null": TRUE,
            "type_of": FLOAT,
            "model_of": EURO,
            "decimals_of": 1,
            "range_of": NO_RANGE        
            },
        "commissione_gestione": {
            "field_name": "cod_111commissioni_di_gestione",
            "renaming": "Costi correnti (%)",
            "allow_null": FALSE,
            "type_of": FLOAT,
            "model_of": PERCENT,
            "decimals_of": 2,
            "range_of": PERCENT_RANGE        
            },
        "commissione_transazione": {
            "field_name": "cod_112costi_di_transazione",
            "renaming": "Costi di transazione (%)",
            "allow_null": FALSE,
            "type_of": FLOAT,
            "model_of": PERCENT,
            "decimals_of": 2,
            "range_of": PERCENT_RANGE        
            },
        "descrizione_performance": {
            "field_name": "cod_113descrizione_performance",
            "renaming": "Commissioni di performance",
            "allow_null": FALSE,
            "type_of": STRING,
            "model_of": NA,
            "decimals_of": NA,
            "range_of": NO_RANGE        
            },
        "commissione_performance": {
            "field_name": "cod_114commissioni_di_performance",
            "renaming": "Commissioni di performance (€)",
            "allow_null": TRUE,
            "type_of": FLOAT,
            "model_of": EURO,
            "decimals_of": 2,
            "range_of": NO_RANGE       
            }       
    },
    "sections":{
        "section0": {
            "name": "Informazioni Generali",
            "list": ["cod_100isin", "cod_101date", "cod_102picpac", "cod_103classe_fondo", "cod_104strategia", "cod_105rhp", "cod_106sri"]
           
        },
        "Costi": {
            "name": "Costi",
            "list": ["cod_107costi_ingresso", "cod_108costingresso_dirittifissi", "cod_109costi_uscita", "cod_110costiuscita_dirittifissi", 
                     "cod_111commissioni_di_gestione", "cod_112costi_di_transazione", "cod_113descrizione_performance", "cod_114commissioni_di_performance"]
        }
    }
}