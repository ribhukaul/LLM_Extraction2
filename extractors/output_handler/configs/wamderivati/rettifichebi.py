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




rettifichebi = {
    "fields": {
        "ex_date": {
            "field_name": "cod_ex_date",
            "renaming": "Ex date",
            "allow_null": FALSE,
            "type_of": DATE,
            "model_of": NA,
            "decimals_of": NA,
            "range_of": NO_RANGE
        },
        "isin_sottostante": {
            "field_name": "cod_isin",
            "renaming": "ISIN",
            "allow_null": FALSE,
            "type_of": STRING,
            "model_of": NA,
            "decimals_of": NA,
            "range_of": NO_RANGE
        },
        "fattore_rettifica": {
            "field_name": "cod_codice_rettifica",
            "renaming": "Fattore di rettifica",
            "allow_null": FALSE,
            "type_of": STRING,
            "model_of": NA,
            "decimals_of": NA,
            "range_of": NO_RANGE
        },

    },
    "sections": 
    {
        "section0": {
            "name": "Informazioni",
            "list": ['cod_ex_date', 'cod_isin', 'cod_codice_rettifica']

    }
}
}


