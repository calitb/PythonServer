from bottle import get, run, response
import json

import mysql.connector
import os

@get('/')
def root():
  response.content_type = 'application/json'
  result = {"status":"ok"}
  return json.dumps(result)

@get('/query')
def root():
  response.content_type = 'application/json'

  mydb = mysql.connector.connect(
    host= 'mysql',
    user= os.environ['MYSQL_USER'],
    passwd= os.environ['MYSQL_PASSWORD'],
    database= os.environ['MYSQL_DATABASE']
  )

  sql_select_Query = "select id, name from user"
  cursor = mydb.cursor()
  cursor.execute(sql_select_Query)
  records = cursor.fetchall()

  result = []
  for row in records:
    result.append( {'id': row[0], 'name': row[1]} )

  result = {"status":"ok","data":result}
  return json.dumps(result)

if __name__ == "__main__":
  run(host="0.0.0.0", port=8080, debug=True, reloader=True)
