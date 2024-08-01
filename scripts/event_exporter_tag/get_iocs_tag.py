import csv
from pymisp import PyMISP
import datetime

# Don't use in production
import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def main():
    # Replace values accordly
    misp_url = 'https://misp-url.com'
    misp_key = 'misp-token' # https://misp-url.com/auth_keys/index -> Add auth key
    misp_verifycert = False  # Set to True if you want to verify SSL certificates
    tags = ['companytag1', 'companytag2'] # Change to company export tags
    start_date = datetime.datetime(2023, 7, 1) # Date to start getting events
    end_date = datetime.datetime.now() # Date to stop getting events

    distribution_map = {
        '0': 'Your organization only',
        '1': 'This community only',
        '2': 'Connected communities',
        '3': 'All communities',
        '4': 'Sharing group',
        '5': 'Inherit Event'
    }

    # Initialize the MISP instance
    misp = PyMISP(misp_url, misp_key, misp_verifycert)

    # Fetch all events based on the reserved tags
    events = misp.search(controller='events', tags=tags)

    # Open a CSV file for writing
    with open('output.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Date', 'Category', 'Type', 'Value', 'Distribution'])

        for event in events:
            event_info = event['Event']
            date = event_info['date']
            orgc_name = event_info['Orgc']['name']
            distribution = distribution_map.get(event_info.get('distribution', 'Unknown'), 'Unknown')
            distribution = distribution.replace('\n', ' ').replace('\r', ' ').strip()

            for attribute in event_info['Attribute']:
                category = attribute['category']
                attr_type = attribute['type']
                value = attribute['value']
                value = value.replace('\n', ' ').replace('\r', ' ').replace(';', ',').strip()

                writer.writerow([date, category, attr_type, value, distribution])

if __name__ == '__main__':
    main()
