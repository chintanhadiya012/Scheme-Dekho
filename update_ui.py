import os

def update_css():
    filepath = os.path.join('static', 'css', 'style.css')
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Colors
    content = content.replace('--gold:       #F0C040;', '--accent:     #0EA5E9;')
    content = content.replace('--gold-lt:    #FFD966;', '--accent-lt:  #38BDF8;\n  --accent-dk:  #0284C7;')
    content = content.replace('var(--gold)', 'var(--accent)')
    content = content.replace('var(--gold-lt)', 'var(--accent-lt)')
    content = content.replace('rgba(240,192,64,', 'rgba(14,165,233,')
    content = content.replace('#d4a200', 'var(--accent-dk)')
    
    # Fonts
    content = content.replace("font-family: 'Roboto', sans-serif", "font-family: 'Inter', sans-serif")
    content = content.replace("font-family: 'Syne', sans-serif", "font-family: 'Plus Jakarta Sans', sans-serif")
    content = content.replace("font-family: 'Playfair Display', serif", "font-family: 'Plus Jakarta Sans', sans-serif")
    
    # Specific class names updates
    content = content.replace('.line-gold', '.line-accent')
    content = content.replace('.btn-gold', '.btn-accent')
    content = content.replace('.tag.gold', '.tag.accent')
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

    # HTML changes
    idx_filepath = os.path.join('templates', 'index.html')
    with open(idx_filepath, 'r', encoding='utf-8') as f:
        idx_content = f.read()
    idx_content = idx_content.replace('line-gold', 'line-accent')
    with open(idx_filepath, 'w', encoding='utf-8') as f:
        f.write(idx_content)

if __name__ == '__main__':
    update_css()
