#!/usr/bin/env python 
import json
import pandas as pd
import argparse # adding command line switches 
from art import *
import requests
import numpy as np
from requests.structures import CaseInsensitiveDict

__author__ = "Tedley Meralus"
__copyright__ = "Copyright 2022, Tedley Meralus"
__credits__ = ["Tedley Meralus",]
__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "Tedley Meralus"
__email__ = "tmeralus@gmail.com"
__status__ = "Development"


# Parse Arguments
def parser_error(errmsg): 
    print("Usage: python " + sys.argv[0] + " [Options] use -h for help")
    print(R + "Error: " + errmsg + W)
    sys.exit()

def parse_args():  
    # add command-line arguments
    parser = argparse.ArgumentParser(description='a python tool that grabs historical nba records to gather head-to-head matchups of nba teams and more')
    parser.error = parser_error
    parser._optionals.title = "OPTIONS" 
    parser.add_argument("--credits", help="Prints credits and contributions page") 
    parser.add_argument("-e", "-est", "--established", help=" print records of teams establised year and names") 
    parser.add_argument("-t", "-teams", "--teams", help=" print record of teams in order of championships")  
    return parser.parse_args()

# Banner Ascii Art and notes
BannerArt=text2art("NBA Records",font="rnd-small")
#BannerArt_teams=text2art("NBA Records", "bolger")
BannerBorder=("----------------------------------------------------------------------------------------------------------")
BarcodeBorder=text2art("---------------------------------------------------------------------------------",font="fancy12",decoration="barcode1")
BarcodeEmptyBorder=text2art("                                                                                        ",font="fancy12",decoration="barcode1")
BannerBorder=("----------------------------------------------------------------------------------------------------------")
BannerText1=("                   Compare how NBA Teams Matchup against each other")
BannerText2=("                      View head-to-head records, historical data, and more")
BannerAuthor=(" Follow @techgameteddy for updates")
BannerIssues=(" Issues: https://github.com/tmeralus/py-nba-records/issues") 
Bannerlink=(" Github: https://github.com/tmeralus/py-nba-records") 
BannerCredits=(" Credits: localhost/credits ") 

def title_banner():  
    print(BannerArt)  
    print(BannerBorder)  
    print(BannerText1) 
    print(BannerText2) 
    print(BannerBorder)  
 
def footer():
    print(BannerBorder)  
    print(BannerAuthor, Bannerlink) 
    print("")   

# function for list of team names 
def team_history_table(): 
    # read teams data
    nba_teams = pd.read_json('data/team-history.json')
    nba_table = pd.DataFrame(nba_teams)
    print(nba_table) 


def team_test():
        url = "https://www.landofbasketball.com/head_to_head_gl/heat_vs_timberwolves_game_log_season.htm"
        h2hurl = "https://www.landofbasketball.com/head_to_head/heat_rivals.htm"
        h2hmia = "https://www.landofbasketball.com/head_to_head/heat_rivals.htm"
        url2 = "https://www.landofbasketball.com/head_to_head.htm"
        
        testdata = pd.read_html(url)
        #testdata2 = pd.read_html(url).fillna('')
        # Replace all Nan values to empty string
        #testdatae = testdata.replace(np.nan, '', regex=True)
        #df2 = df.replace(np.nan, '', regex=True)
        #print(df2)
 

        # print most recent 5 seasons
        print("Head To Head in the Regular Season")
        print(testdata[1:6])

def interactive(): 
    parse_args()  
    title_banner()
    team_test()  
    footer()

if __name__ == "__main__":
    interactive()

 