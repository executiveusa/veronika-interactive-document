from pathlib import Path
p=Path('index.html')
s=p.read_text(encoding='utf-8')
marker='<!-- FINAL PRODUCTION SYNC: 2026-09-06 -->'
if marker not in s:
    s=s.replace('</body>', marker+'\n</body>')
p.write_text(s,encoding='utf-8')
