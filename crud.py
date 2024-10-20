import mysql.connector

# Establish a connection to the MySQL database
conn = mysql.connector.connect(
    host="srv1416.hstgr.io",
    user="u869042730_python",
    password="0:@0dgH]5shW",
    database="u869042730_python"
)

cursor = conn.cursor()

# Create the table if it doesn't exist
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100)
)
""")

# Function to create a new user
def create_user():
    name = input("Enter name: ")
    email = input("Enter email: ")
    cursor.execute("INSERT INTO users (name, email) VALUES (%s, %s)", (name, email))
    conn.commit()
    print("User created successfully!")

# Function to read all users
def read_users():
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    print("\nUser List:")
    for user in users:
        print(f"ID: {user[0]}, Name: {user[1]}, Email: {user[2]}")
    print()

# Function to update a user by ID
def update_user():
    user_id = input("Enter the user ID to update: ")
    name = input("Enter new name: ")
    email = input("Enter new email: ")
    cursor.execute("UPDATE users SET name = %s, email = %s WHERE id = %s", (name, email, user_id))
    conn.commit()
    print("User updated successfully!")

# Function to delete a user by ID
def delete_user():
    user_id = input("Enter the user ID to delete: ")
    cursor.execute("DELETE FROM users WHERE id = %s", (user_id,))
    conn.commit()
    print("User deleted successfully!")

# Function to show the menu
def menu():
    print("\n=== User Management ===")
    print("1. Create User")
    print("2. Read Users")
    print("3. Update User")
    print("4. Delete User")
    print("5. Exit")

# Main loop
while True:
    menu()
    choice = input("Enter your choice: ")

    if choice == "1":
        create_user()
    elif choice == "2":
        read_users()
    elif choice == "3":
        update_user()
    elif choice == "4":
        delete_user()
    elif choice == "5":
        print("Exiting...")
        break
    else:
        print("Invalid choice, please try again.")

# Close the cursor and connection
cursor.close()
conn.close()
