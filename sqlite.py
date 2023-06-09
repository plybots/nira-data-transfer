import sqlite3


class SQLiteManager:
    def get_connection(self):
        # Create a connection to the SQLite database
        conn = sqlite3.connect("logs.db")
        # Check if the 'logs' table exists, if not, create it
        conn.cursor().execute('''CREATE TABLE IF NOT EXISTS logs
                                  (id TEXT PRIMARY KEY)''')
        return conn

    def store(self, id):
        conn = self.get_connection()
        cursor = conn.cursor()
        try:
            # Store the id in the 'logs' table
            cursor.execute("INSERT INTO logs (id) VALUES (?)", (id,))
            conn.commit()
        except sqlite3.IntegrityError:
            pass

        cursor.close()
        conn.close()

    def id_exists(self, id):
        conn = self.get_connection()
        cursor = conn.cursor()

        # Query the 'logs' table for the provided id
        cursor.execute("SELECT COUNT(*) FROM logs WHERE id=?", (id,))
        result = cursor.fetchone()

        cursor.close()
        conn.close()

        # Return True if the id exists, False otherwise
        return result[0] > 0
