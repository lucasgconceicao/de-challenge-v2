import json, jsonschema
from jsonschema import validate

class Validator:
    def __init__(self):
        # EPL schema 
        self.raw_schema = {
            "title": "EPL - English Premier League",
            "type" : "object",
            "properties" : {
                "AC": {"type": ["number", "null"]},
                "AF": {"type": ["number", "null"]},
                "AR": {"type": ["number", "null"]},
                "AS": {"type": ["number", "null"]},
                "AST": {"type": ["number", "null"]},
                "AY": {"type": ["number", "null"]},
                "AwayTeam": {"type": "string"},
                "B365A": {"type": ["number", "null"]},
                "B365D": {"type": ["number", "null"]},
                "B365H": {"type": ["number", "null"]},
                "BWA": {"type": ["number", "null"]},
                "BWD": {"type": ["number", "null"]},
                "BWH": {"type": ["number", "null"]},
                "Bb1X2": {"type": ["number", "null"]},
                "BbAH": {"type": ["number", "null"]},
                "BbAHh": {"type": ["number", "null"]},
                "BbAv<2.5": {"type": ["number", "null"]},
                "BbAv>2.5": {"type": ["number", "null"]},
                "BbAvA": {"type": ["number", "null"]},
                "BbAvAHA": {"type": ["number", "null"]},
                "BbAvAHH": {"type": ["number", "null"]},
                "BbAvD": {"type": ["number", "null"]},
                "BbAvH": {"type": ["number", "null"]},
                "BbMx<2.5": {"type": ["number", "null"]},
                "BbMx>2.5": {"type": ["number", "null"]},
                "BbMxA": {"type": ["number", "null"]},
                "BbMxAHA": {"type": ["number", "null"]},
                "BbMxAHH": {"type": ["number", "null"]},
                "BbMxD": {"type": ["number", "null"]},
                "BbMxH": {"type": ["number", "null"]},
                "BbOU": {"type": ["number", "null"]},
                "Date": {"type": "string"},
                "Div": {"type": "string"},
                "FTAG": {"type": "number"},
                "FTHG": {"type": "number"},
                "FTR": {"type": "string"},
                "HC": {"type": ["number", "null"]},
                "HF": {"type": ["number", "null"]},
                "HR": {"type": ["number", "null"]},
                "HS": {"type": ["number", "null"]},
                "HST": {"type": ["number", "null"]},
                "HTAG": {"type": ["number", "null"]},
                "HTHG": {"type": ["number", "null"]},
                "HTR": {"type": "string"},
                "HY": {"type": ["number", "null"]},
                "HomeTeam": {"type": "string"},
                "IWA": {"type": ["number", "null"]},
                "IWD": {"type": ["number", "null"]},
                "IWH": {"type": ["number", "null"]},
                "PSA": {"type": ["number", "null"]},
                "PSCA": {"type": ["number", "null"]},
                "PSCD": {"type": ["number", "null"]},
                "PSCH": {"type": ["number", "null"]},
                "PSD": {"type": ["number", "null"]},
                "PSH": {"type": ["number", "null"]},
                "Referee": {"type": "string"},
                "VCA": {"type": ["number", "null"]},
                "VCD": {"type": ["number", "null"]},
                "VCH": {"type": ["number", "null"]},
                "WHA": {"type": ["number", "null"]},
                "WHD": {"type": ["number", "null"]},
                "WHH": {"type": ["number", "null"]}
            }
        }        
        self.parsed_schema = {
            "title": "EPL - English Premier League",
            "type" : "object",
            "properties" : {
                "Date": {"type": ["string", "null"]},
                "HomeTeam": {"type": ["string", "null"]},
                "AwayTeam": {"type": ["string", "null"]},
                "FTHG": {"type": ["number", "null"]},
                "FTAG": {"type": ["number", "null"]},
                "FTR": {"type": ["string", "null"]},
                "HST": {"type": ["number", "null"]},
                "AST": {"type": ["number", "null"]},
                "HS": {"type": ["number", "null"]},
                "AS": {"type": ["number", "null"]}
            },
            "required":[
               "Date", "HomeTeam", "AwayTeam", "FTHG", "FTAG", "FTR", "HST", "AST", "HS", "AS"
            ]
        }

    def validateSchema(self, json_data, schema):
        try:
            jsonschema.validate(instance=json_data, schema=schema)
            return True, "Json is valid."
        except jsonschema.exceptions.ValidationError as msg_err:
            #msg_err = "EPL JSON data has an invalid schema"
            return False, msg_err

    def validateSchemaCheck(self, data):
        # validate the schema
        print("LOG: Validating Schema...")
        for k,v in data.items():            
            for d in v:
                result = self.validateSchema(json_data = d)
                if result[0] == False:
                    print(k, result)

