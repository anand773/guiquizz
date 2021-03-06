## Tkniter grid system
# https://www.pythontutorial.net/tkinter/tkinter-grid/
# pip install mysql-connector-python
'''
The current recommendation is to use python -m pip, where python is the version of Python you would like to use. This is the recommendation because it works across all versions of Python, and in all forms of virtualenv. For example:

# The system default python:
$ python -m pip install fish

# A virtualenv's python:
$ .env/bin/python -m pip install fish

# A specific version of python:
$ python-3.6 -m pip install fish

Previous answer, left for posterity:

Since version 0.8, Pip supports pip-{version}. You can use it the same as easy_install-{version}:

$ pip-2.5 install myfoopackage
$ pip-2.6 install otherpackage
$ pip-2.7 install mybarpackage

EDIT: pip changed its schema to use pipVERSION instead of pip-VERSION in version 1.5. You should use the following if you have pip >= 1.5:

$ pip2.6 install otherpackage
$ pip2.7 install mybarpackage

Check https://github.com/pypa/pip/pull/1053 for more details

Tools for a programmer
Having professional experience in development of various applications on different Web based Application and Client Server
Application. Strong understanding of Spring,Spring LDAP, Spring Security, GWT(Google Web Tool), Ext- GWT,
SOAP Technology (Apache Axis, Apache CXF RS,WS), Thrift, Java web Start,Hibernate, Ajax, Portal, Portlet, 
Jersey Restful Services, Java OSGI Frame, Shibboleth Single Sing on Architecture, Core Java, Struts, Swing, and 
J2EE Technologies like JSP, Servlet, JDBC and Java Beans, EJB (Both Sesssion and Entity Bean), Android Mobile Development, 
Apache Kafka. Service Mesh, Microservice Architecture. Hybrid Mobile development using Ionic Frame work. 
Sound knowledge of Front End Java frame work like Angular 6 and React. • Sound knowledge of integrating 
SSO Circle Single Sign On, ADFS integration. 

'''
import tkinter as tk
from tkinter import ttk ## ttk Theamed Tkinter widgets new widgets

import time
import mysql.connector
import random



## database related infomation 
## https://pynative.com/python-mysql-database-connection/
db_Info = None
try:
    connection_config_dict = {
        'user': 'root',
        'password': 'root1234',
        'host': 'localhost',
        'database': 'quizdb',
        'raise_on_warnings': True,
        'use_pure': False,
        'autocommit': True,
        'pool_size': 5
    }
    connection = mysql.connector.connect(**connection_config_dict)

    if connection.is_connected():
        ## global db_Info
        db_Info = connection.get_server_info()
        print("Connected to MySQL Server version ", db_Info)
        cursor = connection.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("Your connected to database: ", record)

except Error as e:
    print("Error while connecting to MySQL", e)
finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")


# root windows
root = tk.Tk()
root.title("Quiz Program")
root.geometry("500x350") ## width x height
root.resizable(0,0)

# configure the grid
root.columnconfigure(0,weight=1) # 0th column width weigtage = 1
root.columnconfigure(1,weight=3) # 1th column width weigtage = 3 times of the col 0

## define command binding functions
def btnlogin_clicked():
    print('btnlogin clicked')
    ## get the database and check the existance of the user
    try:
        connection_config_dict = {
            'user': 'root',
            'password': 'root1234',
            'host': 'localhost',
            'database': 'quizdb',
            'raise_on_warnings': True,
            'use_pure': False,
            'autocommit': True,
            'pool_size': 5
        }
        connection = mysql.connector.connect(**connection_config_dict)
        """
        *************************** 4. row ***************************
        userno: 4
        username: Ramesh Kumar
        usruid: ramesh1995
        pword: ramesh1234
        email: ramesh@gmail.com
        birthday: 1995-04-12
        gender: M
            role: U
        """
        #sql_select_Query = "select * from users"
        cursor = connection.cursor()
        #cursor.execute(sql_select_Query)
        sql_select_Query = """select * from users where usruid = %s"""
        # set variable in query
        cursor.execute(sql_select_Query, (username_entry,))
        # get all records
        records = cursor.fetchall()
        print("Total number of rows in table: ", cursor.rowcount)

        print("\nPrinting each row")
        for row in records:
            print("Id = ", row[0], )
            print("Name = ", row[1])
            print("Price  = ", row[2])
            print("Purchase date  = ", row[3], "\n")


    except mysql.connector.Error as error:
        print("Failed to create table in MySQL: {}".format(error))
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

# populate the windows

# username
username_label = ttk.Label(root,text="User Name :")
username_label.grid(column=0, row=0, sticky=tk.W, padx=5, pady=5)
## The sticky option specifies which edge of the cell the widget should stick to.
# W West or Left Center ref: the link placed at top of file

username_entry  = ttk.Entry(root)
username_entry.grid(column=1, row=0, sticky=tk.W, padx=5,pady=5)

# password
password_label = ttk.Label(root, text="Password:")
password_label.grid(column=0, row=1, sticky=tk.W, padx=5, pady=5)

password_entry = ttk.Entry(root,  show="*")
password_entry.grid(column=1, row=1, sticky=tk.W, padx=5, pady=5)

# login button
login_button = ttk.Button(root, text="Login",command=btnlogin_clicked)
login_button.grid(column=1, row=3, sticky=tk.E, padx=5, pady=5)
##login_button.pack() #This geometry manager organizes widgets in blocks before placing them in the parent widget.
## not need as it is already packed by grid geometry manager


if __name__ == "__main__":
    # start the window show
    root.mainloop()