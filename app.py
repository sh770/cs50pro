from flask import Flask, redirect, render_template, request, url_for
from waitress import serve
import json

app = Flask(__name__)


# קריאת משתמשים מהקובץ JSON
def read_users_from_file():
    with open('users.json', 'r') as file:
        data = json.load(file)
        return data['users']

# פונקציה לכתיבת משתמש חדש לקובץ JSON
def write_user_to_file(username, password):
    users = read_users_from_file()
    new_user = {'username': username, 'password': password}
    users.append(new_user)
    
    with open('users.json', 'w') as file:
        json.dump({'users': users}, file)    


@app.route("/", methods=['GET', 'POST'])
def login():        
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        users = read_users_from_file()
        valid_credentials = any(user['username'] == username and user['password'] == password for user in users)

        if valid_credentials:
            return redirect(url_for('home'))
    
    # אם הכניסה לדף היא GET או אם אין מידע נכנס, נציג את הדף המתאים
    return render_template("login.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/home")
def home():
    return render_template("index.html")

@app.route("/logout",methods=['GET'])
def logout():
    return render_template("login.html")

@app.route("/register", methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # קריאת המשתמשים מהקובץ
        users = read_users_from_file()

        # בדיקה אם המשתמש כבר קיים
        if any(user['username'] == username for user in users):
            return render_template("register.html", error="Username already exists")

        # הוספת המשתמש החדש
        write_user_to_file(username, password)

        return redirect(url_for('home'))

    return render_template("register.html")





if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)
    # app.run(host='0.0.0.0')
    # serve(app, host='0.0.0.0', port=5000)
    # serve(app, host='0.0.0.0', port=8081)
    # app.run(debug=True)