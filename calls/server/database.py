import psycopg2
import logging
from call import Call

connection = psycopg2.connect(database="calls", user="admin", password="admin", host="127.0.0.1", port="5432")
logging.warning('Database opened successfully')


def create_call(call_object: Call):
    """Create call objects in database"""
    cursor = connection.cursor()
    sql = f"INSERT INTO call (caller_number, callee_number, start_call, end_call, type_call) VALUES " \
          f" ('{call_object.caller_number}', '{call_object.callee_number}', '{call_object.start_call}', '{call_object.end_call}', '{call_object.type_call}')"
    cursor.execute(sql)
    connection.commit()
    logging.info('the call was inserted')


def remove_call(identifier):
    """Remove objects in databse"""
    cursor = connection.cursor()
    sql = f"DELETE FROM call WHERE id = {identifier}"
    cursor.execute(sql)
    connection.commit()
    logging.info('the call was removed')


def get_all_and_by_type(parameters):
    """Get calls with pagination and be able to filter by type"""
    cursor = connection.cursor()
    page_current = int(parameters['page_current'])
    records_per_page = int(parameters['records_per_page'])
    type_call = None
    if "type" in parameters:
        type_call = parameters['type']
    offset = (page_current - 1) * records_per_page
    sql = " SELECT id, caller_number, callee_number, start_call, end_call, type_call"
    sql += " FROM call"
    if type_call:
        sql += f" WHERE type_call = upper('{type_call}')"
    sql += " ORDER BY id"
    sql += " LIMIT " + str(records_per_page)
    sql += " OFFSET " + str(offset)+";"
    cursor.execute(sql)
    record_set = cursor.fetchall()
    list_calls = []
    for row in record_set:
        list_calls.append(Call(row[1], row[2], row[3], row[4], row[5], row[0]))
    logging.info('get call by type')
    return list_calls


def get_all():
    """Get all elements to generate statistics"""
    cursor = connection.cursor()
    sql = " SELECT id, caller_number, callee_number, start_call, end_call, type_call"
    sql += " FROM call"
    cursor.execute(sql)
    print(sql)
    record_set = cursor.fetchall()
    list_calls = []
    for row in record_set:
        list_calls.append(Call(row[1], row[2], row[3], row[4], row[5]))
    logging.info('get call statistics')
    return list_calls
