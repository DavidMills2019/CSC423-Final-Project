import sqlite3
import pandas as pd

# Connects to an existing database file in the current directory
# If the file does not exist, it creates it in the current directory
db_connect = sqlite3.connect('test.db')

# Instantiate cursor object for executing queries
cursor = db_connect.cursor()

# String variable for passing queries to cursor
clinic = """
    CREATE TABLE Clinic(
    clinicNo VARCHAR(3) 
                        PRIMARY KEY 
                        NOT NULL 
                        UNIQUE 
                        CHECK(clinicNo GLOB '[A-Z][0-9][0-9]'),
    clinicName VARCHAR(256)
                        NOT NULL,
    address VARCHAR(256)
                        NOT NULL
                        UNIQUE,
    phoneNumber INT
                        NOT NULL
                        UNIQUE  
                        CHECK(LENGTH(phoneNumber) = 10),
    managedBy VARCHAR(3)
                        NOT NULL,
    FOREIGN KEY(managedBy) REFERENCES Staff(staffNo)
                        ON DELETE SET NULL
                        ON UPDATE CASCADE
    );
    """

staff = """
    CREATE TABLE Staff(
    staffNo VARCHAR(3)
                        PRIMARY KEY
                        NOT NULL
                        UNIQUE
                        CHECK(staffNo GLOB '[A-Z][0-9][0-9]'),
    name VARCHAR(256)
                        NOT NULL,
    address VARCHAR(256),
    phoneNumber INT
                        CHECK(LENGTH(phoneNumber) = 10),
    dOB DATE
                        CHECK(dOB < '2022-12-08'),
    position VARCHAR(256)
                        NOT NULL,
    salary INT,
    clinicNo VARCHAR(3)
                        NOT NULL,
    FOREIGN KEY(clinicNo) REFERENCES Clinic 
                        ON DELETE SET NULL
                        ON UPDATE CASCADE
    );
"""

owner = """
    CREATE TABLE Owner(
    ownerNo VARCHAR(3)
                        PRIMARY KEY
                        NOT NULL
                        UNIQUE
                        check(ownerNo GLOB '[A-Z][0-9][0-9]'),
    name VARCHAR(256)
                        NOT NULL,
    address VARCHAR(256),
    phoneNumber INT
                        CHECK(LENGTH(phoneNumber) = 10)
    );
"""

pet = """
    CREATE TABLE Pet(
    petNo VARCHAR(3)
                        PRIMARY KEY
                        NOT NULL
                        UNIQUE
                        check(petNo GLOB '[A-Z][0-9][0-9]'),
    name VARCHAR(256)
                        NOT NULL,
    dOB DATE
                        CHECK(dOB < '2022-12-08'),
    species VARCHAR(256),
    breed VARCHAR(256),
    color VARCHAR(256),
    clinicNo VARCHAR(3)
                        NOT NULL,
    ownerNo VARCHAR(3)
                        NOT NULL,
    FOREIGN KEY(clinicNo) REFERENCES Clinic 
                        ON DELETE SET NULL
                        ON UPDATE CASCADE,
    FOREIGN KEY(ownerNo) REFERENCES Owner
                        ON DELETE SET NULL
                        ON UPDATE CASCADE
    );
"""

examination = """
    CREATE TABLE Examination(
    examNo VARCHAR(3)
                        PRIMARY KEY
                        NOT NULL
                        UNIQUE
                        check(examNo GLOB '[A-Z][0-9][0-9]'),
    chiefComplient VARCHAR(256),
    description VARCHAR(256),
    dateSeen DATE
                        CHECK(dateSeen < '2022-12-08'),
    actionsTaken VARCHAR(256),
    staffNo
                        NOT NULL,
    petNo
                        NOT NULL,
    FOREIGN KEY(staffNo) REFERENCES Staff
                        ON DELETE SET NULL
                        ON UPDATE CASCADE,
     FOREIGN KEY(petNo) REFERENCES Pet
                        ON DELETE SET NULL
                        ON UPDATE CASCADE
    );
"""


# Execute query, the result is stored in cursor
cursor.execute(clinic)
cursor.execute(staff)
cursor.execute(owner)
cursor.execute(pet)
cursor.execute(examination)

#------------------------ INSERTS FOR CLINIC --------------------------

clinic = """
    INSERT INTO Clinic
    VALUES(
        "C01",
        "Pawsome Clinic Miami",
        "3787 Thomas Ave Miami, FL 33133",
        7817402661,
        "S01"
    );
    """
