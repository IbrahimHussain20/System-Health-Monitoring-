# System-Health-Monitoring-
Accuknox DevOps Trainee Practical Assessment 

Sure! Here are the Python scripts for each of the described tasks:

### 1. System Health Monitoring Script
This script monitors CPU usage, memory usage, disk space, and running processes.

```python
import psutil
import logging
from datetime import datetime

# Set up logging
logging.basicConfig(filename='system_health.log', level=logging.INFO, format='%(asctime)s %(message)s')

# Thresholds
CPU_THRESHOLD = 80  # in percent
MEMORY_THRESHOLD = 80  # in percent
DISK_THRESHOLD = 80  # in percent

def check_system_health():
    # Check CPU usage
    cpu_usage = psutil.cpu_percent(interval=1)
    if cpu_usage > CPU_THRESHOLD:
        logging.warning(f'High CPU usage detected: {cpu_usage}%')

    # Check memory usage
    memory_info = psutil.virtual_memory()
    memory_usage = memory_info.percent
    if memory_usage > MEMORY_THRESHOLD:
        logging.warning(f'High memory usage detected: {memory_usage}%')

    # Check disk usage
    disk_info = psutil.disk_usage('/')
    disk_usage = disk_info.percent
    if disk_usage > DISK_THRESHOLD:
        logging.warning(f'High disk usage detected: {disk_usage}%')

    # Check running processes
    processes = [p.info for p in psutil.process_iter(attrs=['pid', 'name', 'username'])]
    logging.info(f'Running processes: {processes}')

if __name__ == "__main__":
    check_system_health()
```

### 2. Automated Backup Solution
This script backs up a specified directory to a remote server using `rsync`. Adjust the remote server details and directory paths as needed.

```python
import subprocess
import logging
from datetime import datetime

# Set up logging
logging.basicConfig(filename='backup.log', level=logging.INFO, format='%(asctime)s %(message)s')

# Backup configuration
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
```

### 3. Log File Analyzer
This script analyzes web server logs for common patterns.

```python
import re
from collections import Counter

LOG_FILE_PATH = '/path/to/web/server/logfile.log'

def analyze_logs():
    with open(LOG_FILE_PATH, 'r') as file:
        logs = file.readlines()

    # Patterns to search for
    ip_pattern = re.compile(r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
    status_pattern = re.compile(r'\" \d{3} ')
    page_pattern = re.compile(r'\"GET (.*?) HTTP/')

    ip_addresses = []
    status_codes = []
    pages = []

    for log in logs:
        ip_match = ip_pattern.search(log)
        status_match = status_pattern.search(log)
        page_match = page_pattern.search(log)

        if ip_match:
            ip_addresses.append(ip_match.group())
        if status_match:
            status_codes.append(status_match.group().strip('" '))
        if page_match:
            pages.append(page_match.group(1))

    # Analyze patterns
    most_common_ips = Counter(ip_addresses).most_common(5)
    most_common_pages = Counter(pages).most_common(5)
    error_404_count = status_codes.count('404')

    # Print report
    print(f'Most common IP addresses: {most_common_ips}')
    print(f'Most common pages: {most_common_pages}')
    print(f'Number of 404 errors: {error_404_count}')

if __name__ == "__main__":
    analyze_logs()
```

### 4. Application Health Checker
This script checks the uptime of an application by verifying HTTP status codes.

```python
import requests
import logging
from datetime import datetime

# Set up logging
logging.basicConfig(filename='app_health.log', level=logging.INFO, format='%(asctime)s %(message)s')

# Application URL
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
```

These scripts provide basic functionality for each of the requested tasks. Adjust paths, thresholds, and other details according to your specific requirements.
