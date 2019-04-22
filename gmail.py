from __future__ import print_function
import pickle
import os
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import json
import sys
import time
import sqlite3

#Connects to existing database and creates a table with id and date as headers, ensures that all ids are unique and do not repeat
print("Connecting to Gmail API and adding table to database")

conn = sqlite3.connect('sql_data.sqlite')
cur = conn.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS Gmail_ID_and_Date_Info (id TEXT, date TIMESTAMP, UNIQUE (id))''')

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']

def main():
    """Shows basic usage of the Gmail API.
    Lists the user's Gmail labels.
    """
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # Created automatically when the authorization flow completes for the first time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server()
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('gmail', 'v1', credentials=creds)

    # Call the Gmail API
    # Store the email dictionaries into a list
    
    threads_list = []
    threads = service.users().threads().list(userId='me', maxResults=100).execute().get('threads', [])
    for thread in threads:
        tdata = service.users().threads().get(userId='me', id=thread['id']).execute()
        threads_list.append(tdata)
   

    # Create a loop to find the internalDates
    # Convert the internalDates into date times
    # Retrieve the email id to store in and produce a dictionary where the id is the key and the converted timestamp is the value
    date_dic = {}
    for email in threads_list:
        email_id = email['id']
        internalDate = email['messages'][0]['internalDate']
        dt_object = time.ctime(int(internalDate)//1000)
        date_dic[email_id] = dt_object
    #add id and date to sqlite file
        cur.execute ('INSERT OR IGNORE INTO Gmail_ID_and_Date_Info (id, date) VALUES (?, ?)', (email_id, dt_object))
    conn.commit()



if __name__ == '__main__':
    main()

