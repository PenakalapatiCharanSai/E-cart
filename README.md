# E-cart E-commerce Platform

A fully functional, modern e-commerce web application built using Python Flask and MySQL. It features user authentication, a product catalog, shopping cart functionality, secure checkout using Razorpay, order tracking, invoice generation, and a complete admin dashboard for inventory and order management.

## Features
- **User Authentication**: Secure registration and login with bcrypt password hashing.
- **Product Catalog**: View products with categories and search functionality.
- **Shopping Cart & Checkout**: Add products to cart, specify delivery addresses, and securely pay via Razorpay.
- **Order Management**: Users can track their orders and download invoices.
- **Admin Dashboard**: Secure admin login to add/edit/delete products and manage user orders.

## Technologies Used
- **Backend**: Python 3, Flask, Flask-Mail
- **Database**: MySQL (via mysql-connector-python)
- **Frontend**: HTML5, CSS3, Jinja2 Templates, FontAwesome
- **Security**: bcrypt (Password hashing), python-dotenv (Environment variables)
- **Payments**: Razorpay API

## Project Structure
```text
Ecart/
├── app.py                  # Main Flask application entry point
├── config.py               # Configuration and environment variables setup
├── requirements.txt        # Python dependencies
├── Procfile                # Railway deployment configuration
├── .env.example            # Template for environment variables
├── .gitignore              # Files to ignore in Git
├── database/
│   └── schema.sql          # MySQL database schema for easy setup
├── static/                 # CSS stylesheets and uploaded images
└── templates/              # HTML templates (Jinja2)
    ├── admin/              # Admin interface templates
    └── user/               # User interface templates
```

## Prerequisites
- Python 3.11 or higher
- MySQL Server (Local or Cloud)
- Razorpay Account (for testing payments)

## Local Installation Instructions

1. **Clone the repository**:
   ```bash
   git clone https://github.com/PenakalapatiCharanSai/E-cart.git
   cd E-cart
   ```

2. **Create a virtual environment**:
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment**:
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## Configuration (.env)
Create a `.env` file in the root directory based on `.env.example`:
```text
FLASK_SECRET_KEY=your_secret_key
MYSQLHOST=localhost
MYSQLPORT=3306
MYSQLUSER=root
MYSQLPASSWORD=your-local-mysql-password
MYSQLDATABASE=smartcart_db
MAIL_SERVER=smtp.gmail.com
MAIL_PORT=587
MAIL_USE_TLS=True
MAIL_USERNAME=your-email@gmail.com
MAIL_PASSWORD=your-app-password
RAZORPAY_KEY_ID=your-razorpay-key
RAZORPAY_KEY_SECRET=your-razorpay-secret
```

## Database Setup
1. Open your MySQL Command Line Client or preferred GUI (e.g., phpMyAdmin, DBeaver).
2. Create the database:
   ```sql
   CREATE DATABASE smartcart_db;
   USE smartcart_db;
   ```
3. Import the schema to create the necessary tables:
   - On Windows Command Prompt:
     ```cmd
     mysql -u root -p smartcart_db < database\schema.sql
     ```
   - Or just copy and paste the contents of `database/schema.sql` into your SQL client and execute it.

## How to Run Locally
Start the Flask development server:
```bash
python app.py
```
Open your browser and navigate to `http://127.0.0.1:5000/`.

## Production Start Command
For production environments (like Railway), the app is started using Gunicorn:
```bash
gunicorn app:app
```
*Note: Ensure `debug=True` is disabled in production environments.*

## Railway Deployment Preparation
This project is pre-configured for Railway deployment via GitHub:
1. Push your code to GitHub.
2. Link the repository to a new Railway project.
3. Provision a MySQL Database in Railway.
4. Copy the environment variables from your local `.env` file into the Railway Service Variables, ensuring you update the `MYSQL...` variables to match your new Railway database credentials.
5. Railway will automatically build and start the application using the `Procfile`.
