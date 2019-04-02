# ----------------------------------------------------------------------------------------------------------------------
# Config file to test project mysql-log-analysis-ELK

# database and table on which procedure calls are executed
BD_HOST = '127.0.0.1'
DB_PORT = 3306
DB_NAME = 'learning'
DB_USER = 'learning-user'
DB_PWD = 'learning'

# ----------------------------------------------------------------------------------------------------------------------
# stored procedures are called with an interval: 1 - DB_MAX_SC_CALL_INTERVAL * 1000
DB_MAX_SECONDS_CALL_INTERVAL = 2

# ----------------------------------------------------------------------------------------------------------------------
# database calls to test it

STORED_PROCEDURE_CALLS = [
    ['learning.usp_person_ins', ['Ros', 'Aaren', '1995-02-23', ]],
    ['learning.usp_person_sel', [1, ]],
    ['learning.usp_person_sel', [0, ]],
    ['learning.usp_person_sel', [0, ]],
    ['learning.usp_person_sel', [1, ]],
    ['learning.usp_person_sel', [0, ]],
    ['learning.usp_person_sel', [0, ]],
    ['learning.usp_person_upd', [1, 'Ros', 'Linsey', '1970-06-30', ]],
    ['learning.usp_person_upd', [1, 'Ros', 'Linsey', '1970-06-30', ]],
    ['learning.usp_person_upd', [1, 'Ros', 'Linsey', '1970-06-30', ]],
    ['learning.usp_person_upd', [1, 'Ros', 'Linsey', '1970-06-30', ]],
    ['learning.usp_person_upd', [1, 'Ros', 'Linsey', '1970-06-30', ]],
    ['learning.usp_person_upd', [1, 'Ros', 'Linsey', '1970-06-30', ]],
    ['learning.usp_person_upd', [1, 'Ros', 'Linsey', '1970-06-30', ]],
    ['learning.usp_person_del', [0, ]],
    ['learning.usp_person_del', [0, ]]
]

# ----------------------------------------------------------------------------------------------------------------------
