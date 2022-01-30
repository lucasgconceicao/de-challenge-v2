from data_parser import Parser
from pathlib import Path
from datetime import datetime

class EPLS:
    ''' Functions to generate overall stats for EPL data'''
    def __init__(self, validate_schema=False):
        '''
        Initialize working dirs a reference variables.
        '''
        self.working_directory = Path(__file__).parents[1]
        self.epl_files_path = str(self.working_directory / 'data' / '*season-[0-9]*.json')
        self.ref_points = {'A': 3, 'D': 1, 'H': 3}
        self.validate_schema = validate_schema
    
    def readData(self):
        '''
        Generic function to read epl data
        :return: list of matches by season
        :rtype: list
        '''
        data = Parser().readFiles(self.epl_files_path)
        all_matches = Parser().parseFiles(data, validate_schema=self.validate_schema)
        return all_matches
    
    def getAttributes(self, attribute):
        '''
        Generic function to generate list of attributes for season and teams.
        :param str attribute: type of attribute, season or teams
        :return: list of possible (teams|seasons)
        :rtype: list
        '''
        all_matches = self.readData()
        if attribute == 'seasons':
            possible_seasons = []
            for match in all_matches:
                possible_seasons.append((match[0])) 
            possible_seasons = sorted(set(possible_seasons))
            return possible_seasons
        elif attribute == 'teams':
            possible_teams = []
            for match in all_matches:
                possible_teams.append((match[0], match[2]))
            possible_teams = sorted(set(possible_teams))
            return possible_teams

    def getSeasonByTeamDict(self):
        '''
        Generic function to generate dictonary with combination of seasons and teams and stats
        :return: dict with stats by team and season
        :rtype: dict
        '''
        possible_seasons = self.getAttributes('seasons')
        possible_teams = self.getAttributes('teams')
        dict_season = {}
        for season in possible_seasons:
            dict_season.update({season: []})
            for team in possible_teams:
                if season == team[0]:
                    dict_season[season].append(team[1])
                    
        dict_metrics = {}
        for season, teams in dict_season.items():
            dict_metrics.update({season: {'teams': {}}})
            for team in teams:
                dict_metrics[season]['teams'].update({team: {
                    'points': [],
                    'goals': [],
                    'shots_on_target': [],
                }})        
        return dict_metrics

    def getStats(self):
        '''
        Generic function to aggregate and populate all stats by team and season
        :return: dict with stats by team and season
        :rtype: dict
        '''
        possible_teams = self.getAttributes('teams')        
        all_matches = self.readData()
        dict_stats = self.getSeasonByTeamDict()
        print('LOG: {} Computing Statistics...'.format(datetime.now()))
        # Populate all metrics for every team and season
        for match in all_matches:
            season = match[0]
            home_team = match[2]
            away_team = match[3]
            home_team_goals = match[4]
            away_team_goals = match[5]
            result = match[6]
            home_team_shots_on_target = match[7]
            away_team_shots_on_target = match[8]
            dict_stats[season]['teams'][home_team]['goals'].append(home_team_goals)
            dict_stats[season]['teams'][away_team]['goals'].append(away_team_goals)            
            dict_stats[season]['teams'][home_team]['shots_on_target'].append(home_team_shots_on_target)
            dict_stats[season]['teams'][away_team]['shots_on_target'].append(away_team_shots_on_target)

            ''' A = Away Team wins, H = Home Team wins, D = Draw'''
            if result == 'A':
                dict_stats[season]['teams'][away_team]['points'].append(self.ref_points.get('A'))
            elif result == 'H':
                dict_stats[season]['teams'][home_team]['points'].append(self.ref_points.get('H'))
            else:
                dict_stats[season]['teams'][away_team]['points'].append(self.ref_points.get('D'))
                dict_stats[season]['teams'][home_team]['points'].append(self.ref_points.get('D'))
        # For every possible team and season populate stats in the dictionary
        for season, team in possible_teams:
            team_season = dict_stats[season]['teams'][team]
            team_season['points'] = sum(team_season['points'])
            team_season['goals'] = sum(team_season['goals'])
            team_season['shots_on_target'] = sum(team_season['shots_on_target'])
            team_season['ratio_goals_shots_on_target'] = team_season['goals'] / team_season['shots_on_target']
        
        return dict_stats