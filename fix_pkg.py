import os

directory = 'c:/Users/Angus/Desktop/RuleGems/src/main/java/org/cubexmc'
count = 0

for root, dirs, files in os.walk(directory):
    for file in files:
        if file.endswith(".java"):
            path = os.path.join(root, file)
            with open(path, 'r', encoding='utf-8') as f:
                content = f.read()

            new_content = content.replace("org.bukkit.org.cubexmc.utils.ColorUtils", "org.cubexmc.utils.ColorUtils")
            
            if new_content != content:
                with open(path, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f"Fixed {file}")
                count += 1

print(f"Total fixed: {count}")
