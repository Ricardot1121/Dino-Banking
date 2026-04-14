# ================================
# Create Admin User Script
# Run this once to create the admin account
# ================================

from app import app, db, User, bcrypt

with app.app_context():
    # Check if admin already exists to avoid duplicates
    existing_admin = User.query.filter_by(username='admin').first()
    
    if existing_admin:
        print('Admin already exists!')
    else:
        # Create admin user with is_admin set to True
        admin = User(
            first_name='Admin',
            last_name='Dino',
            username='admin',
            password=bcrypt.generate_password_hash('admin123').decode('utf-8'),
            is_admin=True
        )
        db.session.add(admin)
        db.session.commit()
        print('Admin created successfully!')