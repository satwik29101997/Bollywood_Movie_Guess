import json, csv, re

# load existing hints
path = r"c:\Users\Dell\Documents\GitHub\Bollywood_Movie_Guess\index.html"
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()
hints_existing = set(re.findall(r"hint: '([^']*)'", content))

clean = lambda h: re.sub(r"\s*\(quote #[0-9]+\)|\s*\(meme #[0-9]+\)", '', h).strip()
new_entries = []

def add(character, actor, movie, hint):
    if hint is None:
        return
    hintc = clean(hint)
    if hintc and hintc not in hints_existing and hintc not in [e['hint'] for e in new_entries]:
        new_entries.append({'characterFull':character, 'actor':actor, 'movieFull':movie, 'hint':hintc})

# process json files
for fname in [r"c:\Users\Dell\Downloads\bollywood_dialogues_500.json",
              r"c:\Users\Dell\Downloads\movie_quote_game_dataset.json",
              r"c:\Users\Dell\Downloads\bollywood_meme_dialogues_250.json"]:
    try:
        with open(fname, 'r', encoding='utf-8') as f:
            data = json.load(f)
            for d in data:
                if 'question' in d:
                    add(d.get('character'), d.get('answer_actor'), d.get('answer_movie'), d.get('question',''))
                else:
                    add(d.get('characterFull'), d.get('actor'), d.get('movieFull'), d.get('hint',''))
    except FileNotFoundError:
        print(f"missing {fname}")

# process csv file
try:
    with open(r"c:\Users\Dell\Downloads\bollywood_dialogues_1200.csv","r",encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for d in reader:
            add(d.get('characterFull'), d.get('actor'), d.get('movieFull'), d.get('hint',''))
except FileNotFoundError:
    print("missing csv")

print(len(new_entries))
for e in new_entries:
    print(e)
