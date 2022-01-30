# Instructions

# Navigate to /de-challenge-v2/
cd ./de-challenge-v2/

# Create new virutal env and install dependencies
python -m venv venv

git clone https://github.com/lucasgconceicao/de-challenge-v2.git

# Activate the .eplenv and navigate to the src location of main.py
venv\Scripts\activate (Linux: venv/bin/activate)
pip install -r requirements.txt
cd src

# Run the ETL job for EPL reporting
python main.py

# Reports:
    - /reports/position_table_by_season.txt -> The position table for all the seasons 
    - /reports/general_stats_by_season.txt -> The summary statistics for all teams by season. It includes best scoring team and ratio of shots on target convert in goals by season. 
    
    