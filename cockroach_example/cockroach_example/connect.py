import psycopg2
import sys
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import plotly.express as px  # (version 4.7.0)
import plotly.graph_objects as go

import dash  # should be used to create graphs for result and datavisualization
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

# Parameters for connection 
param_dic = {
    "host"      : "localhost",
    "database"  : "bank",
    "user"      : "member",
    "password"  : "blackwings"
}

def connect(params_dic):
    """ Connect to the PostgreSQL database server """
    conn = None
    try:
        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(**params_dic)
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        sys.exit(1) 
    print("Connection successful")
    return conn

def postgresql_to_dataframe(conn, select_query, column_names):
    """
    Tranform a SELECT query into a pandas dataframe
    """
    cursor = conn.cursor()
    try:
        cursor.execute(select_query)
    except (Exception, psycopg2.DatabaseError) as error:
        print("Error: %s" % error)
        cursor.close()
        return 1
    
    # Naturally we get a list of tupples
    tupples = cursor.fetchall()
    cursor.close()
    
    # We just need to turn it into a pandas dataframe
    df = pd.DataFrame(tupples, columns=column_names)
    return df


    # Connect to the database
# Connect to the database
conn = connect(param_dic)

column_names = ["id","email","company","title","education","yearsExp","baseSalary","bonuses","gender","race", "state"]
# Execute the "SELECT *" query
df = postgresql_to_dataframe(conn, "select * from cockroach_example_user", column_names)

#Next we can do data visualisation using plotly and dash

conn.close()