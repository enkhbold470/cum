# C.U.M - Centralized User Management

A modern, secure, and efficient user management system built with Flask and HTMX.

## Features

- User registration and authentication
- Profile management
- Admin dashboard
- Role-based access control
- Modern UI with Bootstrap 5
- HTMX for dynamic interactions
- Secure password handling
- Email verification (optional)

## Requirements

- Python 3.10
- Flask
- Flask-SQLAlchemy
- Flask-Login
- Flask-WTF
- Flask-Migrate
- python-dotenv
- email-validator
- Werkzeug

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/cum.git
cd cum
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up environment variables:
Create a `.env` file in the root directory with the following variables:
```
SECRET_KEY=your-secret-key
DATABASE_URL=sqlite:///cum.db
MAIL_SERVER=smtp.example.com
MAIL_PORT=587
MAIL_USE_TLS=True
MAIL_USERNAME=your-email@example.com
MAIL_PASSWORD=your-email-password
```

5. Initialize the database:
```bash
flask db init
flask db migrate
flask db upgrade
```

6. Run the application:
```bash
flask run
```

## Usage

1. Access the application at `http://localhost:5000`
2. Register a new user account
3. Log in with your credentials
4. Access the admin dashboard (if you have admin privileges)

## Admin Features

- View all users
- Activate/deactivate user accounts
- Delete user accounts
- Monitor user activity

## Security Features

- Password hashing
- CSRF protection
- Session management
- Role-based access control
- Secure password reset (optional)

## Contributing

1. Fork the repository
2. Create a new branch
3. Make your changes
4. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Flask
- HTMX
- Bootstrap
- SQLAlchemy 