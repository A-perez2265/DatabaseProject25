import sqlite3

DATABASE_FILE = "netflix_db.db"

# WATCHLIST FUNCS   

def create_watchlist(list_name, teacher_name): # create
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
            
def read_all_watchlist(): # read
    #prints the watchlist
    conn = None
    try:
        conn = sqlite3.connect(DATABASE_FILE)
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM Watchlists")
        watchlists = cursor.fetchall()
        return watchlists # return the fetched watchlists
    
    except sqlite3.Error as e:
        print(f"Error has occured: {e}")
        return [] # return empty list on error
    finally:
        if conn:
            conn.close()
            
def delete_watchlist(watchlist_id): # deletes a watchlist by ID
    # connect to the database
    conn = None 
    try:
        conn = sqlite3.connect(DATABASE_FILE) 
        cursor = conn.cursor()

        # get name before deleting
        cursor.execute("SELECT list_name FROM Watchlists WHERE list_id = ?", (watchlist_id,))
        result = cursor.fetchone()
        if not result:
            return False, None  # no record found
        
        list_name = result[0] # extract list name

        # execute the delete statement
        cursor.execute("DELETE FROM Watchlists WHERE list_id = ?", (watchlist_id,))
        conn.commit()

        return cursor.rowcount, list_name # 0 if no rows deleted, 1 if deleted

    except sqlite3.Error as e:
        print(f"Error has occurred: {e}")
    finally:
        if conn:
            conn.close()

def update_watchlist(list_id, new_list_name, new_teacher_name): # updates a watchlist's name and teacher
    conn = None
    try:
        conn = sqlite3.connect(DATABASE_FILE)
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE Watchlists SET list_name = ?, teacher_name = ? WHERE list_id= ?",
            (new_list_name, new_teacher_name, list_id),
        )
        conn.commit()
        return cursor.rowcount  # number of rows updated
    except sqlite3.Error as e:
        print(f"Error has occurred: {e}")
        return 0
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