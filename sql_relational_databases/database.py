from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Connection string
SQLALCHEMY_DATABASE_URL = 'sqlite:///./sql_app.db'

# Create SQLAlchemy engine, note the connect_args argument is only needed for SQLite
engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False}
)

# Create SessionLocal class as our database session. 
# Used to create instances of our database session
# sessionamker is used to create the SessionLocal class
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
)

# declarative_base is used to create a Base class that our database models wil inherit from
Base = declarative_base()
