#1
import mysql.connector

def getAirport_code(ICAO_code):
    sql=sql = "SELECT name,location,ident FROM airport,game"
    sql+=" WHERE ident='"+ICAO_code+"'"
    print(sql)
    cursor=connection.cursor()
    cursor.execute(sql)
    result=cursor.fetchall()
    if cursor.rowcount>0:
        for row in result:
            print(f"The airport name is {row[0]},location is {row[1]}")
        return

#main program
connection = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='root',
    password='20231001',
    autocommit=True)

ICAO_code=input("Enter the ICAO code you want to search:")
getAirport_code(ICAO_code)


#2


