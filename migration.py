import pandas as pd
import os
from sqlalchemy import create_engine
from dotenv import load_dotenv

load_dotenv()

db_username = os.getenv("DB_USERNAME")
db_password = os.getenv("DB_PASSWORD")
db_host = os.getenv("DB_HOST")
db_port = os.getenv("DB_PORT")
db_name = os.getenv("DB_NAME")

file_path = "data/candidates_clean.csv"  
candidates = pd.read_csv(file_path, delimiter=',')

engine = create_engine(f"postgresql://{db_username}:{db_password}@{db_host}:{db_port}/{db_name}")

candidates.to_sql("candidates_clean", engine, if_exists="replace", index=False)

print("Datos migrados exitosamente a PostgreSQL")
