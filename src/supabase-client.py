import os
from supabase import create_client, Client

url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")
supabase: Client = create_client(url, key)


def test_db_connection():
    try:
        # Run a simple select query on a known table.
        response = (supabase.table("agents").select("*").execute())

        if hasattr(response, 'error') and response.error:
            print("Error accessing the database:", response.error)
        else:
            # If you have any rows returned, the connection is working
            print("Connection successful. Data returned:")
            print(response.data)
    except Exception as e:
        print("An exception occurred while testing the DB connection:", e)

if __name__ == "__main__":
    test_db_connection()