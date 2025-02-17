
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

cga = {
    "fields": {
        # GENERAL INFO
        "tariffa": {
            "field_name": "cod_100tariffa",
            "renaming": "Tipologia di tariffa",
            "allow_null": FALSE,
            "type_of": STRING,
            "model_of": NA,
            "decimals_of": NA,
            "range_of": NO_RANGE 
            },
        "durata": {
            "field_name": "cod_101durata",
            "renaming": "Durata polizza (se presente)",
            "allow_null": FALSE,
            "type_of": STRING,
            "model_of": NA,
            "decimals_of": NA,
            "range_of": NO_RANGE        
            },
        "unico": {
            "field_name": "cod_102unico",
            "renaming": "Polizza a premio unico?",
            "allow_null": FALSE,
            "type_of": BOOL,
            "model_of": NA,
            "decimals_of": NA,
            "range_of": NO_RANGE        
            },
        "ricorrente": {
            "field_name": "cod_103ricorrente",
            "renaming": "Polizza a premio ricorrente?",
            "allow_null": FALSE,
            "type_of": BOOL,
            "model_of": NA,
            "decimals_of": NA,
            "range_of": NO_RANGE        
            },
       
    },
    "sections": 
    {
        "section0": {
            "name": "TInformazioni polizza",
            "list": ["cod_100tariffa", "cod_101durata", "cod_102unico", "cod_103ricorrente"],
        },
    }
}


