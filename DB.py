import sqlite3
from datetime import datetime

def create_connection():
    return sqlite3.connect('foldersDB.db')

def craet_all_tables():
    create_table()
    create_scan_info_table()
    create_scans_menu_table()

def create_table():
    conn = create_connection()
    cursor = conn.cursor()

    create_table_query = '''
    CREATE TABLE IF NOT EXISTS folderNames (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        folder_name TEXT NOT NULL
    );
    '''
    cursor.execute(create_table_query)

    conn.commit()
    conn.close()


def create_scan_info_table():
    conn = create_connection() 
    cursor = conn.cursor()

    create_table_query = '''
    CREATE TABLE IF NOT EXISTS ScanInfo (
        id INTEGER PRIMARY KEY,
        Name TEXT,
        Description TEXT,
        FolderName TEXT,
        Target TEXT
    );
    '''
    cursor.execute(create_table_query)

    conn.commit()
    conn.close()

def create_scans_menu_table():
    conn = create_connection()  # Assume you have a function named create_connection
    cursor = conn.cursor()

    create_table_query = '''
    CREATE TABLE IF NOT EXISTS ScansMenu (
        Id INTEGER PRIMARY KEY,
        Name TEXT UNIQUE,
        Schedule TEXT,
        LastModify TEXT,
        FolderName TEXT,  -- New column added
        FOREIGN KEY (Name) REFERENCES ScanInfo(Name)
    );
    '''
    cursor.execute(create_table_query)

    conn.commit()
    conn.close()


def insert_scan_info_data(name, description, folder_name, target):
    conn = create_connection()
    cursor = conn.cursor()

    insert_data_query = f'''
    INSERT INTO ScanInfo (Name, Description, FolderName, Target)
    VALUES ('{name}', '{description}', '{folder_name}', '{target}');
    '''
    cursor.execute(insert_data_query)

    current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M")
    insert_scans_menu_query = f'''
    INSERT INTO ScansMenu (Name, Schedule, LastModify, FolderName)
    VALUES (?, 'N/A', ?, ?);
    '''
    try:
        cursor.execute(insert_scans_menu_query, (name, current_datetime, folder_name))
        conn.commit()
    except sqlite3.IntegrityError:
        print(f"A scan with the name '{name}' already exists.")
        # Handle the duplicate name scenario as needed, e.g., show an error message to the user

    conn.close()


def show_scans_menu_data():
    conn = create_connection()  
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM ScansMenu;")
    data = cursor.fetchall()

    conn.close()

    if not data:
        print("No data in the ScansMenu table.")
        return

    print(data)
    return data

def value_exists_in_column(value, table_name="ScanInfo", column_name="Name"):
    conn = create_connection()  
    cursor = conn.cursor()

    query = f"SELECT {column_name} FROM {table_name} WHERE {column_name} = ?;"
    cursor.execute(query, (value,))
    result = cursor.fetchone()

    conn.close()

    return result is not None

def show_scan_info_data():
    conn = create_connection()  # Assume you have a function named create_connection
    cursor = conn.cursor()

    # Retrieve all data from the ScanInfo table
    cursor.execute("SELECT * FROM ScanInfo;")
    data = cursor.fetchall()

    conn.close()

    return data


def show_tables_and_columns():
    conn = create_connection()  # Assume you have a function named create_connection
    cursor = conn.cursor()

    # Get a list of all tables in the database
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()

    # Display columns for each table
    for table in tables:
        table_name = table[0]
        print(f"Table: {table_name}")
        
        # Get column information for the current table
        cursor.execute(f"PRAGMA table_info({table_name});")
        columns = cursor.fetchall()

        # Display column names and types
        for column in columns:
            column_name = column[1]
            column_type = column[2]
            print(f"  Column: {column_name}, Type: {column_type}")

    conn.close()

def select_all_data():
    conn = create_connection()
    cursor = conn.cursor()

    select_query = 'SELECT * FROM folderNames'
    cursor.execute(select_query)

    rows = cursor.fetchall()

    conn.close()

    return rows

def remove_all_data():
    conn = create_connection()
    cursor = conn.cursor()

    remove_data_query = 'DELETE FROM folderNames'
    cursor.execute(remove_data_query)

    conn.commit()
    conn.close()

def remove_all_data_from_scan_info():
    conn = create_connection()
    cursor = conn.cursor()

    remove_data_query = 'DELETE FROM ScanInfo'
    cursor.execute(remove_data_query)

    conn.commit()
    conn.close()

