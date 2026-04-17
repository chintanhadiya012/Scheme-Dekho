import os

def update_htmls():
    templates_dir = 'templates'
    if not os.path.exists(templates_dir):
        return

    for filename in os.listdir(templates_dir):
        if filename.endswith('.html'):
            filepath = os.path.join(templates_dir, filename)
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()

            new_content = content.replace('var(--gold)', 'var(--accent)')
            new_content = new_content.replace('tag gold', 'tag accent')
            new_content = new_content.replace('btn-gold', 'btn-accent')
            new_content = new_content.replace("'Playfair Display',serif", "'Plus Jakarta Sans', sans-serif")
            
            if new_content != content:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(new_content)

if __name__ == '__main__':
    update_htmls()