cursor.execute(clinic)

clinic = """
    INSERT INTO Clinic
    VALUES(
        "C02",
        "Pawsome Clinic Boston",
        "193 Newbridge Street Hingham, MA 02043",
        3392365308,
        "S02"
    )
    """
cursor.execute(clinic)

clinic = """
    INSERT INTO Clinic
    VALUES(
        "C03",
        "Pawsome Clinic Los Angeles",
        "55 Newbury Street Los Angeles, CA 51234",
        7325983162,
        "S03"
    )
    """
cursor.execute(clinic)

clinic = """
    INSERT INTO Clinic
    VALUES(
        "C04",
        "Pawsome Clinic Coral Gables",
        "6240 SW 88th Street Coral Gables, FL 33166",
        1158029160,
        "S04"
    )
    """
cursor.execute(clinic)

clinic = """
    INSERT INTO Clinic
    VALUES(
        "C05",
        "Pawsome Clinic Dallas",
        "67 Adams Drive Dallas, TX 75001",
        6125903573,
        "S05"
    )
    """
cursor.execute(clinic)


#------------------------ INSERTS FOR STAFF --------------------------

staff = """
    INSERT INTO Staff
    VALUES(
        "S01",
        "John Cena",
        "50 Pine Road Miami, FL 33133",
        7817964291,
        '2001-01-22',
        "Manager",
        93000,
        "C01"
        );
"""
cursor.execute(staff)

staff = """
    INSERT INTO Staff
    VALUES(
        "S02",
        "Katie Farrell",
        "58 Foxrun Drive Bolingbrook, IL 60440",
        4135259062,
        '1993-06-15',
        "Manager",
        87000,
        "C02"
        );
"""
cursor.execute(staff)

staff = """
    INSERT INTO Staff
    VALUES(
        "S03",
        "Bob Sagget",
        "8137 Oxford Street Xenia, OH 45385",
        3529660174,
        '1988-03-01',
        "Manager",
        62000,
        "C03"
        );
"""
cursor.execute(staff)


staff = """
    INSERT INTO Staff
    VALUES(
        "S04",
        "Cameron Johnson",
        "268 Amerige Street Doylestown, PA 18901",
        6394201964,
        '2002-11-18',
        "Manager",
        120000,
        "C04"
        );
"""
cursor.execute(staff)


staff = """
    INSERT INTO Staff
    VALUES(
        "S05",
        "Mary Poppins",
        "9113 Beaver Ridge Drive Worcester, MA 01604",
        7817964291,
        '2000-03-18',
        "L",
        96000,
        "C05"
        );
"""
cursor.execute(staff)

staff = """
    INSERT INTO Staff
    VALUES(
        "S06",
        "Harry Lewis",
        "241 Marvon Road West Bend, WI 53095",
        9303383274,
        '1976-09-17',
        "Veterinarian",
        230000,
        "C01"
        );
"""
cursor.execute(staff)

staff = """
    INSERT INTO Staff
    VALUES(
        "S07",
        "David Letterman",
        "969 Mayflower Street Wasilla, AK 99654",
        6522550433,
        '1992-06-10',
        "Veterinary Assistant",
        32000,
        "C01"
        );
"""
cursor.execute(staff)

staff = """
    INSERT INTO Staff
    VALUES(
        "S08",
        "James Bond",
        "9304 West Ridgewood Street Arvada, CO 80003",
        3187925431,
        '2000-03-18',
        "Veterinary Technician",
        152000,
        "C01"
        );
"""
cursor.execute(staff)

#------------------------ INSERTS FOR OWNER --------------------------

owner = """
    INSERT INTO Owner
    VALUES(
        "O01",
        "Jeffrey Bubbles",
        "510 Fawn Street Temple Hills, MD 20748",
        6270848737 
    );
"""
cursor.execute(owner)

owner = """
    INSERT INTO Owner
    VALUES(
        "O02",
        "Courtney Lawson",
        "7 Canal Street Fayetteville, NC 28303",
        3371947770 
    );
"""
cursor.execute(owner)

owner = """
    INSERT INTO Owner
    VALUES(
        "O03",
        "Tom Brady",
        "8409 Marsh Drive Villa Park, IL 60181",
        6919385756
    );
"""
cursor.execute(owner)

owner = """
    INSERT INTO Owner
    VALUES(
        "O04",
        "Kelly Smith",
        "665 Alderwood Street Baldwin, NY 11510",
        4985693185 
    );
"""
cursor.execute(owner)

