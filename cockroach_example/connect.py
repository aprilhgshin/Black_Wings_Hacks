import psycopg2
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Connection parameters, yours will be different
param_dic = {
    "host"      : "127.0.0.1",
    "database"  : "test",
    "user"      : "postgres",
    "password"  : "mMhatrARMIE12$"
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
conn = connect(param_dic)

column_names = ["id","email","company","title","education","yearsExp","baseSalary","bonuses","gender","race"]
# Execute the "SELECT *" query
df = postgresql_to_dataframe(conn, "select * from users_revised", column_names)
tb1 = df[(df['gender']=='male') & (df['title']=='Associate Software Engineer')]
tb2 = df.sort_values('yearsExp')

plt.figure()

plt.scatter(df['baseSalary'], df['yearsExp'])  

plt.ylabel("Years of Experience")
plt.xlabel("base salary")
plt.title("base salary VS years of experience ")

plt.show()