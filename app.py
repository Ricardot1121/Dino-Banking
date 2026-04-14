# ================================
# DINO BANKING - Main Application
# ================================

# Import Flask and tools we need
from flask import Flask, render_template, request, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
import random



# Create our Flask application
app = Flask(__name__)

# Database configuration - creates a file called dino_banking.db
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///dino_banking.db'
app.config['SECRET_KEY'] = 'dinobanking123'

# Initialize database and bcrypt
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

# ================================
# USER MODEL - our database table
# ================================
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    account_number = db.Column(db.String(10), unique=True)
    routing_number = db.Column(db.String(9), default='031000053')
    checking_balance = db.Column(db.Float, default=0.0)
    savings_balance = db.Column(db.Float, default=0.0)

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
        
        # Find user in database
        user = User.query.filter_by(username=username).first()
        
        # Check if user exists and password matches
        if user and bcrypt.check_password_hash(user.password, password):
            # Password matched! Save user id in session so we remember who is logged in
            session['user_id'] = user.id
            # Redirect to dashboard - no need to pass user_id in URL anymore, session handles it
            return redirect(url_for('dashboard'))
        else:
            return 'Invalid username or password'
            
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

        # Hash the password for security
        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')

        # Generate random account number
        account_number = str(random.randint(1000000000, 9999999999))

        # Create new user object
        new_user = User(
            first_name=first_name,
            last_name=last_name,
            username=username,
            password=hashed_password,
            account_number=account_number
        )

        # Save to database
        db.session.add(new_user)
        db.session.commit()

        return redirect(url_for('login'))

    return render_template('register.html')

# This will go to dashboard once user is logged in
@app.route('/dashboard')
def dashboard():
    # Check if user is logged in by looking for user_id in session
    # If not found, send them back to login page
    if 'user_id' not in session:
        return redirect(url_for('login'))
    
    # Get the full user object from database using the session user_id
    user = User.query.get(session['user_id'])
    
    # Send user data to dashboard template
    return render_template('dashboard.html', user=user)

# Here is where the user can log out - we will clear the session to log them out.
@app.route('/logout', methods=['POST'])
def logout():
    # Clear the session to log the user out
    session.clear()
    return redirect(url_for('login'))

# This ALWAYS goes last - runs the application
if __name__ == '__main__':
    # Create database tables if they don't exist
    with app.app_context():
        db.create_all()
    app.run(debug=True)