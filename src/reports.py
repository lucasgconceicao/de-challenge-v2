from epl_table import EPLS
from datetime import datetime

class generateReport(EPLS):
    ''' Generate all position table and general stats report'''
    def __init__(self):
        super().__init__()
        self.current_date = datetime.now()

    def postionTableBySeason(self):
        '''
        Function to generate the position table by Season
        :return: True, formatted position table to stdout
        :rtype: stdout
        '''
        all_stats = self.getStats()
        scored_goals = []
        for season, stats in all_stats.items():
            for team, stat in stats['teams'].items():
                scored_goals.append((season, team, stat['points']))
        scored_goals = (sorted(scored_goals, key=lambda x: (x[0], x[2]), reverse=True))
        
        possible_seasons = self.getAttributes('seasons')
        season_pos = 0
        pos = 1

        print('\nPosition Table Report - {}\n'.format(self.current_date))
        print("=" * 44)
        print('{:^8} {:>10} {:^20} {:>3}'.format('SEASON', 'POS', 'TEAM', 'PTS'))
        print("=" * 44)
        for team in scored_goals:
            if team[0] != sorted(possible_seasons, reverse=True)[season_pos]:
                print("=" * 44)
                print('{:^8} {:>10} {:^20} {:>3}'.format('SEASON', 'POS', 'TEAM', 'PTS'))
                print("=" * 44)
                season_pos += 1
                pos = 1
            print('{season:^1} {pos:>6} {team:>16} {points:>8}'.format(season=team[0], pos=pos, team=team[1], points=team[2]))
            pos += 1
        return True

    def statsRankedBySeason(self, stat_val):
        '''
        Function to generate the any given stat by season by team
        :param str stat_val: type of stat to be printed out
        :return: True, formatted table to stdout
        :rtype: stdout
        '''
        if stat_val not in ['goals', 'ratio_goals_shots_on_target']:
            raise ValueError('Ivalid Stat')

        if stat_val == 'goals':
            header = '{:^12}{:^20}{:^8}'.format('Season', 'Team', 'Goals')
        elif stat_val == 'ratio_goals_shots_on_target':
            header = '{:^12}{:^15}{:^10}'.format('Season', 'Team', "Ratio Goals x Shots on Target")
        
        all_stats = self.getStats()
        possible_seasons = self.getAttributes('seasons') 

        scored_goals = []
        for season, stats in all_stats.items():
            for team, stat in stats['teams'].items():
                scored_goals.append((season, team, stat[stat_val]))
        scored_goals = (sorted(scored_goals, key=lambda x: (x[0], x[2]), reverse=True))

        season_pos = 0
        print('\nStatistics Report - {}\n'.format(self.current_date))
        print('='*58)
        print(header)
        print('='*58)
        for i in scored_goals:
            try:
                if i[0] == sorted(possible_seasons, reverse=True)[season_pos]:
                    season_pos +=1
                    print('{season:<15} {team:<15} {stat:>5}'.format(season=i[0], team=i[1], stat=i[2]))
            except:
                break
        print('\n')
        return True
    
    