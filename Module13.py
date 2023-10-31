#1
from flask import Flask, request

app = Flask(__name__)

num=int(input('Enter a number:'))
def is_prime(num):
    if num % num==0 and num%1==0:
        return True
    if num<=1:
        return False
@app.route('/prime_number/<int:number>', methods=['GET'])
def check_prime(num):
    is_prime_result = is_prime(num)
    response = {
        "Number": num,
        "isPrime": is_prime_result  }
    return response

app.run(host='127.0.0.1', port=5000)


#2
from flask import Flask,request
app = Flask(__name__)
airport_db={"ICAO":"EFHK",
            "Name":"Helsinki-Vantaa Airport",
            "Location":"Helsinki"}
@app.route('/airport/<icao>',methods=['GET'])
def airport_infor(icao):
    if icao in airport_db:
        airport_infor={'ICAO':icao,
                       'Name':airport_db['Name'],
                       'Location':airport_db['Location']
                      }
        return airport_infor

app.run(host='127.0.0.1', port=5000)


