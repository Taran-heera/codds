#!/usr/bin/env python
"""Create admin user with correct bcrypt password hashing"""
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'backend'))

import bcrypt
from datetime import datetime
from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['codds']

username = 'admin'
email = 'admin@codds.com'
password = 'AdminPassword123'

# Check if admin exists
existing = db.users.find_one({'username': username})
if existing:
    print(f"Admin user '{username}' already exists!")
    print(f"Deleting old admin user...")
    db.users.delete_one({'username': username})

# Hash password using bcrypt (same as app does)
hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

# Create admin document
admin_doc = {
    'username': username,
    'email': email,
    'password': hashed_password,
    'role': 'admin',
    'created_at': datetime.utcnow(),
    'style_profile': {},
    'analysis_count': 0
}

# Insert into MongoDB
result = db.users.insert_one(admin_doc)

print(f"✅ Admin user created successfully!")
print(f"   ID: {result.inserted_id}")
print(f"   Username: {username}")
print(f"   Password: {password}")
print(f"   Email: {email}")
print(f"   Role: admin")
print(f"\n📝 Login with:")
print(f"   Username: admin")
print(f"   Password: AdminPassword123")
print(f"\n🔐 Hashed password stored: {hashed_password.decode()}")
