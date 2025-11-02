import sqlite3

DATABASE_FILE = "netflix_db.db"

def create_watchlist(list_name, teacher_name):
    conn = None
    try:
        conn = sqlite3.connect(DATABASE_FILE)
        cursor = conn.cursor()

        cursor.execute("INSERT INTO Watchlists (list_name, teacher_name) VALUES (?, ?)",
                       (list_name, teacher_name))
        conn.commit()
        print(f"Watchlist '{list_name}' created successfully.")
    except sqlite3.Error as e:
        print(f"Error has occured: {e}")
    finally:
        if conn:
            conn.close()
            

def read_all_watchlist():
    #prints the watchlist
    conn = None
    try:
        conn = sqlite3.connect(DATABASE_FILE)
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM Watchlists")
        watchlists = cursor.fetchall()

        if not watchlists:
            print("No watchlists found.")
            return
        print("Current Watchlists:")
        print("ID\tList Name\tTeacher Name\tCreated Date")
        for item in watchlists:
            print(f"{item[0]}\t{item[1]}\t{item[2]}\t{item[3]}")
    except sqlite3.Error as e:
        print(f"Error has occured: {e}")
    finally:
        if conn:
            conn.close()
            



if __name__ == "__main__":
    
    print("--- (R)EAD: First, reading all watchlists . ---")
    read_all_watchlist()
    
    print("\n--- (C)REATE: Now, creating two new watchlists. ---")
    create_watchlist("Geology 101", "Mr. Smith")
    create_watchlist("History of Film", "Ms. Davis")
    
    print("\n--- (R)EAD: Finally, reading all watchlists again. ---")
    read_all_watchlist()
    
    print("\n--- END OF DEMO ---")