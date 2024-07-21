import subprocess
import logging
from datetime import datetime

logging.basicConfig(filename='backup.log', level=logging.INFO, format='%(asctime)s %(message)s')

SOURCE_DIR = '/path/to/source/directory'
REMOTE_DIR = 'user@remote_server:/path/to/remote/directory'

def backup_directory():
    try:
        result = subprocess.run(['rsync', '-avz', SOURCE_DIR, REMOTE_DIR], check=True, capture_output=True)
        logging.info(f'Backup successful: {result.stdout}')
    except subprocess.CalledProcessError as e:
        logging.error(f'Backup failed: {e.stderr}')

if __name__ == "__main__":
    backup_directory()
