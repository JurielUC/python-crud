import mysql.connector
from mysql.connector import Error
from datetime import datetime

# Connection
try:
    conn = mysql.connector.connect(
        host="srv1416.hstgr.io",
        user="u869042730_python",
        password="0:@0dgH]5shW",
        database="u869042730_python"
    )
    if conn.is_connected():
        print("Connected to MySQL database")
except Error as e:
    print(f"Error while connecting to MySQL: {e}")
    exit()

cursor = conn.cursor()

# Menu display (START) #
def display_menu():
    print("\n--- Disaster Management System ---")
    print("1. Manage Evacuation Centers")
    print("2. Manage Residents")
    print("3. Manage Resources")
    print("4. Manage Volcano Monitoring")
    print("5. Manage Disaster Alerts")
    print("6. Exit")
    print("\n")

def evacuation_center_menu():
    print("\n--- Evacuation Centers ---")
    print("1. Add New Evacuation Center")
    print("2. View All Evacuation Centers")
    print("3. Update Evacuation Center")
    print("4. Delete Evacuation Center")
    print("5. Back to Main Menu")
    print("\n")

def residents_menu():
    print("\n--- Residents ---")
    print("1. Add New Resident")
    print("2. View All Residents")
    print("3. Update Resident")
    print("4. Delete Resident")
    print("5. Back to Main Menu")
    print("\n")

def resources_menu():
    print("\n--- Resources ---")
    print("1. Add New Resource")
    print("2. View All Resources")
    print("3. Update Resource")
    print("4. Delete Resource")
    print("5. Back to Main Menu")
    print("\n")

def monitorings_menu():
    print("\n--- Volcano Monitoring Updates ---")
    print("1. Add New Monitoring")
    print("2. View All Monitorings")
    print("3. Update Monitoring")
    print("4. Delete Monitoring")
    print("5. Back to Main Menu")
    print("\n")

def alerts_menu():
    print("\n--- Disaster Alerts ---")
    print("1. Add New Alert")
    print("2. View All Alerts")
    print("3. Update Alert")
    print("4. Delete Alert")
    print("5. Back to Main Menu")
    print("\n")
# Menu display (END) #

#====================================================================================================
# EVACUATION CENTER CRUD FUNCTIONS (START)
# Create Evacuation Center
def create_evacuation_center():
    try:
        print("\n==============================================")
        print("--- ADD: Evacuation Center Form ---")
        print("==============================================")
        name = input("Name: ")
        capacity = input("Capacity: ")
        location = input("Location: ")
        cursor.execute("""
        INSERT INTO evacuation_centers (name, capacity, location)
        VALUES (%s, %s, %s)
        """, (name, capacity, location))
        conn.commit()
        print("")
        print("Evacuation Center added successfully.")
        print("==============================================")
    except Error as e:
        print(f"Error while adding evacuation center: {e}")

# Read Evacuation Centers
def read_evacuation_centers():
    try:
        cursor.execute("SELECT * FROM evacuation_centers")
        centers = cursor.fetchall()
        if centers:
            print("\n==============================================")
            print("--- List of Evacuation Centers ---")
            print("{:<5} {:<20} {:<10} {:<20}".format('ID', 'Name', 'Capacity', 'Location'))
            for center in centers:
                print("{:<5} {:<20} {:<10} {:<20}".format(center[0], center[1], center[2], center[3]))

            print("==============================================")
        else:
            print("No evacuation centers found.")
            print("==============================================")
    except Error as e:
        print(f"Error while retrieving evacuation centers: {e}")

# Update Evacuation Center
def update_evacuation_center():
    try:
        print("\n==============================================")
        print("--- UPDATE: Evacuation Center Form ---")
        print("==============================================")
        center_id = input("Enter the ID of the evacuation center to update: ")
        name = input("Name: ")
        capacity = input("Capacity: ")
        location = input("Location: ")
        cursor.execute("""
        UPDATE evacuation_centers
        SET name = %s, capacity = %s, location = %s
        WHERE id = %s
        """, (name, capacity, location, center_id))
        conn.commit()
        print("")
        print("Evacuation Center updated successfully.")
        print("==============================================")
    except Error as e:
        print(f"Error while updating evacuation center: {e}")

