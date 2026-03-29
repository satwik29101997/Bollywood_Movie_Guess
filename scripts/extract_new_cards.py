import json, csv, re

# Load existing hints from HTML
path = r"c:\Users\Dell\Documents\GitHub\Bollywood_Movie_Guess\index.html"
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

# Extract all card entries from HTML
html_cards = []
html_hints_set = set()
pattern = r"\{characterFull:\s*'([^']*)',\s*actor:\s*'([^']*)',\s*movieFull:\s*'([^']*)',\s*hint:\s*'([^']*)'\}"
for match in re.finditer(pattern, content):
    card = {
        'characterFull': match.group(1),
        'actor': match.group(2),
        'movieFull': match.group(3),
        'hint': match.group(4)
    }
    html_cards.append(card)
    html_hints_set.add(card['hint'].lower())

# Load all records from JSON file
json_records = []
try:
    with open(r"c:\Users\Dell\Documents\GitHub\Bollywood_Movie_Guess\bollywood_dialogues_list.json", 'r', encoding='utf-8') as f:
        json_records = json.load(f)
except FileNotFoundError:
    print("Error: bollywood_dialogues_list.json not found")

# Function to clean hints
clean = lambda h: re.sub(r"\s*\(quote #[0-9]+\)|\s*\(meme #[0-9]+\)", '', h).strip()

# VALIDATION: Find records in JSON but not in HTML
print("=" * 100)
print("VALIDATION: Records in bollywood_dialogues_list.json but NOT in index.html")
print("=" * 100)

missing_in_html = []
seen_hints = set()

for record in json_records:
    hint = record.get('hint', '').strip()
    hint_lower = hint.lower()
    
    # Check for duplicate hints and if hint exists in HTML
    if hint_lower not in seen_hints and hint_lower not in html_hints_set:
        missing_in_html.append(record)
        seen_hints.add(hint_lower)

if missing_in_html:
    print(f"\nFound {len(missing_in_html)} records in JSON but NOT in HTML:\n")
    print("Copy the following records to index.html (in the 'cards' array):\n")
    print("JavaScript format:\n")
    
    for i, record in enumerate(missing_in_html, 1):
        char = record.get('characterFull', '')
        actor = record.get('actor', '')
        movie = record.get('movieFull', '')
        hint = record.get('hint', '')
        
        # Escape single quotes in strings
        char = char.replace("'", "\\'")
        actor = actor.replace("'", "\\'")
        movie = movie.replace("'", "\\'")
        hint = hint.replace("'", "\\'")
        
        print(f"      {{characterFull: '{char}', actor: '{actor}', movieFull: '{movie}', hint: '{hint}'}},")
    
    print("\n")
else:
    print("\n✓ All JSON records are present in HTML file. No missing records found.")

print("=" * 100)
print(f"Total HTML cards: {len(html_cards)}")
print(f"Total JSON records: {len(json_records)}")
print(f"Missing in HTML: {len(missing_in_html)}")
print("=" * 100)
