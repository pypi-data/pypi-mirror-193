import pandas as pd
import datetime
import pymssql
import socket
import os


# basic utility to print current timestamp and message
def pt(text, indent=False):
    if indent:
        print(f'                     {text}')
    else:
        print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + f': {text}')


# coverts file name to full extension if being run on the VM (gb5-li-bpsn001)
def zfile(file):
    if socket.gethostname() == 'gb5-li-bpsn001':
        file = os.path.join(os.path.dirname(__file__), file)
    return file


# function to get data from sql
def sql_get_data(query=None, file=None, server='AAO-LI-AHCRP002.Thehutgroup.LOCAL', username=None, password=None):
    # print statements for query configurations & contents
    def print_query_statement(server, username, query, file=None):
        if username == None:
            username = '<Windows Authentication>'
        if len(query) > 50:
            query = query[:50] + '...'

        pt(f'Executing SQL Query')
        pt(f'SQL Server: {server}', indent=True)
        pt(f'SQL Username: {username}', indent=True)
        if file != None:
            pt(f'Query File: {file}', indent=True)
        pt(f'Query Preview: <{query}>', indent=True)

    # extract query from file (if applicable)
    if file != None:
        query = open(zfile(file), 'r', encoding='utf-8-sig').read()

    # get results
    print_query_statement(server, username, query, file)
    starting_timestamp = datetime.datetime.now()
    connection = pymssql.connect(server=server, user=username, password=password)
    df = pd.read_sql(sql=query, con=connection)
    ending_timestamp = datetime.datetime.now()
    runtime = ending_timestamp - starting_timestamp
    rows, columns = len(df), df.shape[1]
    pt(f'Dataframe Completed from SQL ({columns} columns x {rows} rows)')
    pt(f'Runtime: {runtime}', indent=True)
    return df


# function to execute sproc in sql
def sql_exec_sproc(sproc, server='AAO-LI-AHCRP002.Thehutgroup.LOCAL', username=None, password=None):
    # print statements for query configurations & contents
    def print_query_statement(server, username, sproc):
        if username == None:
            username = '<Windows Authentication>'
        pt(f'Executing SQL Stored Procedure')
        pt(f'SQL Server: {server}', indent=True)
        pt(f'SQL Username: {username}', indent=True)
        pt(f'Stored Procedure: <{sproc}>', indent=True)

    # run sproc
    print_query_statement(server, username, sproc)
    starting_timestamp = datetime.datetime.now()
    connection = pymssql.connect(server=server, user=username, password=password)
    cursor = connection.cursor()
    cursor.execute(f'EXEC {sproc}')
    connection.commit()
    connection.close()
    ending_timestamp = datetime.datetime.now()
    runtime = ending_timestamp - starting_timestamp
    pt(f'Stored Procedure executed successfully')
    pt(f'Runtime: {runtime}', indent=True)


