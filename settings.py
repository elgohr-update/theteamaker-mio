from dotenv import load_dotenv
import os

load_dotenv()

PREFIX = "mio "
TOKEN = os.getenv("TOKEN")
SQL_DATABASE = os.getenv("SQL_DATABASE")