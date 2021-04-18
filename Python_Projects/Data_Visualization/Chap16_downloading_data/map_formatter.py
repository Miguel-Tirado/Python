import json

filename = 'data/all_week.json'

with open(filename, encoding='utf-8') as f:
    all_eq_data = json.load(f)

readable_file = 'data/readable_month.json'
with open(readable_file, 'w') as f:
    json.dump(all_eq_data, f, indent=4)