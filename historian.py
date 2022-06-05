#!/usr/bin/env python 
import json
import pandas as pd
import argparse # adding command line switches 

__author__ = "Tedley Meralus"
__copyright__ = "Copyright 2022, Tedley Meralus"
__credits__ = ["Tedley Meralus",]
__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "Tedley Meralus"
__email__ = "tmeralus@gmail.com"
__status__ = "Development"

def title_banner():
    banner = """ 
|----------------------------------------------------------------------------------------------------------|
|             __             __    _      __             _             |                                   |
|      ____  / /_  ____ _   / /_  (_)____/ /_____  _____(_)___ _____   |            ..ee$$$$$ee..          |
|     / __ \/ __ \/ __ `/  / __ \/ / ___/ __/ __ \/ ___/ / __ `/ __ \  |        .e$*""    $    ""*$e.      |
|    / / / / /_/ / /_/ /  / / / / (__  ) /_/ /_/ / /  / / /_/ / / / /  |      d"    *     $      z"  "b    |
|   /_/ /_/_.___/\__,_/  /_/ /_/_/____/\__/\____/_/  /_/\__,_/_/ /_/   |     3L    .F     $     'r    JP   |
|                                                                      |     *c    $      $      3.   z$   |
|               ---Python Nba Historical Matchups App---               |      *b  J"      $      3r  dP    |
|             See how NBA Teams Matchup against each other             |         "*$ee..  $  ..ze$P"       |
|              gather head-to-head records, historical data,           |             ""*******""           | 
|                            and more                                  |                                   |
|----------------------------------------------------------------------------------------------------------|
|                     created by @techgameteddy                                                            |
|----------------------------------------------------------------------------------------------------------|
        """
        
    print(banner) 


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

# read teams data
#nba_teams = pd.read_json('data/teams.json')
#nba_table = pd.DataFrame(nba_teams)
 


def interactive(): 
    title_banner()
    parse_args()  
    
if __name__ == "__main__":
    interactive()
