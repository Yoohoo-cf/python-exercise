# Exercises Module 8.2

"""
Write a program that asks the user to enter the area code (for example FI)
and prints out the airports located in that country ordered by airport type.
For example, Finland has 65 small airports, 15 helicopter airports and so on.
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

def getairportsbyareacode(area_code):
    sql = "SELECT ID, name, type, COUNT(*) AS count FROM airports"
    sql += " WHERE iso_country='" + area_code + "' GROUP BY type ORDER BY count desc"
    print(sql)
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    if cursor.rowcount > 0:
        for row in result:
            print(f"The iso_country of {area_code} has {row[3]} {row[2]} airports")
    return


area_code = input('Enter an area code to find the corresponding airports types(eg: FI): ')
getairportsbyareacode(area_code)






