'''
    https://www.c-sharpcorner.com/article/creating-a-crudcreate-retrieveupdate-and-delete-desktop-application-using-pyt2/
'''

import tkinter as tk  
import mysql.connector 

## db connection 
connection_config_dict = {
        'user': 'root',
        'password': 'root1234',
        'host': 'localhost',
        'database': 'quizdb',
        'raise_on_warnings': True,
        'use_pure': True, #'use_pure': False, #False , meaning the C extension is used
        'autocommit': True,
        'pool_size': 5
    }
db_connection = None
## ------------------------
password = tk.StringVar() #Password variable

def db_connect(): #{
    global connection_config_dict, db_connection
    print("{} {}".format(connection_config_dict['user'], connection_config_dict['host']))
    try:
        db_connection = mysql.connector.connect(**connection_config_dict)
    except Error as e:
        print("Error while connecting to MySQL", e)
    #finally:
    #    if db_connection.is_connected():
            #cursor.close()
           # db_connection.close()
    #        print("MySQL connection is closed")    

#}
def db_disconnect(): #{
    if db_connection.is_connected():
        print("connection still exists")
        db_connection.close()
        print("connection closed")
    else:
        print("connection terminate")
#}

def db_select():#{
    try:
        #sql_select_Query = "select * from users"
        cursor = db_connection.cursor()
        #cursor.execute(sql_select_Query)
        sql_select_Query = """select * from users where usruid = %s"""
        # set variable in query
        cursor.execute(sql_select_Query, ('anand1973',))
        # get all records
        records = cursor.fetchall()
        print("Total number of rows in table: ", cursor.rowcount)
        print("mysql string {}".format(cursor.statement))
    except mysql.connector.Error as error:
        print("Failed to create table in MySQL: {}".format(error))    

#}
root = tk.Tk()
## window design
root.title="Login App"
root.geometry("500x400+100+20") # window.geometry("widthxheight+XPOS+YPOS") #(all values are in pixels)
mylabel = tk.Label(text = "Quiz program ")
mylabel.grid(column=3,row=1)
tk.Label(
    root,
    text='Enter Email', 
    #bg='#9FD996'
).grid(row=3, column=0)
tk.Label(
    root,
    text='Enter Password',
    #bg='#9FD996'
).grid(row=4, column=0)
tk.Entry(root).grid(row=3, column=1)
tk.Entry(root, textvariable=password, show='*').grid(row=4, column=1)


#-----------------
db_connect()
db_select()
if db_connection.is_connected():
    db_disconnect()    
root.mainloop()