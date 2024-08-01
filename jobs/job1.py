def job1():
    print("Job 1 executed.")
    import sqlite3
    
    conn = sqlite3.connect(':memory:')
    cursor = conn.cursor()
    
    cursor.execute('''CREATE TABLE sample (id INTEGER PRIMARY KEY, name TEXT)''')
    cursor.execute("INSERT INTO sample (name) VALUES ('Alice')")
    cursor.execute("INSERT INTO sample (name) VALUES ('Bob')")
    conn.commit()
    
    # Query the database
    cursor.execute("SELECT * FROM sample")
    results = cursor.fetchall()
    
    print("Query results:")
    for row in results:
        print(row)
    
    # Close the connection
    conn.close()
