import os

file_path = "c:/Users/Angus/Desktop/RuleGems/lang.yml"

mapping = {
    "&7": "&#F1F5F9",
    "&8": "&#CFD8DC",
    "&f": "&#FFFFFF",
    "&b": "&#CDE0F5",
    "&3": "&#82B1FF",
    "&9": "&#A3C2DE",
    "&c": "&#E63946",
    "&4": "&#C62828",
    "&6": "&#F4D03F",
    "&e": "&#FFE066",
    "&a": "&#69DB7C",
    "&2": "&#51CF66",
    "&5": "&#B39DDB",
    "&d": "&#F48FB1",
    "&1": "&#3B5BDB",
    "&0": "&#212529"
}

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

for k, v in mapping.items():
    content = content.replace(k, v)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Colors updated successfully in lang.yml")
