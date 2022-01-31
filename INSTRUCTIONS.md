# Instructions
How to execute deployement of the ETL pipeline for The EPL (English Premier League)
Requirements: Docker, Python

# Docker
1. Clone the repository
```
git clone https://github.com/lucasgconceicao/de-challenge-v2.git
```
2. Navigate to cloned repository /de-challenge-v2/
```
cd ./de-challenge-v2/
```
3. Create a Docker Image from DockerFile
```
docker build --tag epl_image -f ./deploy/Dockerfile .
```
4. Execute the ETL script
```
windows: docker run -v %cd%/reports/:/reports/ epl_image
linux: docker run -v $PWD/reports/:/reports/ epl_imagee
```

# VirtualEnv
1. Create new virutal env
```
python -m venv venv
```
2. Activate the virtual env and install dependencies, then navigate to the src
```
venv\Scripts\activate (linux: source venv/bin/activate)
pip install -r deploy/requirements.txt
cd src
```
3. Run the EPL job
```
python src/main.py
```

# Reports should be generate at:
./de-challenge-v2/reports/
    - /reports/position_table_by_season.txt -> The position table for all the seasons 
    - /reports/general_stats_by_season.txt -> The summary statistics for all teams by season. It includes best scoring team and ratio of shots on target convert in goals by season.    
    
    