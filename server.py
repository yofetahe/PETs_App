from flask import Flask, render_template, session, request, redirect
from mysqlconnection import connectToMySQL

app = Flask('__home__')
my_sql = connectToMySQL("flask_pets")

@app.route("/")
def index():
    my_sql = connectToMySQL("flask_pets")
    lst = my_sql.query_db("select * from pets")
    return render_template("index.html", petsList=lst)

@app.route("/insert_pets", methods=['POST'])
def insert_pets():
    my_sql = connectToMySQL("flask_pets")
    query = "INSERT INTO pets(name, type, create_at) VALUES(%(name)s, %(type)s, NOW())"    
    data = {
        "name": request.form['pet_name'],
        "type": request.form['pet_type']
    }
    id = my_sql.query_db(query, data)
    print(id)
    return redirect("/")

@app.route("/delete_pet", methods=['POST'])
def delete_pets():
    query = "DELETE FROM pets WHERE pet_id = %(pet_id)s"
    data = {
        "pet_id": request.form['pet_id']
    }
    print(request.form['pet_id'])
    my_sql.query_db(query, data)
    return redirect("/")

@app.route("/update_form", methods=['GET'])
def get_update_form():
    return render_template("update.html")

@app.route("/update_pet", methods=['POST'])
def update_pet():
    return redirect("/")

if __name__=='__main__':
    app.run(debug=True)