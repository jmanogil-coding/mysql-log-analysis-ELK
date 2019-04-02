# ----------------------------------------------------------------------------------------------------------------------
# test project mysql-log-analysis-ELK

import time
import random
from datetime import datetime
import config
from config import STORED_PROCEDURE_CALLS as SP_CALLS
from database import Database


# random number of milliseconds to wait between databases accesses
def get_time_to_wait():
    return random.randint(1, config.DB_MAX_SECONDS_CALL_INTERVAL * 1000)


# waiting for next access
def wait_for_next(t):
    time.sleep(t / 1000)


# random database access picking next call up from a SQL list in config file
def call_database():
    next_call = random.randint(0, len(SP_CALLS) - 1)
    with Database(config.BD_HOST,
                  config.DB_PORT,
                  config.DB_NAME,
                  config.DB_USER,
                  config.DB_PWD) as my_db:
        my_db.execute_sp(SP_CALLS[next_call][0], SP_CALLS[next_call][1])
        if my_db.last_error_code != 0:
            return f'Error calling: {SP_CALLS[next_call][0]}, Message Error {my_db.last_error_msg}'
        else:
            return f'Calling: {SP_CALLS[next_call][0]}'


# just to track the process
def show_log(msg):
    print(f'{datetime.now()} - {msg}')


def main():

    show_log(f'Starting automatic load: Database {config.DB_NAME}, Host {config.BD_HOST}, '
             f'Port {config.DB_PORT}, Max Call Interval, {config.DB_MAX_SECONDS_CALL_INTERVAL}')
    try:
        # infinite loop until user press Ctrl-C
        while True:

            # between 1 and DB_MAX_SECONDS_CALL_INTERVAL * 1000 milliseconds
            waiting_time = get_time_to_wait()

            # waiting those milliseconds chosen randomly
            wait_for_next(waiting_time)

            # call randomly stored procedures
            last_call_result = call_database()

            show_log(last_call_result)

    except KeyboardInterrupt:
        show_log('Ending automatic load by user')


if __name__ == '__main__':
    main()



