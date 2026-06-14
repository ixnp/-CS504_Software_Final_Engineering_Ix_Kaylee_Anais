# Google Auth Implementation

This is a small example implementation of a web-based application that demonstrates how to use the Google Authenticator app for two-factor authentication.

## Application Description

A server-rendered Flask web application using:

- Flask
- SQLAlchemy for data persistence
- Flask-Login for session management
- Flask-Bcrypt for password hashing
- PyOTP with QR code provisioning for Time-based One-Time Passwords (TOTP)
- Jinja2 templates for the frontend

## Purpose

The purpose of this project is to demonstrate how to implement two-factor authentication in a Flask application. Users can:

- Create an account
- Log in with a username and password
- Enroll in Google Authenticator by scanning a QR code
- Verify their identity using TOTP code
- Access a protected home page after successful authentication

## Sources

The primary reference for this project is:

- Krishna, A. (2023, November 27). _How to Implement Two-Factor Authentication with PyOTP and Google Authenticator in Your Flask App_. freeCodeCamp.org.
  - https://www.freecodecamp.org/news/how-to-implement-two-factor-authentication-in-your-flask-app/

## Technology Stack

- Backend
  - Flask
  - SQLAlchemy
  - Flask-Migrate / Alembic

- Authentication
  - Flask-Login
  - Flask-Bcrypt
  - PyOTP

- Frontend
  - Jinja2 templates
  - WTForms / Flask-WTF

- Configuration
  - python-decouple

## How to Run

1. Install the required packages.

   ```bash
   pip install -r requirements.txt
   ```

2. Create a `.env` file and configure the application.

   Example:

   ```text
   SECRET_KEY=your_secret_key_here
   SQLALCHEMY_DATABASE_URI=sqlite:///site.db
   ```

3. Initialize the database.

   ```bash
   flask db init
   flask db migrate -m "Initial migration"
   flask db upgrade
   ```

4. Start the Flask development server.

   ```bash
   flask run
   ```

5. Open the application in your web browser.

   ```text
   http://127.0.0.1:5000
   ```

## AI Transparency Statement

Generative AI tools were used only to assist with formatting, grammar, spelling, and improving the clarity of the documentation. The implementation, code, design decisions, and technical content are the author's own work or that of (Krishna, 2023)
