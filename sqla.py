from sqlalchemy import create_engine
import oracledb

# Create the connection string
username = "your_username"
password = "your_password"
host = "your_host"  # e.g., '127.0.0.1' or 'mydbserver.example.com'
port = 1521          # Default Oracle port
service_name = "your_service_name"  # Replace with your service name

# Connection URL format for Oracle using oracledb:
connection_url = f"oracle+oracledb://{username}:{password}@{host}:{port}/?service_name={service_name}"

# Create SQLAlchemy engine
engine = create_engine(connection_url)

# Test connection by executing a simple query
with engine.connect() as connection:
    result = connection.execute("SELECT * FROM your_table_name")
    for row in result:
        print(row)
