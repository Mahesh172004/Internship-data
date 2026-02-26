from database.connection import get_connection

# CREATE
def add_patient():
    connection = get_connection()
    cursor = connection.cursor()

    name = input("Enter patient name: ")
    age = int(input("Enter age: "))
    gender = input("Enter gender: ")

    query = "INSERT INTO patients (name, age, gender) VALUES (%s, %s, %s)"
    cursor.execute(query, (name, age, gender))
    connection.commit()

    print("✅ Patient added successfully!\n")
    connection.close()


# READ
def view_patients():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM patients")
    rows = cursor.fetchall()

    print("\n--- Patient List ---")
    for row in rows:
        print(f"ID: {row[0]}, Name: {row[1]}, Age: {row[2]}, Gender: {row[3]}")
    print()

    connection.close()


# UPDATE
def update_patient():
    connection = get_connection()
    cursor = connection.cursor()

    patient_id = int(input("Enter patient ID: "))
    name = input("Enter new name: ")
    age = int(input("Enter new age: "))
    gender = input("Enter new gender: ")

    query = """
    UPDATE patients
    SET name=%s, age=%s, gender=%s
    WHERE patient_id=%s
    """
    cursor.execute(query, (name, age, gender, patient_id))
    connection.commit()

    print("✅ Patient updated successfully!\n")
    connection.close()


# DELETE
def delete_patient():
    connection = get_connection()
    cursor = connection.cursor()

    patient_id = int(input("Enter patient ID to delete: "))

    query = "DELETE FROM patients WHERE patient_id=%s"
    cursor.execute(query, (patient_id,))
    connection.commit()

    print("✅ Patient deleted successfully!\n")
    connection.close()