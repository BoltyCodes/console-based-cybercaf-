import sys
import sqlite3
import random
import pandas as pd  
import matplotlib.pyplot as plt




try:
 conn = sqlite3.connect('Project\SQLite_Python.db')
 sqlite_create_table_query = '''CREATE TABLE SqliteDb_developers (
	                                name TEXT NOT NULL,
                                    password TEXT NOT NULL)'''
	
 cursor = conn.cursor()
 print("Successfully connnected to SQLite")
 cursor.execute(sqlite_create_table_query)
 conn.commit()
 cursor = conn.cursor()
	
 
except sqlite3.Error as error:
 print("Error while creating a sqlite table", error)
finally:
	 if conn:
	  False


print("Welcome to Cyber Cafe! Hope you have a great time!")

data = cursor.execute('SELECT * FROM SqliteDb_developers')
output = list(data.fetchall())


def login_account():
    name = input("Enter your username:")
    password = input("Enter your password:")
    

   
    data = cursor.execute('SELECT * FROM SqliteDb_developers')
    output = data.fetchall()
    
    length = len(output)
    
    for i in range(length):
        if name == output[i][0] and password == output[i][1]:
            print("Access granted.")
            project_code()
            
            break
        
    else:
        print("Access denied.")
        

    


def register_account():
    print("Welcome to CyberCafe, sign up now")
    name = input("Enter a username (make sure it is between 5-15 letters):")

    if len(name) < 5:
        print("Too small")
        register_account()
    elif len(name) > 15:
        print("Too big")
        register_account()
    
    password = input("Enter a password (make sure it is more than 6:")
    if len(password) < 6:
        print("Too small")
        register_account()
    
   
    

    username_sql_query = f'''insert into SqliteDb_developers(name,password) values("{name}","{password}")'''
    cursor.execute(username_sql_query)
    conn.commit()
    login = input("Would you like to login now? (y/n): ")   
    if login == 'y' or "Y": 
        login_account() 
          
        
    
    elif login == 'n' or "N":
        pass


    
def project_code():
    print("Welcome to CyberCafe")
    print("In order to use the pc you have to subscibe for hours. 10 AED for 1 hour.")
    options = int(input("1. Add hours. \n 2. View hours \n 3. Admin_users \n Click options 1, 2 or 3)"))
    if options == 1:
        addhours()
    elif options == 2:
        viewhours()
    
    elif options == 3:
        veri = int(input("what is the code: "))
        if veri == 123456:
            admin_login()
        
        else:
            print("Access denied")
    else:
        print("invalid input, use 1, 2 or 3")
        project_code()

def addhours(): 
    name = input("Enter your username:")
    pwd = input("Enter your password:")
    

    

    length = len(output)
    
    for i in range(length):
        if name == output[i][0] and pwd == output[i][1]:
            amount = int(input("How many hours do you want to add? 10 AED for 1 hour:"))
            if amount > 0:
                hours_query = f'''insert into hours(name, password, hours) values("{name}","{pwd}", "{amount}")'''
                
                print('***********BILL***********\n',amount * 10, "\n\n<---- This is your final bill. Pay cashier.")
                cursor.execute(hours_query)
                conn.commit()
                pc_chair = ["seat 1", "seat 2", "seat 3", "seat 4", "seat 5", "seat 6", "seat 7", "seat 8", "seat 9", "seat 10"]
                seat = random.choice(pc_chair)
                print(f"You may go to {seat}. Enter your login credentials there! You have {amount} hours to play!\n Thank you for using CyberCafe!\n")
                z = cursor.execute('''SELECT * FROM hours''')
                print(z.fetchall())
                
                

def viewhours():
    name = input("Enter your username:")
    pwd = input("Enter your password:")
    insert_query = cursor.execute('''SELECT * FROM hours''')
    lest = insert_query.fetchall()
    for i in lest:
        if i[0] == name and i[1] == pwd:
            print(f" You have {i[2]} hours to play!\n Thank you for using CyberCafe!")




    
    

#Adnin functions
def adminadd():
      table_query = cursor.execute('SELECT * FROM hours')
      data = table_query.fetchall()
    
      user = input("Enter the username of the user you want to add hours to:")
      pwd = input("Enter password of the user")
      for i in data:
        if i[0] == user and i[1] == pwd:
         hours = int(input("How many hours do you want to add?"))
         if hours > 0:
            cursor.execute(f'''INSERT INTO hours (name, password, hours) VALUES("{user}", "{pwd}", "{hours}")''')
            conn.commit()
            print(f"{hours} hours added")

def admin_view_hours():
    tb_query = cursor.execute('SELECT * FROM hours')
    lst = tb_query.fetchall()
    choice = int(input("How would you like to view this data? \n 1. BarGraph \n 2. line chart \n 3. dataframe"))
    if choice == 1:
        names, values = [], []
        for idx in lst:
        names.append(idx[0])
        values.append(0 if idx[2] == None else idx[2])

        names = np.array(names)
        values = np.array(values)

        plt.bar(names, values)
        plt.xlabel("Users")
        plt.ylabel("Hours in account")
        plt.title("Hours in account")
        sys.exit()
       
    elif choice == 2:
        plt.plot(names, values)
        plt.xlabel("Users")
        plt.ylabel("Hours in account")
        sys.exit()
    
    elif choice == 3:
      dr = pd.DataFrame(values, names)
      print(dr)
    
    
    
        
def add_user():
    name = input("Enter the username of the user you want to add:")
    pwd = input("Enter the password of the user")
    cursor.execute(f'''INSERT INTO SqliteDb_developers (name, password) VALUES("{name}", "{pwd}")''')
    cursor.execute(f'''INSERT INTO hours (name, password) VALUES("{name}", "{pwd}")''')
    conn.commit()
    print(f"{name} added")

def delete_user():
    query = cursor.execute("SELECT * FROM hours")
    output = query.fetchall()
    print(output)
    name = input("Enter the username of the user you want to delete:")
    pwd = input("Enter the password of the user:")

    for i in output:   
     if i[0] == name and i[1] == pwd:
            
        
      cursor.execute(f'''DELETE FROM hours WHERE name = "{name}" AND password = "{pwd}"''')
      conn.commit()
      print(f"{name} deleted")
        
    
        
def admin_login():
    options = int(input("What would you like to access: \n 1. Add hours. \n 2. View hours. \n 3. Add user. \n 4. Delete user. 6. Exit. \n"))
    

    if options == 1:
        adminadd()

    elif options == 2:
        admin_view_hours()

    elif options == 3:
        add_user()
    elif options == 4:
        delete_user()
    elif options == 5:
        sys.exit()
    else:
        print("Invalid input, use 1-6")





    
accounts = input("Do you have an account? (y/n): ")

if accounts == "y" or accounts == "Y":
    login_account()

elif accounts == "n" or accounts == "N":
    register_account()

else:
    print("Error, please choose one of the options")
