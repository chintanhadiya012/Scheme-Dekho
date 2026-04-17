from flask import Flask, render_template, request, jsonify
import sqlite3
import os

app = Flask(__name__)
DB_PATH = os.path.join(os.path.dirname(__file__), 'database', 'schemes.db')

def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

# ── Routes ────────────────────────────────────────────────────────────────────

@app.route('/')
def home():
    db = get_db()
    total_schemes = db.execute('SELECT COUNT(*) as c FROM schemes').fetchone()['c']
    categories = db.execute('SELECT COUNT(DISTINCT category) as c FROM schemes').fetchone()['c']
    db.close()
    return render_template('index.html', total_schemes=total_schemes, categories=categories)

@app.route('/dashboard')
def dashboard():
    db = get_db()
    categories = db.execute('SELECT DISTINCT category FROM schemes ORDER BY category').fetchall()
    total = db.execute('SELECT COUNT(*) as c FROM schemes').fetchone()['c']
    db.close()
    return render_template('dashboard.html', categories=[r['category'] for r in categories], total=total)

@app.route('/eligibility')
def eligibility():
    return render_template('eligibility.html')

@app.route('/schemes')
def schemes():
    db = get_db()
    cat = request.args.get('category', '')
    q   = request.args.get('q', '')
    sql = 'SELECT * FROM schemes WHERE 1=1'
    params = []
    if cat:
        sql += ' AND category = ?'; params.append(cat)
    if q:
        sql += ' AND (name LIKE ? OR description LIKE ?)'; params += [f'%{q}%', f'%{q}%']
    rows = db.execute(sql + ' ORDER BY name', params).fetchall()
    cats = db.execute('SELECT DISTINCT category FROM schemes ORDER BY category').fetchall()
    db.close()
    return render_template('schemes.html',
                           schemes=[dict(r) for r in rows],
                           categories=[r['category'] for r in cats],
                           selected_cat=cat, query=q)

@app.route('/scheme/<int:sid>')
def scheme_detail(sid):
    db = get_db()
    s = db.execute('SELECT * FROM schemes WHERE id=?', (sid,)).fetchone()
    db.close()
    if not s:
        return "Scheme not found", 404
    return render_template('scheme_detail.html', scheme=dict(s))

@app.route('/verifier')
def verifier():
    return render_template('verifier.html')

# ── API ───────────────────────────────────────────────────────────────────────

@app.route('/api/check_eligibility', methods=['POST'])
def check_eligibility():
    data = request.json
    age    = int(data.get('age', 0))
    income = int(data.get('income', 0))
    caste  = data.get('caste', '').lower()
    gender = data.get('gender', '').lower()
    bpl    = data.get('bpl', False)

    db = get_db()
    schemes = db.execute('SELECT * FROM schemes').fetchall()
    db.close()

    matched = []
    for s in schemes:
        ok = True
        if s['min_age'] and age < s['min_age']: ok = False
        if s['max_age'] and age > s['max_age']: ok = False
        if s['max_income'] and income > s['max_income']: ok = False
        if s['caste_required'] and s['caste_required'].lower() != 'all' and caste not in s['caste_required'].lower(): ok = False
        if s['gender_required'] and s['gender_required'].lower() != 'all' and gender != s['gender_required'].lower(): ok = False
        if s['bpl_required'] and not bpl: ok = False
        if ok:
            matched.append({'id': s['id'], 'name': s['name'], 'category': s['category'], 'description': s['description'], 'official_link': s['official_link']})

    return jsonify({'count': len(matched), 'schemes': matched})

@app.route('/api/verify_scheme', methods=['POST'])
def verify_scheme():
    data = request.json
    name = data.get('name', '').strip()
    db = get_db()
    results = db.execute(
        'SELECT id, name, category, ministry, official_link FROM schemes WHERE name LIKE ?',
        (f'%{name}%',)
    ).fetchall()
    db.close()
    if results:
        return jsonify({'found': True, 'schemes': [dict(r) for r in results]})
    return jsonify({'found': False, 'message': 'No matching scheme found. It may be fake or misspelled.'})

@app.route('/api/schemes')
def api_schemes():
    db = get_db()
    rows = db.execute('SELECT id,name,category,ministry FROM schemes ORDER BY name').fetchall()
    db.close()
    return jsonify([dict(r) for r in rows])

if __name__ == '__main__':
    app.run(debug=True, port=5000)
