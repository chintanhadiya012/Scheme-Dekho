import os
import glob

def replace_in_file(filepath, old_str, new_str):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    if old_str in content:
        content = content.replace(old_str, new_str)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)

search_paths = glob.glob('templates/*.html') + ['static/css/style.css']

for filepath in search_paths:
    # URL in base.html
    replace_in_file(filepath, 
        'href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700;800;900&display=swap"',
        'href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap"')
    
    # CSS rules
    replace_in_file(filepath, "'Outfit'", "'Inter'")

print("Fonts updated to Inter!")
