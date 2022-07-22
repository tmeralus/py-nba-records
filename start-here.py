#!/usr/bin/env python 
import random
import argparse # adding command line switches 
from art import * 
from records import * # random record data 

# credits 
__author__ = "Tedley Meralus"
__copyright__ = "Copyright 2022, Tedley Meralus"
__credits__ = ["Tedley Meralus",]
__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "Tedley Meralus"
__email__ = "tmeralus@gmail.com"
__status__ = "Development"

# Banner Ascii Art and notes
BannerBorder=("----------------------------------------------------------------------------------------------------------")
BarcodeBorder=text2art("---------------------------------------------------------------------------------",font="fancy12",decoration="barcode1")
BarcodeEmptyBorder=text2art("                                                                                        ",font="fancy12",decoration="barcode1")
BannerBorder=("----------------------------------------------------------------------------------------------------------")
BannerHeader=("$ curl nba head to head records")
BannerBlank=("") 
BannerText1=("View head-to-head records, historical data, and more")
BannerAuthor=(" Follow @techgameteddy for updates")
BannerIssues=(" Issues: https://github.com/tmeralus/py-nba-records/issues") 
Bannerlink=(" Github: https://github.com/tmeralus/py-nba-records") 
BannerCredits=(" Credits: localhost/credits ") 

# Text 2 art simple logic
text2artfont_list = ["speed", "britei", "charact2", "radical", "smkeyboard", "tombstone", "rev", "italics", "asc"]
text2artfont_choices = (random.choice(text2artfont_list)) # chooses random item from text2artfont_list array to print
#BannerArt=text2art("nba records",font=text2artfont_choices) # print title with random text2art option from array
BannerArt=text2art("nba records",font="ascii") # print title with random text2art option from array

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

def title_banner():  
    print(BannerHeader) 
    print(BannerBlank)    
    print(BannerArt) 
    print(BannerBlank)    
    print(BannerText1) 
#    print(BannerText2)    
    print(BannerBorder) 
 
def footer(): 
    print(BannerBorder) 
    print(BannerAuthor, Bannerlink) 
    print(BannerBorder)

  
def interactive(): 
    parse_args()  
    title_banner() 
    random_stats() 
    footer() 

if __name__ == "__main__":
    interactive()

 