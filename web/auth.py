# auth.py

from flask import Blueprint, render_template, request, flash

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Handle login logic here
        flash('Login logic will be implemented later', 'info')
    return render_template('login.html')

@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        # Handle sign-up logic here
        flash('Sign-up logic will be implemented later', 'info')
    return render_template('sign_up.html')
