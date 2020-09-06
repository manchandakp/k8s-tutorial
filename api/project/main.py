from flask import Flask, json, request
from flask_cors import CORS
import psycopg2 as pg2
from psycopg2.extras import RealDictCursor
from project import config

app = Flask(__name__)
CORS(app)

@app.route("/registrations", defaults={'registrationId': None}, methods=['GET'])
@app.route("/registrations/<int:registrationId>", methods=['GET'])
def getRegistrations(registrationId = None):
    sql = """SELECT registration_id, person_name, person_email, person_phone, registration_datetime 
             FROM registrations
          """
    
    if registrationId is not None:
        sql = sql + f" WHERE registration_id = {registrationId}"
    
    connectDB()
    cursor.execute(sql)
    rows = cursor.fetchall()
    
    return app.response_class(response=json.dumps(rows),
                                status=200 if len(rows) > 0 else 204,
                                mimetype='application/json')

@app.route("/registrations", methods=["POST"])
def saveRegistrations():
    if request.method == "POST":
        inputData = request.get_json(force = True)
        
        sql = f"""INSERT INTO registrations (person_name, person_email, person_phone)
                VALUES ('{inputData["person_name"] if "person_name" in inputData else ""}', 
                '{inputData["person_email"] if "person_email" in inputData else ""}', 
                '{inputData["person_phone"] if "person_phone" in inputData else ""}')
                """
        
        connectDB()
        cursor.execute(sql)
        conn.commit()

        return app.response_class(response=json.dumps({'Status':'Success'}),
                                    status=201,
                                mimetype='application/json')

@app.after_request
def after_request(response):
  response.headers.add('Access-Control-Allow-Origin', '*')
  response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
  response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
  return response

def connectDB():
    global conn
    global cursor

    conn = pg2.connect(host = config.POSTGRES_HOST,
                        port = config.POSTGRES_PORT,
                        database = config.POSTGRES_DB,
                        user = config.POSTGRES_USER,
                        password = config.POSTGRES_PASSWORD)
    
    cursor = conn.cursor(cursor_factory=RealDictCursor)
