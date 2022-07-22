#!/usr/bin/env python 
from cgi import test
import json
import pandas as pd
import argparse # adding command line switches 
from art import * 
import html5lib
import numpy as np
from requests.structures import CaseInsensitiveDict
 

# function for list of team names 
def team_history_table(): 
    # read teams data
    nba_teams = pd.read_json('data/team-history.json')
    nba_table = pd.DataFrame(nba_teams)
    print(nba_table) 

def random_stats():
    print("no stats available")
    
def head_to_head():
        url = "https://www.landofbasketball.com/head_to_head_gl/heat_vs_timberwolves_game_log_season.htm"
        url2 = "https://www.landofbasketball.com/head_to_head/lakers_vs_heat_all_time.htm" 
        url3 = "https://www.landofbasketball.com/head_to_head.htm"
        
        #  keep_default_na=False removes the default behavior of replacing missing values with NaN
        testdata = pd.read_html(url, keep_default_na=False)
        print(len(testdata))
        # prints a new text banner 
        print("Head To Head in the Regular Season")
        # variables for data ranging from 3-5 years
        data0 = testdata[0]  
        data1 = testdata[1]
        data2 = testdata[2]
        data3 = testdata[3]
        data4 = testdata[4]
        data5 = testdata[5]  
        data6 = testdata[6]  
        data2[0:6].astype('object')
        print(data0.head())
        print(data1.head())
        print(data2.head())
        print(data3.head())
#        print(data4.head())
#        print(data5.head())

def interactive():  
    head_to_head()   

if __name__ == "__main__":
    interactive()

 