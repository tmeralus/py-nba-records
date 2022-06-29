#!/usr/bin/env python 
import json
import pandas as pd
import argparse # adding command line switches 
from art import *

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
 

# Credits Banner 
def credits_banner():
    cbanner = """
|----------------------------------------------------------------------------------------------------|
|                                                      ___________________   ___________________      |
|                     _ _ _                        .-/|                   \ /                  |\-.   |
|                    | (_) |                       ||||    ~~*~~           |       ~~*~~       ||||   |
|    ___ _ __ ___  __| |_| |_ ___                  |||| Dr. James Naismith |    Inventor of    ||||   |
|   / __| '__/ _ \/ _` | | __/ __|                 ||||                    |    Basketball     ||||   |
|   | (__| | |  __/ (_| | | |_\__ \                ||||    ~~*~~           |       ~~*~~       ||||   |
|    \___|_|  \___|\__,_|_|\__|___/                |||| Born: 11-06-1861   |   ____________    ||||   |
|                                                  |||| Died: 11-28-1939   |  |_____ ______|   ||||   |
|                                                  ||||                    |   \/\/\/\\//\/    ||||   |
|                                                  ||||    ~~*~~           |    \/\/\/\/\/     ||||   |
|                                                  ||||   Physician,       |     |/\/\/\|      ||||   |
|                                                  ||||    Educator        |      |/\/\|       ||||   |
|                                                  ||||    Chaplain,       |                   ||||   |
|                                                  ||||   Sports coach,    |                   ||||   |
|                                                  ||||___________________ | __________________||||   |
|                                                  ||/====================\|/===================\||   |
|                                                  `---------------------~___~-------------------''   |
|-----------------------------------------------------------------------------------------------------|
|                                                                         |                           |
|   Credits and Contributions to the nba-historian Python App             |                           |
|   Created by Tedley Meralus <tmeralus@gmail.com>                        |                           |
|    Twitter: @techgameteddy                                              |                           |
|                                                                         |                           |
|-----------------------------------------------------------------------------------------------------|
        """
    print(cbanner) 

# Banner Ascii Art and notes
Banner_goat=text2art("G.O.A.T. DEBATE", "random")
Banner_head_to_head=text2art("Head To Head Comparison", "random")
BannerBorder=("----------------------------------------------------------------------------------------------------------")
BarcodeBorder=text2art("---------------------------------------------------------------------------------",font="fancy12",decoration="barcode1")
BarcodeEmptyBorder=text2art("                                                                                        ",font="fancy12",decoration="barcode1")
BannerBorder=("----------------------------------------------------------------------------------------------------------")
BannerText1=("Head To Head Comparison")
BannerText2=("                      View head-to-head records, historical data, and more")
BannerAuthor=(" Created by @techgameteddy")
BannerIssues=(" Issues: https://github.com/tmeralus/py-nba-records ") 
BannerCredits=(" Credits: localhost/creddits ") 

def title_banner():  
    print(Banner_goat)   
    print(BannerBorder)  
    print(BannerText1)   
    print(BannerBorder) 
 
# function for list of team names 
def head_to_head_table(): 
    # read teams data
    nba_teams = pd.read_json('data/team-history.json')
    nba_table = pd.DataFrame(nba_teams)
    print(nba_table) 

def interactive(): 
    title_banner()
    head_to_head_table() 
    
if __name__ == "__main__":
    interactive()

 