# Delete Evacuation Center
def delete_evacuation_center():
    try:
        center_id = input("Enter the ID of the evacuation center to delete: ")
        cursor.execute("DELETE FROM evacuation_centers WHERE id = %s", (center_id,))
        conn.commit()
        print(f"Evacuation Center {center_id} deleted successfully.")
    except Error as e:
        print(f"Error while deleting evacuation center: {e}")

# EVACUATION CENTER CRUD FUNCTIONS (END)

#====================================================================================================
# RESIDENT CRUD FUNCTIONS (START)
# Create Resident
def create_resident():
    try:
        print("\n==============================================")
        print("--- ADD: Resident Form ---")
        print("==============================================")
        evacuation_center_id = input("Enter the evacuation center ID: ")
        name = input("Name: ")
        age = input("Age: ")
        address = input("Address: ")
        cursor.execute("""
        INSERT INTO residents (evacuation_center_id, name, age, address)
        VALUES (%s, %s, %s, %s)
        """, (evacuation_center_id, name, age, address))
        conn.commit()
        print("Resident added successfully.")
    except Error as e:
        print(f"Error while adding resident: {e}")

# Read Residents
def read_residents():
    try:
        cursor.execute("SELECT * FROM residents")
        residents = cursor.fetchall()
        if residents:
            print("\n==============================================")
            print("--- List of Residents ---")
            print("{:<5} {:<20} {:<10} {:<20} {:<10}".format('ID', 'Name', 'Age', 'Address', 'Center ID'))
            for resident in residents:
                print("{:<5} {:<20} {:<10} {:<20} {:<10}".format(resident[0], resident[2], resident[3], resident[4], resident[1]))
            print("==============================================")
        else:
            print("No residents found.")
            print("==============================================")
    except Error as e:
        print(f"Error while retrieving residents: {e}")

# Update Resident
def update_resident():
    try:
        print("\n==============================================")
        print("--- UPDATE: Resident Form ---")
        print("==============================================")
        resident_id = input("Enter the ID of the resident to update: ")
        evacuation_center_id = input("Evacuation center ID: ")
        name = input("Name: ")
        age = input("Age: ")
        address = input("Address: ")
        cursor.execute("""
        UPDATE residents
        SET evacuation_center_id = %s, name = %s, age = %s, address = %s
        WHERE id = %s
        """, (evacuation_center_id, name, age, address, resident_id))
        conn.commit()
        print("")
        print("Resident updated successfully.")
        print("==============================================")
    except Error as e:
        print(f"Error while updating resident: {e}")

# Delete Resident
def delete_resident():
    try:
        resident_id = input("Enter the ID of the resident to delete: ")
        cursor.execute("DELETE FROM residents WHERE id = %s", (resident_id,))
        conn.commit()
        print(f"Resident {resident_id} deleted successfully.")
    except Error as e:
        print(f"Error while deleting resident: {e}")
# RESIDENT CRUD FUNCTIONS (END)

#====================================================================================================
# MONITORING CRUD FUNCTIONS (START)
# Create Monitoring
def create_monitoring():
    try:
        print("\n==============================================")
        print("--- ADD: Volcano Monitoring Form ---")
        print("==============================================")
        date_time = input("Date and Time: ")
        gas_levels = input("Gas Levels: ")
        siesmic_activities = input("Activity: ")
        temperature = input("Temperature: ")
        cursor.execute("""
        INSERT INTO volcano_monitoring (date_time, gas_levels, siesmic_activities, temperature)
        VALUES (%s, %s, %s, %s)
        """, (date_time, gas_levels, siesmic_activities, temperature))
        conn.commit()
        print("Volcano update added successfully.")
    except Error as e:
        print(f"Error while adding monitoring update: {e}")

# Read Monitoring
def read_monitorings():
    try:
        cursor.execute("SELECT * FROM volcano_monitoring")
        items = cursor.fetchall()
        if items:
            print("\n==============================================")
            print("--- List of Volcano Updates ---")
            print("{:<5} {:<40} {:<20} {:<20} {:<10}".format('ID', 'Date and Time', 'Gas Levels', 'Activity', 'Temperature'))
            for item in items:
                print("{:<5} {:<40} {:<20} {:<20} {:<10}".format(item[0], item[1], item[2], item[3], item[4]))
            print("==============================================")
        else:
            print("No monitoring updates found.")
            print("==============================================")
    except Error as e:
        print(f"Error while retrieving monitoring updates: {e}")

