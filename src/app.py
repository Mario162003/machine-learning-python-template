from utils import db_connect
engine = db_connect()

# your code here
from dotenv import load_dotenv
import os

load_dotenv()  # Cargar variables de entorno desde el archivo .env

database_url = os.getenv('DATABASE_URL')
print(database_url)