import sys
import time
import requests
from datetime import datetime


def run(DOMAIN):
    URL = 'api/current-user/?format=json'
    MONITORING_URL = DOMAIN + URL
    FILENAME = 'results.txt'
    DATETIME_FORMAT = '%d/%m/%Y %H:%M:%S'

    now = datetime.now()

    request_started_at = time.time()
    response = requests.get(MONITORING_URL)
    request_ended_at = time.time()
    worked_at = request_ended_at - request_started_at

    with open(FILENAME, 'a') as the_file:
        message = f'{round(worked_at, 2)}-{now.strftime(DATETIME_FORMAT)}\n'
        the_file.write(message)


if __name__ == "__main__":
    run(sys.argv[1])
