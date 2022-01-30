from schema_validator import Validator
from datetime import datetime
import json
import glob
import re
import sys

class Parser:
    ''' Parser class Read and Parse EPL files''' 
    def readFiles(self, path):
        '''
        Generic function to read files from a path
        :param str path: Path to the files, it can contain wildcard patterns.
        :return: dict of the files from the specified path with json raw content
        :rtype: dict
        '''
        print('LOG: {} Readind Data...'.format(datetime.now()))
        data = {}
        files = glob.glob(path, recursive=True)
        for season_file in files:
            with open(season_file, 'r') as f:
                content = f.read()
            data.update({f.name: json.loads(content)})
        return data

    def parseFiles(self, data, validate_schema=False):
        '''
        Generic function to parse EPL files.
        :param dict data: dict of files with its season and matches. [{seaoson: [matches]}]
        :param boolean validate_schema: if schema needs to be validated, set to True. 
        :return: list of matches by season
        :rtype: (list|Exception)
        '''
        print('LOG: {} Parsing Data...'.format(datetime.now()))
        validator = Validator()
        all_matches = []
        for season, match_results in data.items():
            season = re.search(r'season-\d{4}', season).group()
            for match in match_results:                
                try:
                    if validate_schema:
                        validator_result = validator.validateSchema(json_data = match, schema=validator.parsed_schema)
                        if validator_result[0] == False:
                            sys.exit("Failed to validate schema. JSON has an invalid schema.\n {}{}".format(season, validator_result[1]))
                    match_result = (
                        str(season),
                        match['Date'],
                        match['HomeTeam'], 
                        match['AwayTeam'], 
                        match['FTHG'], 
                        match['FTAG'],
                        match['FTR'],
                        match['HST'],
                        match['AST'],
                        match['HS'],
                        match['AS'],
                    )
                    all_matches.append(match_result)
                except Exception as e:
                    print(e)
        return all_matches