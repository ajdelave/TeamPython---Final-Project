import os
import sys
import json
from json.decoder import JSONDecodeError
import sqlite3
import csv


# This function is used to find the average popularity ratings of a user's favorite songs from the year each was released.
# Year and Average Popularity (Out of 100) are the columns on the outputted CSV file
def spotify_manipulations_1():
    print("")
    print("Preforming Manipulation #1...")

    # Connect to database
    conn = sqlite3.connect('sql_data.sqlite')
    cur = conn.cursor()
    cur.execute('SELECT release_year, popularity FROM Spotify_Song_Info')

    # Create dictionary and fill list with data
    year_v_pop = {}
    data = []
    for row in cur:
        try:
            data.append(row)
        except:
            print('encoding error')
    
    # Loop through data to get important information
    for tup in data:
        year = tup [0]
        pop = tup[1]
        if year not in year_v_pop.keys():
            year_v_pop[year] = [pop]
        else:
            year_v_pop[year].append(pop)
    
    # Finds the avergae of the popularity ratings of all a user's favorite songs for their release year
    for item in year_v_pop.items():
        average = sum(item[1])/len(item[1])
        year_v_pop[item[0]] = int(average)

    # Sorts the lsit for easy viewing
    sorted_list_1 = sorted(year_v_pop.items(), key=lambda x: x[0])

    # Outputs a CSV file for use in spotify_visualizations.py
    with open('spotify_calculations_1.csv', 'w', newline='') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerows(sorted_list_1)
    csvFile.close()  
    print("Manipulation #1 Ended")



# This function is very similar to sportify_manipulations_1, except that it grabs track number and popularity data.
# Year and Average Popularity (Out of 100) are the columns on the outputted CSV file
def spotify_manipulations_2():
    print("Preforming Manipulation #2...")


    # Connect to database
    conn = sqlite3.connect('sql_data.sqlite')
    cur = conn.cursor()
    cur.execute('SELECT track_number, popularity FROM Spotify_Song_Info')

    # Create dictionary and fill list with data
    tracknum_v_pop = {}
    data = []
    for row in cur:
        try:
            data.append(row)
        except:
            print('encoding error')

    # Loop through data to get important information
    for tup in data:
        tracknum = tup [0]
        pop = tup[1]
        if tracknum not in tracknum_v_pop.keys():
            tracknum_v_pop[tracknum] = [pop]
        else:
            tracknum_v_pop[tracknum].append(pop)
    # Finds the avergae of the popularity ratings of all of a user's favorite songs for their given track number
    for item in tracknum_v_pop.items():
        average = sum(item[1])/len(item[1])
        tracknum_v_pop[item[0]] = int(average)

    # Sorts the lsit for easy viewing

    sorted_list_2 = sorted(tracknum_v_pop.items(), key=lambda x: x[0])
    # Outputs a second CSV file for use in spotify_visualizations.py
    with open('spotify_calculations_2.csv', 'w', newline='') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerows(sorted_list_2)
    csvFile.close() 

    # Let the user know what steps to follow next.
    print("Manipulation #2 Ended")
    print("")

# Call functions to run the manipulations
spotify_manipulations_1()
spotify_manipulations_2()