owner = """
    INSERT INTO Owner
    VALUES(
        "O05",
        "Aaron Nesmith",
        "9314 Fifth Drive Matawan, NJ 07747",
        3749689110
    );
"""
cursor.execute(owner)

#------------------------ INSERTS FOR PET --------------------------

pet = """
    INSERT INTO Pet
    Values(
        "P01",
        "Rex",
        '2012-09-19',
        "Dog",
        "German Shepherd",
        "Brown",
        "C04",
        "O01"
    );
"""
cursor.execute(pet)

pet = """
    INSERT INTO Pet
    Values(
        "P02",
        "Lucy",
        '2014-03-01',
        "Cat",
        "Bombay Cat",
        "Black",
        "C04",
        "O01"
    );
"""
cursor.execute(pet)

pet = """
    INSERT INTO Pet
    Values(
        "P03",
        "Hopps",
        '2020-03-22',
        "Rabbit",
        "American Fuzzy Hop",
        "White",
        "C02",
        "O05"
    );
"""
cursor.execute(pet)

pet = """
    INSERT INTO Pet
    Values(
        "P04",
        "Roxy",
        '2018-13-12',
        "Dog",
        "Poodle",
        "Orange",
        "C01",
        "O03"
    );
"""
cursor.execute(pet)

pet = """
    INSERT INTO Pet
    Values(
        "P05",
        "Todd",
        '2016-12-21',
        "Guinea Pig",
        "Teddy Guinea Pig",
        "Brown",
        "C03",
        "O04"
    );
"""
cursor.execute(pet)


#------------------------ INSERTS FOR EXAMINATION --------------------------

examination = """
    INSERT INTO Examination
    Values(
        "E01",
        "Patient had an ear infection",
        "Patient was checked in both ears and given medicaton to take for infection",
        '2022-08-23',
        "a treatment was perscribed",
        "S04",
        "P01"
    );
"""
cursor.execute(examination)

examination = """
    INSERT INTO Examination
    Values(
        "E02",
        "Annual Checkup",
        "Patient's height and weight were measured, vaccination shots were given",
        '2021-11-30',
        "tests were ordered, treatment was perscribed",
        "S04",
        "P02"
    );
"""
cursor.execute(examination)

examination = """
    INSERT INTO Examination
    Values(
        "E03",
        "Patient had not been eating",
        "Patient was checked for stomach issues, perscribed special food",
        '2019-02-25',
        "tests were ordered, treatment was perscribed",
        "S02",
        "P03"
    );
"""
cursor.execute(examination)

examination = """
    INSERT INTO Examination
    Values(
        "E04",
        "Patient had an upset stomach",
        "Patient was checked for stomach bacteria or parasites",
        '2022-04-01',
        "tests were ordered",
        "S06",
        "P04"
    );
"""
cursor.execute(examination)

examination = """
    INSERT INTO Examination
    Values(
        "E05",
        "Patient had been limping",
        "X-Ray scans were given, found fracture in front right leg",
        '2020-05-16',
        "tests were ordered",
        "S03",
        "P05"
    );
"""
cursor.execute(examination)

#Printing out all relations
#CLINIC
print("------------------------- DATABASE RELATIONS -------------------------")
print("Clinic")
print("--------------------------------------------------------")

clinicRelation = """
    SELECT *
    FROM Clinic
"""
cursor.execute(clinicRelation)

# Extract column names from cursor
column_names = [row[0] for row in cursor.description]

# Fetch data and load into a pandas dataframe
table_data = cursor.fetchall()
df = pd.DataFrame(table_data, columns=column_names)

# Examine dataframe
print(df)
print(" ")

#STAFF
print("Staff")
print("--------------------------------------------------------")

staffRelation = """
    SELECT *
    FROM Staff
"""
cursor.execute(staffRelation)

# Extract column names from cursor
column_names = [row[0] for row in cursor.description]

# Fetch data and load into a pandas dataframe
table_data = cursor.fetchall()
df = pd.DataFrame(table_data, columns=column_names)

# Examine dataframe
print(df)
print(" ")

#OWNER
print("Owner")
print("--------------------------------------------------------")

ownerRelation = """
    SELECT *
    FROM Owner
"""
cursor.execute(ownerRelation)

# Extract column names from cursor
column_names = [row[0] for row in cursor.description]

# Fetch data and load into a pandas dataframe
table_data = cursor.fetchall()
df = pd.DataFrame(table_data, columns=column_names)

# Examine dataframe
print(df)
print(" ")

