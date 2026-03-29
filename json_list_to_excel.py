import json
from openpyxl import Workbook

# Load JSON file
path = r"C:\Users\Dell\Documents\GitHub\Bollywood_Movie_Guess\bollywood_dialogues_list.json"
with open(path, 'r', encoding='utf-8') as file:
    data = json.load(file)

# Create Excel workbook
wb = Workbook()
ws = wb.active
ws.title = "Bollywood Dialogues"

# Add headers
headers = ["Serial No", "Character", "Actor", "Movie", "Hint", "ID"]
ws.append(headers)

# Add data rows
for index, item in enumerate(data, start=1):
    row = [
        index,                          # Serial Number
        item.get("characterFull", ""),
        item.get("actor", ""),
        item.get("movieFull", ""),
        item.get("hint", ""),
        item.get("id", "")
    ]
    ws.append(row)

# Save Excel file
wb.save("Bollywood_Game_Data.xlsx")

print("Excel file created successfully!")