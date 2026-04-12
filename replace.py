import os
import re

directory = 'c:/Users/Angus/Desktop/RuleGems/src/main/java/org/cubexmc'
pattern = re.compile(r"ChatColor\.translateAlternateColorCodes\('&',\s*(.*?)\)")
count = 0

for root, dirs, files in os.walk(directory):
    for file in files:
        if file.endswith(".java") and file != "ColorUtils.java":
            path = os.path.join(root, file)
            with open(path, 'r', encoding='utf-8') as f:
                content = f.read()

            new_content = pattern.sub(r"org.cubexmc.utils.ColorUtils.translateColorCodes(\1)", content)
            
            if new_content != content:
                with open(path, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f"Updated {file}")
                count += 1

print(f"Total updated: {count}")
