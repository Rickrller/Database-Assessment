"""
Docstring
Code used to look up swimmers in a database based off modes, such as time and placing.
Made by Rick Wang
"""
import sqlite3
DATABASE = 'Top_Swimmers.db'

# Variable decleration
Zero = 0
Look_Up_Type = "Empty"
Negative_Check = Zero


# Function for look up swimmer
def Look_Up_Swimmer():
    # Search setup
    Look_Up_Value = Zero
    if Look_Up_Type == "Time":  # Time based search
        while True:
            try:
                Look_Up_Value = int(input('Please enter a time (Milliseconds): '))  # Time input
                if Look_Up_Value > Negative_Check:
                    print("Looking up swimmers...")
                    break
                else:
                    print('Please enter a positive number!')  # Negative number detected
            except ValueError:  # Invalid input detected
                print('Invalid time!')

    if Look_Up_Type == "Placing":  # Placing based search
        while True:
            try:
                Look_Up_Value = int(input('Please enter a placement: '))  # Placement input
                if Look_Up_Value > Negative_Check:
                    print("Looking up swimmer...")
                    break
                else:
                    print('Please enter a positive number!')  # Negative number detected
            except ValueError:  # Invalid input detected
                print('Invalid placing!')

    # SQL Code
    with sqlite3.connect(DATABASE) as db:
        db = sqlite3.connect('Top_Swimmers.db')
        cursor = db.cursor()
        if Look_Up_Type == "Time":  # Time search
            sql = "SELECT Swimmer_Name, Fastest_50_Free_Milliseconds, Country, World_Placing, Event FROM swimmers WHERE Fastest_50_Free_Milliseconds < ?;"
        if Look_Up_Type == "Placing":  # Placement search
            sql = "SELECT Swimmer_Name, Fastest_50_Free_Milliseconds, Country, World_Placing, Event FROM swimmers WHERE World_Placing = ?;"
        # Execute search
        cursor.execute(sql, (Look_Up_Value,))
        results = cursor.fetchall()
        # Print results
        for swimmer in results:
            print(f'Swimmer: {swimmer[0]}. Speed: {swimmer[1]/1000} seconds. Country: {swimmer[2]}. Event the time was taken: {swimmer[4]}. Current placing in the world: {swimmer[3]}.') 
        print("Lookup Complete.")


# User inputs
while True:
    Look_Up_Mode = input('Please enter lookup mode (Time/Placing): ')  # Search mode input
    try:
        if Look_Up_Mode.lower() == "time":
            Look_Up_Type = "Time"  # Set mode to time
            Look_Up_Swimmer()
        elif Look_Up_Mode.lower() == "placing":
            Look_Up_Type = "Placing"  # Set mode to placing
            Look_Up_Swimmer()
        else:
            print('Invalid mode! Please make sure no mispellings were made and no numbers were inputted!')  # Wrong spelling error
    except ValueError:
        print('Invalid mode! Please make sure no mispellings were made and no numbers were inputted!')  # Value error
