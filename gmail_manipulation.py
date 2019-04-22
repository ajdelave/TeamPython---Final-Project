import os
import sys
import json
from json.decoder import JSONDecodeError
import sqlite3
import csv
import sys

#Connect to sqlite and pull the id and dates of each email from the database

print("")
print("Starting Gmail Data Manipulations...")
print("")

conn = sqlite3.connect('sql_data.sqlite')
cur = conn.cursor()
cur.execute('SELECT id, date FROM Gmail_ID_and_Date_Info')

#The program is used to find the average amount of emails recieved per hour out of the past 100 emails recieved
#Use the range function to pul the most recent 100 pieces of data
def Create_Hour_Dic():
    date = {}
    for z in range(100):
        for x in cur:
            hour = x[1]
            if hour[11:13] not in date.keys():
                date[hour[11:13]] = 1
            else:
                date[hour[11:13]] += 1

    return date

#This function converts the dictionary from the Create_Hour_Dic function into a tuple to find the average 
#amount of emails received per hour out of 100
def Find_Avg_Recieved(save_date):
    dates_tuple = list(save_date.items())
    new_dic = {}
    for x in dates_tuple:
        hour = x[0]
        average = x[1]/100
        if hour not in new_dic.keys():
            new_dic[hour] = average
    return new_dic

#Sorts the dictionary to see easier
#Creates a CSV File using the sorted dictionary created in the Find_Avg_Recieved function
#The hour of the day will be the first column and the average amount of emails recieved will be the second column
def Create_CSV(find_avg):
    sorted_list = sorted(find_avg.items(), key=lambda x: x[0])

    with open('email_averages.csv', 'w', newline='') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerow(["Hour of Day", "Average out of 100"])
        writer.writerows(sorted_list)

    csvFile.close()

print("Gmail Manipulations Completed")

save_date = Create_Hour_Dic()
find_avg = Find_Avg_Recieved(save_date)
Create_CSV(find_avg)
