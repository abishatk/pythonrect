import pymysql
from app import app
from config import mysql
from flask import jsonify
from flask import flash, request


#Creating record in company and address table

@app.route('/create/join', methods=['POST'])
def company_address():
    try:        
        _json = request.json
        Company_name = _json['company_name']
        Year = _json['year_established']
        Type = _json['type']
        #Company_id = _json['company_id']
        Street_name = _json['street_name']
        City = _json['city']
        _Country = _json['Country']	
        if Company_name and Year and Type  and Street_name and City and _Country and request.method == 'POST':
            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)		
            Q1 = "INSERT INTO company(company_name,year_established,type) VALUES(%s, %s, %s)"
            data = (Company_name, Year, Type)            
            cursor.execute(Q1, data)
            conn.commit()
            last_id = cursor.lastrowid
            Q2 = "INSERT INTO address(company_id,street_name,city,Country) VALUES(%s, %s, %s,%s)"
            data3 = (last_id, Street_name,City,_Country)            
            cursor.execute(Q2, data3)
            conn.commit()
            respone = jsonify('Details of company added Successfully!!')
            respone.status_code = 200
            return respone
        else:
            return showMessage()
    except Exception as e:
        print(e)
    finally:
        cursor.close() 
        conn.close() 


#READ ALL RECORDS FROM TABLE COMPANY     
@app.route('/comp')
def comp():
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT company.company_id,company.company_name, company.year_established, company.type,address.street_name,address.city,address.Country FROM company INNER JOIN address ON company.company_id=address.company_id")
        comp_details = cursor.fetchall()
        respone = jsonify(comp_details)
        respone.status_code = 200
        return respone
    except Exception as e:
        print(e)
    finally:
        cursor.close() 
        conn.close() 



#UPDATE A RECORD IN TABLE COMPANY

@app.route('/update/comp', methods=['PUT'])
def update_company():
    try:
        _json = request.json
        Id = _json['company_id']
        Company_name = _json['company_name']
        Year = _json['year_established']
        Type = _json['type']
        StreetName=_json['street_name']
        City=_json['city']
        _Country=_json['Country']
        
        if Company_name and Year and Type  and StreetName and City and _Country and request.method == 'PUT':
            Query="UPDATE company,address SET company.company_name= %s,company.year_established=%s,company.type=%s,address.street_name=%s,address.city=%s,address.Country=%s WHERE company.company_id=address.company_id AND company.company_id=%s"			
            data =  (Company_name, Year, Type,StreetName,City,_Country,Id)
            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)
            cursor.execute(Query, data)
            conn.commit()
            respone = jsonify('Company items updated successfully!')
            respone.status_code = 200
            return respone
        else:
            return showMessage()
    except Exception as e:
        print(e)
    finally:
        cursor.close() 
        conn.close()

# DELETE RECORD FROM COMPANY TABLE
@app.route('/comp/<int:company_id>', methods=['DELETE'])
def delete_comp(company_id):
	try:
		conn = mysql.connect()
		cursor = conn.cursor()
		cursor.execute("DELETE FROM company WHERE company_id =%s", (company_id,))
		conn.commit()
		respone = jsonify('Table deleted successfully!')
		respone.status_code = 200
		return respone
	except Exception as e:
		print(e)
	finally:
		cursor.close() 
		conn.close()
       
     
@app.errorhandler(404)
def showMessage(error=None):
    message = {
        'status': 404,
        'message': 'Record not found: ' + request.url,
    }
    respone = jsonify(message)
    respone.status_code = 404
    return respone
        
if __name__ == "__main__":
    app.run(host='0.0.0.0', port = int("8800"),debug=True)