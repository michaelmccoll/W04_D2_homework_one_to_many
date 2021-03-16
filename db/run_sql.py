import psycopg2
import psycopg2.extras as ext                                   # Just renames the import function

# This makes the connection to your database
# This function can be re-used many times, only change required would be the 'dbname' it's linked to
def run_sql(sql,values = None):                                        # sql - will take in the sql query. values - will take in values to operate
    conn = None                                                 # This sets the connection as None by default
    results = []                                                # This starts function with an empty list
    try:                                                        # Tries to connect
        conn = psycopg2.connect("dbname='task_manager'")        # Connects to the database 'task_manager.sql'
        cur = conn.cursor(cursor_factory=ext.DictCursor)        # Creates a cursor for executing queries, the cursor will operate the sql instructions
        cur.execute(sql,values)                                 # Executes sql query with values
        conn.commit()                                           # Commit will finalise transaction created above
        results = cur.fetchall()                                # This makes results equal to whatever the cursor fetches
        cur.close()                                             # Closes the cursor
    except (Exception, psycopg2.DatabaseError) as error:        # This is the error message fed back, renamed 'error'
        print(error)
    finally:
        if conn is not None:                                    # Could also be written as 'conn != None'
            conn.close()                                        # This closes down the connection
    return results                                              # Returns the results