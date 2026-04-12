# ================================
# DINO BANKING - Main Application
# ================================

# Import Flask and tools we need
from flask import Flask, render_template, request, redirect, url_for

# Create our Flask application
app = Flask(__name__)

# Homepage redirects to login
@app.route('/')
def home():
    return redirect(url_for('login'))

# Login route
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Get what user typed
        username = request.form['username']
        password = request.form['password']
        # Checking everything works
        print(f"Username: {username}, Password: {password}")
        return 'Login successful!'
    return render_template('login.html')

# Register Route
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Get what user typed
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        username = request.form['username']
        password = request.form['password']
        # Checking everything works
        print(f"First Name: {first_name}, Last Name: {last_name}, Username: {username}, Password: {password}")
        return 'Registration successful!'
    return render_template('register.html')


# This ALWAYS goes last - runs the application
if __name__ == '__main__':
    app.run(debug=True)