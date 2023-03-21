import sqlite3


#Connecting to sqlite
conn = sqlite3.connect('results.db')


#Creating a cursor object using the cursor() method
cursor = conn.cursor()


#Droping STUDENT table if already exists.
cursor.execute("DROP TABLE IF EXISTS STUDENT")

#Creating table as per requirement
sql ='''CREATE TABLE STUDENT(
        FIRST_NAME CHAR(20) NOT NULL,
        LAST_NAME CHAR(20),
        REG_NO CHAR(20) NOT NULL,
        PASSWORD CHAR(20) NOT NULL,
        PHONE_NO CHAR(13) NOT NULL,
        LEVEL CHAR(7) NOT NULL,
        SEMESTER INT NOT NULL,
        SGPA FLOAT,
        CUMGPA FLOAT,
        CUFAILED INT,
        REMARKS CHAR(100))'''
cursor.execute(sql)
print("Table created successfully........")


#remember to add separate values for each semester
#HND 1 FIRST SEMESTER
cursor.execute('''INSERT INTO STUDENT(FIRST_NAME, LAST_NAME, PASSWORD, PHONE_NO, REG_NO, LEVEL, SEMESTER
    ) VALUES ('Ramya', 'Rama Priya', '1234', '09099249445', 'HEEET/ET/2403', 'HND I', 1)''')

cursor.execute('''INSERT INTO STUDENT(FIRST_NAME, LAST_NAME, PASSWORD, PHONE_NO, REG_NO, LEVEL, SEMESTER
    ) VALUES ('Vinay', 'Battacharya', '1234', '07089697590', 'HEEET/ET/2404', 'HND I', 1)''')

cursor.execute('''INSERT INTO STUDENT(FIRST_NAME, LAST_NAME, PASSWORD, PHONE_NO, REG_NO, LEVEL, SEMESTER
    ) VALUES ('Sharukh', 'Sheik', '1234', '09075491532', 'HEEET/ET/2405', 'HND I', 1)''')

cursor.execute('''INSERT INTO STUDENT(FIRST_NAME, LAST_NAME, PASSWORD, PHONE_NO, REG_NO, LEVEL, SEMESTER
    ) VALUES ('Sarmista', 'Sharma', '1234', '08026324732', 'HEEET/ET/2406', 'HND I', 1)''')



#HND 1 SECOND SEMESTER
cursor.execute('''INSERT INTO STUDENT(FIRST_NAME, LAST_NAME, PASSWORD, PHONE_NO, REG_NO, LEVEL, SEMESTER
    ) VALUES ('Ramya', 'Rama Priya', '1234', '09099249445', 'HEEET/ET/2403', 'HND I', 2)''')

cursor.execute('''INSERT INTO STUDENT(FIRST_NAME, LAST_NAME, PASSWORD, PHONE_NO, REG_NO, LEVEL, SEMESTER
    ) VALUES ('Vinay', 'Battacharya', '1234', '07089697590', 'HEEET/ET/2404', 'HND I', 2)''')

cursor.execute('''INSERT INTO STUDENT(FIRST_NAME, LAST_NAME, PASSWORD, PHONE_NO, REG_NO, LEVEL, SEMESTER
    ) VALUES ('Sharukh', 'Sheik', '1234', '09075491532', 'HEEET/ET/2405', 'HND I', 2)''')

cursor.execute('''INSERT INTO STUDENT(FIRST_NAME, LAST_NAME, PASSWORD, PHONE_NO, REG_NO, LEVEL, SEMESTER
    ) VALUES ('Sarmista', 'Sharma', '1234', '08026324732', 'HEEET/ET/2406', 'HND I', 2)''')


#HND 2 FIRST SEMESTER
cursor.execute('''INSERT INTO STUDENT(FIRST_NAME, LAST_NAME, PASSWORD, PHONE_NO, REG_NO, LEVEL, SEMESTER
    ) VALUES ('Ramya', 'Rama Priya', '1234', '09099249445', 'HEEET/ET/2403', 'HND II', 1)''')

cursor.execute('''INSERT INTO STUDENT(FIRST_NAME, LAST_NAME, PASSWORD, PHONE_NO, REG_NO, LEVEL, SEMESTER
    ) VALUES ('Vinay', 'Battacharya', '1234', '07089697590', 'HEEET/ET/2404', 'HND II', 1)''')

cursor.execute('''INSERT INTO STUDENT(FIRST_NAME, LAST_NAME, PASSWORD, PHONE_NO, REG_NO, LEVEL, SEMESTER
    ) VALUES ('Sharukh', 'Sheik', '1234', '09075491532', 'HEEET/ET/2405', 'HND II', 1)''')

cursor.execute('''INSERT INTO STUDENT(FIRST_NAME, LAST_NAME, PASSWORD, PHONE_NO, REG_NO, LEVEL, SEMESTER
    ) VALUES ('Sarmista', 'Sharma', '1234', '08026324732', 'HEEET/ET/2406', 'HND II', 1)''')


#HND 2 SECOND SEMESTER
cursor.execute('''INSERT INTO STUDENT(FIRST_NAME, LAST_NAME, PASSWORD, PHONE_NO, REG_NO, LEVEL, SEMESTER
    ) VALUES ('Ramya', 'Rama Priya', '1234', '09099249445', 'HEEET/ET/2403', 'HND II', 2)''')

cursor.execute('''INSERT INTO STUDENT(FIRST_NAME, LAST_NAME, PASSWORD, PHONE_NO, REG_NO, LEVEL, SEMESTER
    ) VALUES ('Vinay', 'Battacharya', '1234', '07089697590', 'HEEET/ET/2404', 'HND II', 2)''')

cursor.execute('''INSERT INTO STUDENT(FIRST_NAME, LAST_NAME, PASSWORD, PHONE_NO, REG_NO, LEVEL, SEMESTER
    ) VALUES ('Sharukh', 'Sheik', '1234', '09075491532', 'HEEET/ET/2405', 'HND II', 2)''')

cursor.execute('''INSERT INTO STUDENT(FIRST_NAME, LAST_NAME, PASSWORD, PHONE_NO, REG_NO, LEVEL, SEMESTER
    ) VALUES ('Sarmista', 'Sharma', '1234', '08026324732', 'HEEET/ET/2406', 'HND II', 2)''')

print("Records inserted........")

#Retrieving data
cursor.execute('''SELECT * from STUDENT''')

#Fetching 1st row from the table
result = cursor.fetchone();
print(result)

#Fetching 1st row from the table
result = cursor.fetchall();
print(result)



#Droping ADMIN table if already exists.
cursor.execute("DROP TABLE IF EXISTS ADMIN")

#Creating table as per requirement
sql ='''CREATE TABLE ADMIN(
        FIRST_NAME CHAR(20) NOT NULL,
        LAST_NAME CHAR(20),
        PASSWORD INT NOT NULL)'''
cursor.execute(sql)

print("Admin Table created successfully........")

cursor.execute('''INSERT INTO ADMIN(FIRST_NAME, LAST_NAME, PASSWORD)
    VALUES ('Edu', 'John', 123456)''')

cursor.execute('''INSERT INTO ADMIN(FIRST_NAME, LAST_NAME, PASSWORD)
    VALUES ('Victor', 'Bamidele', 12345)''')

print("Admin Records inserted........")

#Retrieving data
cursor.execute('''SELECT * from ADMIN''')


#Fetching all row from the table
result = cursor.fetchall();
print(result)

# Commit your changes in the database
conn.commit()

#Closing the connection
conn.close()
