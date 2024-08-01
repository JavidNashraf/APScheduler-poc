def job1():
    print("Job 1 executed.")
    import sqlite3
    
    conn = sqlite3.connect(':memory:')
    cursor = conn.cursor()
    
    cursor.execute('''CREATE TABLE sample (id INTEGER PRIMARY KEY, name TEXT)''')
    
    def post_job():
        cursor.execute("INSERT INTO sample (name) VALUES ('Javid')")
        cursor.execute("INSERT INTO sample (name) VALUES ('Nashraf')")
        conn.commit()
        print("POST job completed: Added Javid and Nashraf")
    
    def get_job():
        cursor.execute("SELECT * FROM sample")
        results = cursor.fetchall()
        print("GET job results:")
        for row in results:
            print(row)
    
    def put_job():
        cursor.execute("UPDATE sample SET name = 'UserChanged' WHERE name = 'Javid'")
        conn.commit()
        print("PUT job completed: Updated Javid to UserChanged")
    
    def delete_job():
        cursor.execute("DELETE FROM sample WHERE name = 'Nashraf'")
        conn.commit()
        print("DELETE job completed: Removed Nashraf")
    
    post_job()
    get_job()
    put_job()
    get_job()
    delete_job()
    get_job()
    
    # Close the connection
    conn.close()
