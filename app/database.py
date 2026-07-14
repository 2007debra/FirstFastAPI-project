from sqlalchemy import create_engine

DATABASE_URL = "postgresql+psycopg://debra:debrafastapi@localhost:5432/firstfastapiproject"

engine = create_engine(DATABASE_URL)