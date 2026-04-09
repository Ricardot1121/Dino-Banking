# ================================
# DINO BANKING - Main Application
# ================================

# Import Flask to create our web app
from flask import Flask

# Create our Flask application
app = Flask(__name__)

# This is our homepage route
# When someone visits "/" they see this
@app.route('/')
def home():
    return 'Welcome to Dino Banking! 🦕'

# This runs our application
if __name__ == '__main__':
    app.run(debug=True)

