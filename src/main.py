from reports import generateReport
from contextlib import redirect_stdout
''' 
    @author: Lucas Guimaraes <lucasg.conceicao@gmail.com>
    Executes the ETL pipeline for The EPL (English Premier League)
    It reads all epl files from all seasons, parse the data and generate all the reports.
    The reports being generated are:
        - The position table for all the seasons
        - The summary statistics for all teams by season. It includes best scoring team and ratio of shots on target convert in goals.
'''
if __name__ == '__main__':
    # Initialize generateReport Class
    obj = generateReport()
    position_table_report_path = obj.working_directory / "reports" / 'position_table_by_season.txt'
    general_stats_report_path = obj.working_directory / "reports" / 'general_stats_by_season.txt'

    ''' Redirect stdout to file to generate reports '''
    # Position Table by season
    print('Executing...')
    with open(position_table_report_path , 'w') as f:
        with redirect_stdout(f):
            try:
                obj.postionTableBySeason()
            except Exception as e:
                print('LOG: Error on position table report generation.', e)

    # All stats by season
    with open(general_stats_report_path , 'w') as f:
        with redirect_stdout(f):
            try:
                obj.statsRankedBySeason('goals')            
                obj.statsRankedBySeason('ratio_goals_shots_on_target')
            except Exception as e:
                print('LOG: Error on stats report generation.', e)
    print('Succeed! Please check reports.')