# Update Monitoring
def update_monitoring():
    try:
        print("\n==============================================")
        print("--- UPDATE: Volcano Monitoring Form ---")
        print("==============================================")
        monitoring_id = input("Enter the ID of the monitoring to update: ")
        date_time = input("Date and Time: ")
        gas_levels = input("Gas Levels: ")
        siesmic_activities = input("Activity: ")
        temperature = input("Temperature: ")
        cursor.execute("""
        UPDATE volcano_monitoring
        SET date_time = %s, gas_levels = %s, siesmic_activities = %s, temperature = %s
        WHERE id = %s
        """, (date_time, gas_levels, siesmic_activities, temperature, monitoring_id))
        conn.commit()
        print("")
        print("Volcano monitoring update updated successfully.")
        print("==============================================")
    except Error as e:
        print(f"Error while updating monitoring update: {e}")

# Delete Monitoring
def delete_monitoring():
    try:
        monitoring_id = input("Enter the ID of the volcano monitoring update to delete: ")
        cursor.execute("DELETE FROM residents WHERE id = %s", (monitoring_id,))
        conn.commit()
        print(f"Volcano monitoring update ID {monitoring_id} deleted successfully.")
    except Error as e:
        print(f"Error while deleting monitoring update: {e}")
# MONITORING CRUD FUNCTIONS (END)

#====================================================================================================
# DISASTER ALERTS CRUD FUNCTIONS (START)
# Create Disaster Alerts
def create_alert():
    try:
        print("\n==============================================")
        print("--- ADD: Disaster Alert Form ---")
        print("==============================================")
        evacuation_center_id = input("Enter the evacuation center ID: ")
        volcano_monitoring_id = input("Enter the volcano monitoring ID: ")
        alert_level = input("Alert Level: ")
        description = input("description: ")
        cursor.execute("""
        INSERT INTO disaster_alerts (evacuation_center_id, volcano_monitoring_id, alert_level, description)
        VALUES (%s, %s, %s, %s)
        """, (evacuation_center_id, volcano_monitoring_id, alert_level, description))
        conn.commit()
        print("Disaster alert added successfully.")
    except Error as e:
        print(f"Error while adding alert: {e}")

# Read Disaster Alerts
def read_alerts():
    try:
        cursor.execute("SELECT * FROM disaster_alerts")
        disaster_alerts = cursor.fetchall()
        if disaster_alerts:
            print("\n==============================================")
            print("--- List of Alerts ---")
            print("{:<5} {:<20} {:<50} {:<10} {:<10}".format('ID', 'Alert Level', 'Description', 'Evacuation Center ID', 'Volcano Monitoring ID'))
            for alert in disaster_alerts:
                print("{:<5} {:<20} {:<50} {:<10} {:<10}".format(alert[0], alert[3], alert[4], alert[1], alert[2]))
            print("==============================================")
        else:
            print("No alerts found.")
            print("==============================================")
    except Error as e:
        print(f"Error while retrieving alerts: {e}")

# Update Disaster Alerts
def update_alert():
    try:
        print("\n==============================================")
        print("--- UPDATE: Disaster Alert Form ---")
        print("==============================================")
        alert_id = input("Enter the ID of the alert to update: ")
        evacuation_center_id = input("Evacuation center ID: ")
        volcano_monitoring_id = input("Volcano Monitor ID: ")
        alert_level = input("Alert Level: ")
        description = input("Description: ")
        cursor.execute("""
        UPDATE disaster_alerts
        SET evacuation_center_id = %s, volcano_monitoring_id = %s, alert_level = %s, description = %s
        WHERE id = %s
        """, (evacuation_center_id, volcano_monitoring_id, alert_level, description, alert_id))
        conn.commit()
        print("")
        print("Disaster alert updated successfully.")
        print("==============================================")
    except Error as e:
        print(f"Error while updating alert: {e}")

# Delete Disaster Alerts
def delete_alert():
    try:
        alert_id = input("Enter the ID of the alert to delete: ")
        cursor.execute("DELETE FROM disaster_alerts WHERE id = %s", (alert_id,))
        conn.commit()
        print(f"Alert {alert_id} deleted successfully.")
    except Error as e:
        print(f"Error while deleting alert: {e}")
# DISASTER ALERTS CRUD FUNCTIONS (END)

