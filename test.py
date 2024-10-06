from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# JDBC connection details
jdbc_url = "jdbc:oracle:thin:@//hostname:port/service_name"  # Replace with your actual connection string
username = "your_username"  # Replace with your username
password = "your_password"  # Replace with your password

# Function to create the SQLAlchemy engine
def create_engine_instance():
    try:
        engine = create_engine(
            f"jdbcapi://{username}:{password}@{jdbc_url}",
            pool_size=10,          # Maximum number of connections in the pool
            max_overflow=5,       # Maximum number of connections to allow beyond pool_size
            pool_timeout=30,      # Number of seconds to wait before giving up on getting a connection
            pool_recycle=1800     # Recycle connections after this many seconds
        )
        print("Database engine created successfully.")
        return engine
    except Exception as e:
        print("Error creating database engine:", e)
        return None

# Function to create a sessionmaker
def create_sessionmaker(engine):
    try:
        session_factory = sessionmaker(bind=engine)
        print("Sessionmaker created successfully.")
        return session_factory
    except Exception as e:
        print("Error creating sessionmaker:", e)
        return None

# Function to use the session pool
def perform_db_operations(session_factory):
    # Create a session from the session factory
    session = session_factory()
    try:
        # Example query to test the connection
        result = session.execute("SELECT * FROM your_table_name")  # Replace with your actual table name
        for row in result:
            print(row)
    except Exception as e:
        print("Error during database interaction:", e)
    finally:
        session.close()

# Example usage
if __name__ == "__main__":
    # Create the SQLAlchemy engine inside a try block
    engine = create_engine_instance()
    
    if engine is not None:
        # Create the sessionmaker inside a try block
        Session = create_sessionmaker(engine)
        
        if Session is not None:
            for _ in range(5):  # Simulate multiple calls to the function
                perform_db_operations(Session)
        else:
            print("Failed to create sessionmaker; session operations will not proceed.")
    else:
        print("Failed to create engine; session operations will not proceed.")