#PET
print("Pet")
print("--------------------------------------------------------")

petRelation = """
    SELECT *
    FROM Pet
"""
cursor.execute(petRelation)

# Extract column names from cursor
column_names = [row[0] for row in cursor.description]

# Fetch data and load into a pandas dataframe
table_data = cursor.fetchall()
df = pd.DataFrame(table_data, columns=column_names)

# Examine dataframe
print(df)
print(" ")

#EXAMINATION
print("Examination")
print("--------------------------------------------------------")

examinationRelation = """
    SELECT *
    FROM Examination
"""
cursor.execute(examinationRelation)

# Extract column names from cursor
column_names = [row[0] for row in cursor.description]

# Fetch data and load into a pandas dataframe
table_data = cursor.fetchall()
df = pd.DataFrame(table_data, columns=column_names)

# Examine dataframe
print(df)
print(" ")



#---------------------------------- QUERIES ------------------------------------------------
print("------------------------- QUERIES -------------------------")

#-------------- QUERY 1 ------------------
print("------------------ QUERY 1 ------------------")

#List the name position, and salary of staff members who make more than $100,000 annually. order by salary descending

query = """
    SELECT name, position, salary
    FROM Staff S
    WHERE S.salary > 100000
    ORDER BY S.salary DESC;
"""
cursor.execute(query)

# Extract column names from cursor
column_names = [row[0] for row in cursor.description]

# Fetch data and load into a pandas dataframe
table_data = cursor.fetchall()
df = pd.DataFrame(table_data, columns=column_names)

# Examine dataframe
print(df)
print(" ")



#-------------- QUERY 2 ------------------
print("------------------ QUERY 2 ------------------")

#List the names of all of the owners who own dogs

query = """
    SELECT O.name Owner_Name
    FROM Owner O, Pet P
    WHERE O.ownerNo = P.ownerNo AND p.species = "Dog";
"""
cursor.execute(query)

# Extract column names from cursor
column_names = [row[0] for row in cursor.description]

# Fetch data and load into a pandas dataframe
table_data = cursor.fetchall()
df = pd.DataFrame(table_data, columns=column_names)

# Examine dataframe
print(df)
print(" ")



#------------------ QUERY 3 ------------------
print("------------------ QUERY 3 ------------------")

#List the names and phone numbers of all staff that manage a branch and the name and phone number of the branch they manage
query = """
    SELECT C.clinicName Clinic_Name, C.phoneNumber Clinic_Phone_Number, S.name Staff_Name, S.phoneNumber Staff_Phone_Number  
    FROM Clinic C, Staff S
    WHERE C.managedBy = S.staffNo;
"""
cursor.execute(query)

# Extract column names from cursor
column_names = [row[0] for row in cursor.description]

# Fetch data and load into a pandas dataframe
table_data = cursor.fetchall()
df = pd.DataFrame(table_data, columns=column_names)

# Examine dataframe
print(df)
print(" ")



#------------------ QUERY 4 ------------------
print("------------------ QUERY 4 ------------------")

#List the dates and chiefComplients of all examinations done in the last 2 years. also list the name of pet that the examination was done on and the name of the owner that owns that pet
query = """
    SELECT O.name Owner_Name, P.name Pet_Name, E.chiefComplient Chief_Complient, E.dateSeen Date_Seen
    FROM Owner O, Examination E, Pet P
    WHERE O.ownerNo = P.ownerNo AND P.petNo = E.petNo AND E.dateSeen >= '2020-12-08'
"""
cursor.execute(query)

# Extract column names from cursor
column_names = [row[0] for row in cursor.description]

# Fetch data and load into a pandas dataframe
table_data = cursor.fetchall()
df = pd.DataFrame(table_data, columns=column_names)

# Examine dataframe
print(df)
print(" ")


#------------------ QUERY 5 ------------------
print("------------------ QUERY 5 ------------------")

#Find the average salary of all staff members that work at a clinic with the word "street" in the address
query = """
    SELECT AVG(S.salary)
    FROM Staff S, Clinic C
    WHERE S.clinicNo = C.clinicNo AND C.address LIKE '%Street%'
"""
cursor.execute(query)

# Extract column names from cursor
column_names = [row[0] for row in cursor.description]

# Fetch data and load into a pandas dataframe
table_data = cursor.fetchall()
df = pd.DataFrame(table_data, columns=column_names)

# Examine dataframe
print(df)
print(" ")


# Commit any changes to the database
db_connect.commit()

# Close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
db_connect.close()
