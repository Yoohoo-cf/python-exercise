# Exercises 8.1

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












