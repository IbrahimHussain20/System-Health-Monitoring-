import requests
import logging
from datetime import datetime

logging.basicConfig(filename='app_health.log', level=logging.INFO, format='%(asctime)s %(message)s')

APP_URL = 'http://your_application_url.com'

def check_app_health():
    try:
        response = requests.get(APP_URL)
        if response.status_code == 200:
            logging.info('Application is up and running.')
        else:
            logging.warning(f'Application returned a non-200 status code: {response.status_code}')
    except requests.exceptions.RequestException as e:
        logging.error(f'Application is down. Error: {e}')

if __name__ == "__main__":
    check_app_health()
