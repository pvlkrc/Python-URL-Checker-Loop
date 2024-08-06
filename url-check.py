import requests
import time
from datetime import datetime


# Change URL variable to one you want to check
url = "https://data-warehouse.zone"

while True:
    # There needs to be created url-check.log text file in same folder
    f = open("url-check.log", "a")
    try:
        now = datetime.now()
        response = requests.get(url)
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S  -  ")
        if response.status_code == 200:
            print(dt_string,"Connected")
            f.write(dt_string+"Connected"+"\n")
        else:
            print(dt_string,f"Error. Status code: {response.status_code}")
            f.write(dt_string+"Error. Status code: {response.status_code}"+"\n")
    except requests.exceptions.RequestException as e:
        print(dt_string,f". Error: {e}")
        f.write(dt_string+"Error. Status code: {response.status_code}"+"\n")
    f.close()
    # Time delay in seconds between checks
    time.sleep(5)
