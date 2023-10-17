# Exercises Module 8.1

"""
Write a program that asks the user to enter the ICAO code of an airport.
The program fetches and prints out the corresponding airport name and
location (town) from the airport database used on this course.
The ICAO codes are stored in the ident column of the airport table.
"""

import mysql.connector

connection = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database="exercises",
    user="dbuser",
    password="707708",
    autocommit=True
)

def get_airport_by_icao(ICAO_code):
    sql = "SELECT ID, name, municipality FROM airports"
    sql += " WHERE ident='" + ICAO_code + "'"
    print(sql)
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    if cursor.rowcount > 0:
        for row in result:
            print(f"The airport you are finding is: {row[1]}. It is located at {row[2]}")
    return


ICAO_code = input('Enter an ICAO code to find the airport: ')
get_airport_by_icao(ICAO_code)