def get_last_element_id():
    conn = create_connection()
    cursor = conn.cursor()

    select_last_id_query = 'SELECT MAX(id) FROM folderNames;'
    cursor.execute(select_last_id_query)

    last_id = cursor.fetchone()[0]  # Fetch the value from the result

    conn.close()
    if last_id == None:
        return -1
    return last_id

def insert_folder_data_if_not_exists(id, folder_name):
    conn = create_connection()
    cursor = conn.cursor()

    # Check if the record already exists
    select_query = f'SELECT id FROM folderNames WHERE id={id} OR folder_name="{folder_name}"'
    cursor.execute(select_query)
    existing_record = cursor.fetchone()

    if not existing_record:
        # If the record does not exist, insert it
        insert_data_query = f'''
        INSERT INTO folderNames (id, folder_name) VALUES
        ({id}, '{folder_name}');
        '''
        cursor.execute(insert_data_query)
    else:
        return 1

    conn.commit()
    conn.close()

def get_first_id_and_name():
    conn = create_connection()
    cursor = conn.cursor()

    select_first_id_query = 'SELECT id, folder_name FROM folderNames ORDER BY id LIMIT 1;'
    cursor.execute(select_first_id_query)

    first_record = cursor.fetchone()
    result = {0: None, 1: None}

    if first_record is not None:
        result[0] = first_record[0]
        result[1] = first_record[1]

    conn.close()

    return result

def get_scan_info_row_count():
    conn = create_connection()  # Assume you have a function named create_connection
    cursor = conn.cursor()

    # Check if there is data in the ScanInfo table
    cursor.execute("SELECT COUNT(*) FROM ScanInfo;")
    row_count = cursor.fetchone()[0]

    conn.close()

    return row_count

def delete_folder_by_name(folder_name):
    conn = create_connection()
    cursor = conn.cursor()

    # Find the record with the given folder name
    select_query = f'SELECT id FROM folderNames WHERE folder_name="{folder_name}"'
    cursor.execute(select_query)
    record_to_delete = cursor.fetchone()

    if record_to_delete:
        # If the record exists, delete it and any records with the same ID
        delete_query = f'DELETE FROM folderNames WHERE id={record_to_delete[0]} OR folder_name="{folder_name}"'
        cursor.execute(delete_query)

    conn.commit()
    conn.close()

def get_scans_menu_values():
    conn = create_connection()
    cursor = conn.cursor()

    # Retrieve data from the ScansMenu table excluding the ID column
    cursor.execute("SELECT Name, Schedule, LastModify FROM ScansMenu;")
    data = cursor.fetchall()

    conn.close()

    return data

def get_scans_menu_columns_by_folder(folder_name):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute(f"SELECT Name, Schedule, LastModify FROM ScansMenu WHERE FolderName = ?;", (folder_name,))
    data = cursor.fetchall()

    conn.close()

    return data


def delete_all_scans_menu_values():
    conn = create_connection()  # Assume you have a function named create_connection
    cursor = conn.cursor()

    # Delete all rows from the ScansMenu table
    cursor.execute("DELETE FROM ScansMenu;")

    conn.commit()
    conn.close()

def delete_scans_menu_rows_by_folder(folder_name):
    conn = create_connection()  # Assume you have a function named create_connection
    cursor = conn.cursor()

    # Delete rows from the ScansMenu table where FolderName is equal to the provided value
    cursor.execute("DELETE FROM folderNames WHERE folder_name = ?;", (folder_name,))

    conn.commit()
    conn.close()

def folder_name_exists(folder_name):
    conn = create_connection()  # Assume you have a function named create_connection
    cursor = conn.cursor()

    # Check if the given folder_name exists in the folderNames table
    cursor.execute("SELECT EXISTS(SELECT 1 FROM folderNames WHERE folder_name = ?);", (folder_name,))
    exists = cursor.fetchone()[0] == 1

    conn.close()

    return exists

def insert_folder_name(folder_name):
    conn = create_connection()
    cursor = conn.cursor()

    # Insert data into the folderNames table, excluding the id column
    cursor.execute("INSERT INTO folderNames (folder_name) VALUES (?);", (folder_name,))

    conn.commit()
    conn.close()

def rename_folder(old_folder_name, new_folder_name):
    conn = create_connection()
    cursor = conn.cursor()

    # Update the folder name in the folderNames table
    cursor.execute("UPDATE folderNames SET folder_name = ? WHERE folder_name = ?;", (new_folder_name, old_folder_name))

    conn.commit()
    conn.close()

