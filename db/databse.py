from playhouse.db_url import connect
from dotenv import load_dotenv
from os import getenv
load_dotenv()
db = connect(getenv("DB_URL"))