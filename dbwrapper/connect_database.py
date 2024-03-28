import psycopg2
from dotenv import load_dotenv
import os
# from exceptions import CustomErrors
# from log_config import logger
load_dotenv()

class ConnectDatabase_postgres:
    """
    Class for establishing a connection to a PostgreSQL database.

    Attributes:
    - connection: PostgreSQL database connection object.
    - cursor: Cursor object to execute SQL queries.

    Methods:
    - __init__(): Initializes the database connection using environment variables for configuration.
    - get_cursor(): Returns the cursor object.
    - close_connection(): Closes the database connection.

    The class is designed to handle database connections for PostgreSQL. It uses the psycopg2 library for
    communication with the PostgreSQL database.
    """

    
    def __init__(self):
        """
        Initializes the database connection.

        Configuration is based on environment variables:
        - POSTGRES_DB_NAME: Name of the PostgreSQL database.
        - POSTGRES_USER: Username for connecting to the PostgreSQL database.
        - POSTGRES_DB_PASS: Password for connecting to the PostgreSQL database.
        - POSTGRES_HOST: Hostname or IP address of the PostgreSQL database server.
        - POSTGRES_PORT: Port number on which the PostgreSQL database server is listening.

        Raises:
        - SystemExit: If an exception occurs during database connection setup, the program exits with an error.
        """
        try:
            self.connection = psycopg2.connect(database=os.getenv('POSTGRES_DB_NAME'),
                                            user=os.getenv('POSTGRES_USER'),
                                            password=os.getenv('POSTGRES_DB_PASS'),
                                            host=os.getenv('POSTGRES_HOST'),
                                            port=os.getenv('POSTGRES_PORT'))
            self.cursor = self.connection.cursor()
        except Exception as e:
            
            raise SystemExit(e)

    def get_cursor(self):
        """
        Returns the cursor object for executing SQL queries.

        Returns:
        - psycopg2.extensions.cursor: Cursor object.
        """
        return self.cursor

    def close_connection(self):
        """
        Closes the database connection.
        """
        self.connection.close()



        