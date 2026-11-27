from pathlib import Path
import json,csv
root=Path(__file__).resolve().parents[1]
rows=json.loads((root/'data/opportunities.json').read_text())
raw=json.dumps(rows,ensure_ascii=False).replace('</','<\\/')
(root/'index.html').write_text((root/'scripts/template.html').read_text().replace('/*__DATA__*/[]',raw),encoding='utf-8')
with (root/'data/opportunities.csv').open('w',encoding='utf-8-sig',newline='') as f:
 w=csv.DictWriter(f,fieldnames=rows[0].keys()); w.writeheader();w.writerows(rows)
