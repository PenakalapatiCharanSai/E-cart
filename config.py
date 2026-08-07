import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# ------------------------------------------
# Stores all configuration settings
# ------------------------------------------

SECRET_KEY = os.environ.get("FLASK_SECRET_KEY", "your_secret_key")

# MySQL Database
DB_HOST = os.environ.get("MYSQLHOST", "localhost")
DB_PORT = int(os.environ.get("MYSQLPORT", 3306))
DB_USER = os.environ.get("MYSQLUSER", "root")
DB_PASSWORD = os.environ.get("MYSQLPASSWORD", "")
DB_NAME = os.environ.get("MYSQLDATABASE", "smartcart_db")

# Email SMTP Settings
MAIL_SERVER = os.environ.get("MAIL_SERVER", "smtp.gmail.com")
MAIL_PORT = int(os.environ.get("MAIL_PORT", 587))
MAIL_USE_TLS = os.environ.get("MAIL_USE_TLS", "True").lower() in ("true", "1", "t")
MAIL_USERNAME = os.environ.get("MAIL_USERNAME", "")
MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD", "")

# Razorpay Configuration
RAZORPAY_KEY_ID = os.environ.get("RAZORPAY_KEY_ID", "")
RAZORPAY_KEY_SECRET = os.environ.get("RAZORPAY_KEY_SECRET", "")