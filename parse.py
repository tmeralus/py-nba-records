#!/usr/bin/env python  
from art import * 
import json
import random
import pandas as pd  
import numpy as np

h2h_rivals_base_url = "https://www.landofbasketball.com/head_to_head/"  
worst_to_make_playoffs_url = "https://www.landofbasketball.com/statistics/worst_to_make_playoffs.htm"
worst_seasons_url = "https://www.landofbasketball.com/statistics/worst_seasons.htm"
best_seasons_url = "https://www.landofbasketball.com/statistics/best_seasons.htm"
playoffs_missed_streaks_url = "https://www.landofbasketball.com/statistics/playoffs_missed_streaks.htm"
best_starts_url = "https://www.landofbasketball.com/statistics/best_starts.htm"
worst_starts_url = "https://www.landofbasketball.com/statistics/worst_starts.htm"
all_time_season_standings_url =  "https://www.landofbasketball.com/statistics/all_time_season_standings.htm"
all_time_playoff_standings_url = "https://www.landofbasketball.com/statistics/all_time_playoff_standings.htm"

def url_scraper():
    url = worst_to_make_playoffs_url
    # use pandas to extract and scrape data 
    data = pd.read_html(url, keep_default_na=False) 
    # extract columns
    data1 = data[0]
    # print extracted columns 
    #print(data1)
    table = pd.DataFrame(data1)
    print(table)
    # making a yellow border
    table.style.set_table_styles([{'selector' : '',
                                'props' : [('border',
                                            '2px solid green')]}])

def random_stats():
    stats_list = [worst_to_make_playoffs_url, worst_seasons_url, best_seasons_url, playoffs_missed_streaks_url, best_starts_url, worst_starts_url, all_time_season_standings_url, all_time_playoff_standings_url ]
    # create variable for randon choies
    random_stats_choice_url = (random.choice(stats_list)) 
    # use pandas to extract and scrape data 
    random_data = pd.read_html(random_stats_choice_url, keep_default_na=False) 
    # extract columns
    random_data1 = random_data[0]
    # print extracted columns 
    #print(random_data1)
    nba_table = pd.DataFrame(random_data1)
    print(nba_table)

def h2h_rivals(): 
    print("test")

def worst_to_make_playoffs_scraper(): 
    print("test")
def worst_seasons_scraper():
    print("test")
def best_seasons_scraper():
    print("test")
def playoffs_missed_streaks_scraper():
    print("test")
def best_starts_scraper():
    print("test")
def worst_starts_scraper():
    print("test")
def all_time_season_standings_scraper():
    print("test")
def all_time_playoff_standings_scraper():  
    print("test")
     
def head_to_head():
        # read teams data
        nba_teams = pd.read_json('data/team-history.json')
        team1 = ""
        team2 = ""
        season_url = "https://www.landofbasketball.com/head_to_head_gl/heat_vs_timberwolves_game_log_season.htm"
        all_time_url = "https://www.landofbasketball.com/head_to_head/lakers_vs_heat_all_time.htm" 

        nba_table = pd.DataFrame(nba_teams)
        print(nba_table) 
        url3 = "https://www.landofbasketball.com/head_to_head.htm"
        
        #  keep_default_na=False removes the default behavior of replacing missing values with NaN
        testdata = pd.read_html(season_url, keep_default_na=False)
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

 