#====================================================================================================
# RESOURCES CRUD FUNCTIONS (START)
# Create Resource
def create_resource():
    try:
        print("\n==============================================")
        print("--- ADD: Resource Form ---")
        print("==============================================")
        evacuation_center_id = input("Enter the evacuation center ID: ")
        type = input("Type: ")
        quantity = input("Quantity: ")
        cursor.execute("""
        INSERT INTO resources (evacuation_center_id, type, quantity)
        VALUES (%s, %s, %s)
        """, (evacuation_center_id, type, quantity))
        conn.commit()
        print("Resource added successfully.")
    except Error as e:
        print(f"Error while adding alert: {e}")

# Read Resources
def read_resources():
    try:
        cursor.execute("SELECT * FROM resources")
        resources = cursor.fetchall()
        if resources:
            print("\n==============================================")
            print("--- List of Resources ---")
            print("{:<5} {:<20} {:<10} {:<20}".format('ID', 'Type', 'Quantity', 'Evacuation Center ID'))
            for resource in resources:
                print("{:<5} {:<20} {:<10} {:<20}".format(resource[0], resource[2], resource[3], resource[1]))
            print("==============================================")
        else:
            print("No resources found.")
            print("==============================================")
    except Error as e:
        print(f"Error while retrieving resources: {e}")

# Update Resource
def update_resource():
    try:
        print("\n==============================================")
        print("--- UPDATE: Resource Form ---")
        print("==============================================")
        resource_id = input("Enter the ID of the resource to update: ")
        evacuation_center_id = input("Evacuation center ID: ")
        type = input("Type: ")
        quantity = input("Quantity: ")
        cursor.execute("""
        UPDATE resources
        SET evacuation_center_id = %s, type = %s, quantity = %s
        WHERE id = %s
        """, (evacuation_center_id, type, quantity, resource_id))
        conn.commit()
        print("")
        print("Resource updated successfully.")
        print("==============================================")
    except Error as e:
        print(f"Error while updating resource: {e}")

# Delete Resource
def delete_resource():
    try:
        alert_id = input("Enter the ID of the resource to delete: ")
        cursor.execute("DELETE FROM resources WHERE id = %s", (alert_id,))
        conn.commit()
        print(f"Resource {alert_id} deleted successfully.")
    except Error as e:
        print(f"Error while deleting resource: {e}")
# RESOURCES CRUD FUNCTIONS (END)

#====================================================================================================
# Main loop
while True:
    display_menu()
    choice = input("Choose an option: ")
    
    if choice == "1":
        while True:
            evacuation_center_menu()
            sub_choice = input("Choose an option: ")
            if sub_choice == "1":
                create_evacuation_center()
            elif sub_choice == "2":
                read_evacuation_centers()
            elif sub_choice == "3":
                update_evacuation_center()
            elif sub_choice == "4":
                delete_evacuation_center()
            elif sub_choice == "5":
                break
            else:
                print("Invalid option. Please try again.")

    elif choice == "2":
        while True:
            residents_menu()
            sub_choice = input("Choose an option: ")
            if sub_choice == "1":
                create_resident()
            elif sub_choice == "2":
                read_residents()
            elif sub_choice == "3":
                update_resident()
            elif sub_choice == "4":
                delete_resident()
            elif sub_choice == "5":
                break
            else:
                print("Invalid option. Please try again.")

    elif choice == "3":
        while True:
            resources_menu()
            sub_choice = input("Choose an option: ")
            if sub_choice == "1":
                create_resource()
            elif sub_choice == "2":
                read_resources()
            elif sub_choice == "3":
                update_resource()
            elif sub_choice == "4":
                delete_resource()
            elif sub_choice == "5":
                break
            else:
                print("Invalid option. Please try again.")
    
    elif choice == "4":
        while True:
            monitorings_menu()
            sub_choice = input("Choose an option: ")
            if sub_choice == "1":
                create_monitoring()
            elif sub_choice == "2":
                read_monitorings()
            elif sub_choice == "3":
                update_monitoring()
            elif sub_choice == "4":
                delete_monitoring()
            elif sub_choice == "5":
                break
            else:
                print("Invalid option. Please try again.")

    elif choice == "5":
        while True:
            alerts_menu()
            sub_choice = input("Choose an option: ")
            if sub_choice == "1":
                create_alert()
            elif sub_choice == "2":
                read_alerts()
            elif sub_choice == "3":
                update_alert()
            elif sub_choice == "4":
                delete_alert()
            elif sub_choice == "5":
                break
            else:
                print("Invalid option. Please try again.")
    
    elif choice == "6":
        print("Exiting...")
        break
    
    else:
        print("Invalid option. Please try again.")