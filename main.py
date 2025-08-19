from flask import Flask, request, render_template, redirect
import mysql.connector

app = Flask(__name__)

db = mysql.connector.connect(
    host="localhost",
    user="root",     
    password="123456789", 
    database="test_db"  
)

cursor = db.cursor()

@app.route('/', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        full_name = request.form['full_name']
        email = request.form['email']
        password = request.form['password']
        
        try:
            sql = "INSERT INTO users (full_name, email, password) VALUES (%s, %s, %s)"
            val = (full_name, email, password)
            cursor.execute(sql, val)
            db.commit()
        except mysql.connector.Error:
            pass  
        return redirect('/')
    return render_template('signup.html')

if __name__ == "__main__":
    app.run(debug=True)
