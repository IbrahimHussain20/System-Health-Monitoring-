import re
from collections import Counter

LOG_FILE_PATH = '/path/to/web/server/logfile.log'

def analyze_logs():
    with open(LOG_FILE_PATH, 'r') as file:
        logs = file.readlines()

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

    most_common_ips = Counter(ip_addresses).most_common(5)
    most_common_pages = Counter(pages).most_common(5)
    error_404_count = status_codes.count('404')

    print(f'Most common IP addresses: {most_common_ips}')
    print(f'Most common pages: {most_common_pages}')
    print(f'Number of 404 errors: {error_404_count}')

if __name__ == "__main__":
    analyze_logs()
