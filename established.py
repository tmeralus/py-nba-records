import json
import pandas as pd
import argparse # adding command line switches 

# read teams data
nba_teams = pd.read_json('data/team-history.json')
nba_table = pd.DataFrame(nba_teams)
 
print(nba_table) 
