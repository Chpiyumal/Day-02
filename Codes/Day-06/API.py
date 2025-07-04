import requests
import json
import datetime
import time
import schedule
import pandas as pd

API_URL = "http://api.open-notify.org/iss-now.json"
REPORT_FILE = "iss_location_report.csv"

def fetch_iss_location():
    """Fetch the current ISS location from the Open-Notify API"""
    try:
        response = requests.get(API_URL)
        response.raise_for_status()#Raise an exception for HTTP error
        data = response.json()
        #print(f"{data}")
        return data
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from API: {e}")
        return None
#fetch_iss_location()

def generate_report_entry():

    """Fetch ISS data and append it as a new row to the CSV report. Create the CSV file with header"""

    iss_data = fetch_iss_location()

    if iss_data:
        timestamp = datetime.datetime.fromtimestamp(iss_data['timestamp'])
        laitude = iss_data['iss_position']['latitude']
        longitude = iss_data['iss_position']['longitude']

        print(f"{iss_data}")
        #new_row = pd.DataFrame([{
            #'Timestamp (UTC)' : timestamp,
            #'Latitude': laitude,
            #'Longitude': longitude
        #}])
        
if __name__ == "__main__":
    generate_report_entry()  
