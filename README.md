# E-cart E-commerce Platform (SQLite Version)

A fully functional, modern e-commerce web application built using Python Flask. It features user authentication, a product catalog, shopping cart functionality, secure checkout using Razorpay, order tracking, invoice generation, and a complete admin dashboard for inventory and order management.

This application has been optimized to run on **PythonAnywhere's Free Tier** by utilizing a lightweight **SQLite** database instead of MySQL, requiring zero external database hosting.

## Features
- **User Authentication**: Secure registration and login with bcrypt password hashing.
- **Product Catalog**: View products with categories and search functionality.
- **Shopping Cart & Checkout**: Add products to cart, specify delivery addresses, and securely pay via Razorpay.
- **Order Management**: Users can track their orders and download invoices.
- **Admin Dashboard**: Secure admin login to add/edit/delete products and manage user orders.

## Technologies Used
- **Backend**: Python 3.11, Flask, Flask-Mail
- **Database**: SQLite3 (Built-in Python Library)
- **Frontend**: HTML5, CSS3, Jinja2 Templates, FontAwesome
- **Security**: bcrypt (Password hashing), python-dotenv (Environment variables)
- **Payments**: Razorpay API

## Project Structure
```text
Ecart/
├── app.py                  # Main Flask application entry point
├── config.py               # Configuration and environment variables setup
├── init_db.py              # Script to safely initialize the SQLite database
├── requirements.txt        # Python dependencies (No MySQL dependencies required!)
├── .env.example            # Template for environment variables
├── .gitignore              # Files to ignore in Git
├── database/
│   ├── smartcart.db        # The active SQLite database file (created automatically)
│   ├── sqlite_schema.sql   # SQLite schema used by init_db.py
│   └── mysql_schema.sql    # Original MySQL schema preserved as a backup/reference
├── static/                 # CSS stylesheets and uploaded images
└── templates/              # HTML templates (Jinja2)
```

## Prerequisites
- Python 3.11 or higher
- Razorpay Account (for testing payments)
- Gmail App Password (for sending OTPs and emails)

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
MAIL_SERVER=smtp.gmail.com
MAIL_PORT=587
MAIL_USE_TLS=True
MAIL_USERNAME=your-email@gmail.com
MAIL_PASSWORD=your-app-password
RAZORPAY_KEY_ID=your-razorpay-key
RAZORPAY_KEY_SECRET=your-razorpay-secret
```
*Note: No database credentials are required since we use a local SQLite file.*

## Database Setup
Because this version uses SQLite, setting up the database is completely automated.

Run the following command to create the `database/smartcart.db` file and build the tables:
```bash
python init_db.py
```
*Note: This will create an empty database. You will need to use the app to register a new admin account and upload your products again, as your old MySQL data is not automatically migrated.*

## How to Run Locally
Start the Flask development server:
```bash
python app.py
```
Open your browser and navigate to `http://127.0.0.1:5000/`.

## PythonAnywhere Deployment Preparation
This project is fully configured for deployment on a Free PythonAnywhere account.
1. Upload your code to PythonAnywhere (via GitHub or zip upload).
2. Create a new Web App using the **Flask** framework and **Python 3.11**.
3. Open a bash console on PythonAnywhere and install dependencies: `pip install -r requirements.txt`.
4. Create your `.env` file securely on the server.
5. Run `python init_db.py` on the PythonAnywhere console to generate the production database.
6. Reload your Web App. PythonAnywhere will automatically find `app.py` and serve the site using your SQLite database!
