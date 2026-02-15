from datetime import date 
# Using date.today was an idea help through GPT, at first i wanted to hard code a date in but realized thats not really
# effecient or correct so I asked GPT "How can i check the date to the current time and date of present day on python?"
# You will see this refenced again later when we use the acutal date command when we check the validity of the tickets 

import mysql.connector
# In theme of mysql.connector library, we did use GPT to get an understanding how we bridge the gap between mysql to this python file as well as
# the feuatures within the library such as .cursor() .execute() .fetchone() and etc. Specifcaly I asked GPT 
# "How am i suppose to bridge the gap between my DB written on mysql work bench that is connected to a AWS account to connect to my local python script?" and 
# I did asked "Give me a overview on the certain commands and feaautures of the library, be sure to inlcude logic and sytnax"

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


# =========== Ticket # validation ===========
# Without including this function, we'd have to inherently input the contents of this function 
# in every elif statement of the while loop within the main function so in short, we are creating 
# efficiency

def get_ticket_no():
    while True:
        s = input("Enter ticket number: ").strip()
        if s.isdigit():
            return int(s)
        print("Ticket number must be digits only.")


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
            print("Goodbye.")
            break



        elif choice == "cn":
            ticketno = get_ticket_no()
            cur = db.cursor() 
            cur.execute("SELECT ticketno FROM tickets WHERE ticketno = %s", (ticketno,))
            row = cur.fetchone()
            cur.close()

            if row:
                print("Ticket exists.\n")
            else:
                print("Ticket does NOT exist.\n")



        elif choice == "cv":
            ticketno = get_ticket_no()
            cur = db.cursor()
            cur.execute("SELECT validdate FROM tickets WHERE ticketno = %s", (ticketno,))
            row = cur.fetchone()
            cur.close()

            if not row:
                print("Ticket does NOT exist.\n")
            else:
                validdate = row[0] 
                if validdate >= date.today(): 
                # Using date.today was an idea help through GPT, at first i wanted to hard code a date in but realized thats not really
                # effecient or correct so I asked GPT "How can i check the date to the current time and date of present day on python?"
                    print("Ticket is VALID.\n")
                else:
                    print("Ticket is NOT valid (expired).\n")



        elif choice == "cp":
            cur = db.cursor()
            cur.execute("SELECT COALESCE(SUM(price), 0) FROM tickets")
            total = cur.fetchone()[0]
            cur.close()

            print(f"Total price of all sold tickets: {total}\n")

        else:
            print("Invalid option.\n")



    # =========== Closing the DB ===========
    try:
        if db:
            db.close()
    except:
        pass

if __name__ == "__main__":
    main()