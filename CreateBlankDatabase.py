import sqlite3
import sys
import os

if __name__ == '__main__':

##    if len(sys.argv) != 2:
##        raise ValueError ("Only takes one argument, file name of new database")
##
##    filename = sys.argv[1]
    
    filename = 'test.sqlite'
    print(filename)
    connection = sqlite3.connect(filename)
    c = connection.cursor()
    try:
        c.execute('DROP TABLE people')
    except:
        pass

    try:
        c.execute('DROP TABLE events')
    except:
        pass

    try:
        c.execute('DROP TABLE talks')
    except:
        pass
    
    
    people = """CREATE TABLE people(
                id INTEGER PRIMARY KEY,
                fname VARCHAR(30),
                lname VARCHAR(30),
                organisation VARCHAR(100),
                title VARCHAR(100));
            """

    events = """CREATE TABLE events(
                id INTEGER PRIMARY KEY,
                name VARCHAR(100),
                date DATE);

            """

    talks = """CREATE TABLE talks(
               id INTEGER PRIMARY KEY,
               name VARCHAR(200),
               speaker INTEGER,
               event INTEGER,
               rating INTERGER);

            """
    c.execute(people)
    c.execute(events)
    c.execute(talks)

