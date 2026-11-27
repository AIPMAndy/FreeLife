import json,re,pathlib,datetime
p=pathlib.Path(__file__).resolve().parents[1]
r=json.loads((p/'data/opportunities.json').read_text()); fields={'id','category','region','priority','title','benefit','status','deadline','entry','steps','conditions','source','source_type','checked'}
assert len({x['id'] for x in r})==len(r)
for x in r:
 assert set(x)==fields and all(isinstance(v,str) and v.strip() for v in x.values()),x
 assert x['source'].startswith('https://'),x
 assert x['priority'] in {'P0','P1','P2'},x
 datetime.date.fromisoformat(x['checked'])
 if re.fullmatch(r'\d{4}-\d\d-\d\d',x['deadline']):datetime.date.fromisoformat(x['deadline'])
h=(p/'index.html').read_text();embedded=re.search(r'const DATA=(\[.*?\]);\n',h,re.S); assert embedded and json.loads(embedded.group(1))==r
print(f'PASS: {len(r)} unique records, complete fields, source URLs and embedded data verified. Network availability and account eligibility not tested.')
