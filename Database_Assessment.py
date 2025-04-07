"""Docstring
Code used to look up swimmers in a database."""
import sqlite3


DATABASE = 'Top_Swimmers.db'


def Look_Up_Swimmer():
    Look_Up_Value = 0
    if Look_Up_Type == "Time":
        while True:
            try:
                Look_Up_Value = int(input('Please enter a time (Milliseconds): '))
                break
            except ValueError:
                print('Invalid time!')

    with sqlite3.connect(DATABASE) as db:
        db = sqlite3.connect('Top_Swimmers.db')
        cursor = db.cursor()
        if Look_Up_Type = "Time":
            sql = "SELECT Swimmer_Name, Fastest_50_Free_Milliseconds, Country, World_Placing, Event FROM swimmers WHERE Fastest_50_Free_Milliseconds < ?;"
        if L
        cursor.execute(sql, (Look_Up_Value,))
        results = cursor.fetchall()
        for swimmer in results:
            print(f'Swimmer: {swimmer[0]}. Speed: {swimmer[1]/1000} seconds. Country: {swimmer[2]}. Event the time was taken: {swimmer[4]}. Current placing in the world: {swimmer[3]}.')



Look_Up_Mode = input('Please enter lookup mode (Time/Placing): ')
Time = 0
Placing = 0
Look_Up_Type = "Empty"

if Look_Up_Mode == "Time":
    Look_Up_Type = "Time"
    Look_Up_Swimmer()
elif Look_Up_Mode == "Placing":
    Look_Up_Type = "Placing"
    Look_Up_Swimmer()