def insert_scan_info(name, description, folder_name, target):
    conn = create_connection()
    cursor = conn.cursor()

    # Insert data into the ScanInfo table
    cursor.execute("INSERT INTO ScanInfo (Name, Description, FolderName, Target) VALUES (?, ?, ?, ?);",
                   (name, description, folder_name, target))

    conn.commit()
    conn.close()



def get_scan_info_by_name(name):
    conn = create_connection()
    cursor = conn.cursor()

    try:
        select_query = '''
        SELECT * FROM ScanInfo
        WHERE Name = ?
        '''
        cursor.execute(select_query, (name,))
        row = cursor.fetchone()
        if row:
            return row
        else:
            return None
    except sqlite3.Error as e:
        print("Error retrieving data:", e)
    finally:
        conn.close()

def remove_scan_info_by_name(name):
    conn = create_connection()
    cursor = conn.cursor()

    try:
        delete_query = '''
        DELETE FROM ScanInfo
        WHERE Name = ?
        '''
        cursor.execute(delete_query, (name,))
        
        conn.commit()
    except sqlite3.Error as e:
        print("Error removing row(s):", e)
    finally:
        conn.close()


def check_scan_info_data():
    conn = create_connection()
    cursor = conn.cursor()

    # Execute a SELECT query to count the number of rows in ScanInfo
    cursor.execute("SELECT COUNT(*) FROM ScanInfo")
    row_count = cursor.fetchone()[0]  # Fetch the count from the result

    conn.close()

    return row_count

def remove_scan_by_name(name):
    conn = create_connection()
    cursor = conn.cursor()

    # Execute the DELETE query to remove the row by name
    delete_query = "DELETE FROM ScansMenu WHERE Name = ?"
    cursor.execute(delete_query, (name,))

    conn.commit()
    conn.close()


def delete_row_by_folder_name(folder_name):
    conn = create_connection()
    cursor = conn.cursor()

    try:
        delete_query = '''
        DELETE FROM ScansMenu
        WHERE FolderName = ?
        '''
        cursor.execute(delete_query, (folder_name,))
        
        conn.commit()
    except sqlite3.Error as e:
        print("Error removing row(s):", e)
    finally:
        conn.close()

def delete_row_by_foldername(folder_name):
    conn = create_connection()
    cursor = conn.cursor()

    try:
        delete_query = '''
        DELETE FROM folderNames
        WHERE folder_name = ?
        '''
        cursor.execute(delete_query, (folder_name,))
        
        conn.commit()
    except sqlite3.Error as e:
        print("Error removing row(s):", e)
    finally:
        conn.close()



# remove_scan_info_by_name('sdfgsdgdfs')

# print(get_scan_info_by_name('IT Gate Academy')[3])


# delete_scans_menu_rows_by_folder('Scan 2')
# delete_row_by_folder_name('Scan 3')
# print(get_scans_menu_columns_by_folder('Scan 2'))


# data = get_scans_menu_values()

# for i in data:
#     print(i)

# print()
# for i in show_scan_info_data():
#     print(i)

# insert_scan_info_data('Tiba', 'This scan for tiba academy', 'scan 1', 'https://portal.tiba.edu.eg')
# insert_scan_info_data('home', 'This scan for my home', 'scan 1', '192.168.1.1')
# insert_scan_info_data('Test', 'This scan test scan', 'scan 2', 'https://test.com')


# print(get_scans_menu_columns_by_folder('Scan 2'))


# print(folder_name_exists('scan 1'))

# remove_all_data()
# remove_all_data_from_scan_info()
# delete_all_scans_menu_values()


# insert_data_1()
# insert_data_2()
# insert_scan_info_data()
# insert_folder_data_if_not_exists(10,"scan 10")


# data = select_all_data()

# for row in data:
#     print(f'ID: {row[0]}, Folder Name: {row[1]}')

# delete_scans_menu_rows_by_folder("scan 4")

# show_tables_and_columns()
# print(get_last_element_id())
# print(get_first_id_and_name()[0]," ",get_first_id_and_name()[1])

# print(value_exists_in_column("Tiba"))
# print(get_scan_info_row_count())

# print(show_scan_info_data())

# data = get_scans_menu_values()
# # print(data)
# for i in data:
#     for z in i:
#         print(z)


# if get_scans_menu_columns_by_folder("scan 1"):
    # print('done')

# for i in get_scans_menu_columns_by_folder("scan 1"):
#     for x in i:
#         print(x)

# print(show_scan_info_data())

# for i in show_scan_info_data():
#     print(i)

# data = select_all_data()
# print(data)
# for i in data:
#     print(i)
