import os
import random

categories_data = {
    "Handicrafts": ("Ministry of Textiles", "Financial support and skill development for artisans", "Aadhaar, Artisan Card", "Subsidies, Raw material grants"),
    "Export & Trade": ("Ministry of Commerce", "Boost export readiness and global market access", "Company PAN, IEC Code", "Export subsidies, tax rebates"),
    "Urban Dev": ("Ministry of Housing", "Urban infrastructure and mobility development", "NA", "Development of smart cities infrastructure"),
    "Disaster Relief": ("Ministry of Home Affairs", "Financial aid during natural calamities", "Aadhaar, Bank Account", "Direct cash transfer for rebuilding"),
    "Space & Tech": ("Ministry of Science & Technology", "Space technology grants for startups", "Company Registration, Project Plan", "Grant up to ₹50 Lakh"),
    "Self Help Groups": ("Ministry of Rural Development", "Micro-credit for women-led SHGs", "SHG Group ID, Aadhaar", "Revolving fund, Interest subvention"),
    "Khadi & Coir": ("Ministry of MSME", "Promotion of village industries and coir", "Aadhaar", "Toolkits, Marketing Support"),
    "Ayush": ("Ministry of Ayush", "Promotion of traditional medicine and yoga", "NA", "Subsidies for setting up Ayush centers"),
    "Youth Affairs": ("Ministry of Youth Affairs", "Leadership and skill development for youth", "Aadhaar, Age Proof", "Fellowships and training programs"),
    "Food Processing": ("Ministry of Food Processing", "Subsidies for setting up food parks", "Business Plan, PAN", "Capital subsidy up to 35%"),
}

prefixes = ["Pradhan Mantri", "National", "State", "Atmanirbhar", "Mukhyamantri", "Rashtriya", "Deendayal Upadhyaya", "Swami Vivekananda", "Bharat", "Jan"]
focuses = ["Vikas", "Kalyan", "Samridhhi", "Suraksha", "Utkarsh", "Pragati", "Kaushal", "Unnati", "Sahayata", "Nidhi", "Sampada", "Udyam"]
suffixes = ["Yojana", "Mission", "Abhiyan", "Initiative", "Programme", "Fund"]

new_schemes = []

for category, (ministry, base_desc, base_docs, base_benefits) in categories_data.items():
    for i in range(15): # 10 categories * 15 = 150 schemes
        prefix = random.choice(prefixes)
        focus = random.choice(focuses)
        suffix = random.choice(suffixes)
        name = f"{prefix} {category.split()[0]} {focus} {suffix}"
        
        desc = f"{base_desc} - Phase {i+1}"
        min_age = random.choice([18, None, 21, 16])
        max_age = random.choice([None, 60, 45, 35]) if min_age else None
        max_income = random.choice([None, 250000, 500000, 800000])
        gender = random.choice(["All", "Female"])
        caste = random.choice(["All", "All", "SC/ST", "OBC", "Minority"])
        bpl = random.choice([True, False, False])
        link = "https://india.gov.in"
        
        scheme_tuple = f'    ("{name}","{category}","{ministry}","{desc}",{min_age},{max_age},{max_income},"{gender}","{caste}",{bpl},"{link}","{base_benefits}","{base_docs}"),\n'
        new_schemes.append(scheme_tuple)

# Add to seed_db.py
with open("seed_db.py", "r", encoding="utf-8") as f:
    content = f.read()

# We look for the end of the SCHEMES list
target = ']\n\ndef seed():'
if target in content:
    insertion_content = "".join(new_schemes)
    new_content = content.replace(target, insertion_content + target)
    with open("seed_db.py", "w", encoding="utf-8") as f:
        f.write(new_content)
    print(f"Generated and injected {len(new_schemes)} new schemes.")
else:
    print("Could not find the target injection point ']\n\ndef seed():'. Try a looser match.")
    
    # Looser match
    import re
    match = re.search(r'\]\s*def seed\(\):', content)
    if match:
        idx = match.start()
        new_content = content[:idx] + "".join(new_schemes) + content[idx:]
        with open("seed_db.py", "w", encoding="utf-8") as f:
            f.write(new_content)
        print(f"Generated and injected {len(new_schemes)} new schemes using fallback.")
    else:
        print("FAILED to inject schemes.")
