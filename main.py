# Exercises Module 8.3

"""
Write a program that asks the user to enter the ICAO codes of two airports.
The program prints out the distance between the two airports in kilometers.
The calculation is based on the airport coordinates fetched from the database.
Calculate the distance using the geopy library: https://geopy.readthedocs.io/en/stable/.
Install the library by selecting View / Tool Windows / Python Packages in your PyCharm IDE,
write geopy into the search field and finish the installation.
"""

import mysql.connector
from geopy import distance

connection = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database="exercises",
    user="dbuser",
    password="707708",
    autocommit=True
)

def get_airport_coordinates_by_icao(ICAO_code):
    sql = "SELECT ID, latitude_deg, longitude_deg FROM airports"
    sql += " WHERE ident='" + ICAO_code + "'"
    print(sql)
    cursor = connection.cursor()
    cursor.execute(sql)
    coordinates = cursor.fetchall()
    if coordinates:
        return coordinates
    else:
        print("Could not find this ICAO_code in database")
        return



ICAO_code1 = input('Enter a first ICAO code to find the first airport address: ')
ICAO_code2 = input('Enter a second ICAO code to find the second airport address: ')

coords1 = get_airport_coordinates_by_icao(ICAO_code1)
coords2 = get_airport_coordinates_by_icao(ICAO_code2)

print(distance.distance(coords1, coords2).kilometers)









