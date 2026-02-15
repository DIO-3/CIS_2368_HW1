import mysql.connector

# =========== DB INFO ===========
HOST = "cis2368spring26.cxxnotgoq7im.us-east-1.rds.amazonaws.com"
USER = "admin"
PASSWORD = "quxZyg-huzgis-jygju7"
DATABASE = "CIS2368springdb"
PORT = 3306

# =========== Creating DB connection function for efficient connectivity ===========
def connect():
    return mysql.connector.connect(
        host=HOST,
        user=USER,
        password=PASSWORD,
        database=DATABASE,
        port=PORT
    )

# =========== Defining menu function for efficiency ===========
def show_menu():
    print("cn - Check ticket number")
    print("cv - Check ticket validity")
    print("cp - Calculate total price")
    print("q - Quit")


def main():
    # =========== Opening the DB ===========
    # We are testing connection to the database first to prevent redundancy and failure when running the main function
    try:
        db = connect()
        print("Connected.\n")
    except:
        print("Could not connect to database. Check credentials/endpoint.")
        return

    # =========== Running the menu loop ===========
    # General functionality will occur in this section of the main function
    while True:
        show_menu()
        choice = input("Select option: ").strip().lower()

        if choice == "q":
            print("Quit")
            break

        elif choice == "cn":
            print ("Check ticket number")

        elif choice == "cv":
            print ("Check ticket validity")

        elif choice == "cp":
            print ("Calculate total price")

    # =========== Closing the DB ===========
    try:
        if db:
            db.close()
    except:
        pass


if __name__ == "__main__":
    main()