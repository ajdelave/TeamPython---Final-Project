import matplotlib
import matplotlib.pyplot as plt
import sqlite3
import json
import os
import csv
import sys

def Create_Visualization_Dic():
    # Reads the CSV file and stores it into a dictionary, hour is the key and the average amount of emails per hour is the value
    Visual_dic = {}
    with open('email_averages.csv', mode='r') as csv_file:
        reader = csv.reader(csv_file)
        for row in reader:
            if row[0] not in Visual_dic:
                Visual_dic[row[0]] = row[1]
            else:
                print ('There is an error creating the Visual_dic')
    return Visual_dic

def Create_Visualization_Graph(create_dictionary):
    #Creates a lineplot using the dictionary created in the Create_Visualization_Dic function
    x_axis = list(create_dictionary.keys())
    y_axis = list(create_dictionary.values())

    x_axis = x_axis[1:]
    y_axis = y_axis[1:]
   
    plt.plot(x_axis, y_axis, color = 'orange')
    plt.xlabel('Hour of the Day (in Army Time)')
    plt.ylabel('Average Amount of Emails per 100')
    plt.title('Average Amount of Emails per Hour of the Day Out of the Last 100')
    
    plt.savefig('Gmail_Visualization.png')

    plt.show()



    
            


create_dictionary = Create_Visualization_Dic()
Create_Visualization_Graph(create_dictionary)