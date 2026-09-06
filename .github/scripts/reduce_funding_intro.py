from pathlib import Path

p = Path('index.html')
s = p.read_text(encoding='utf-8')
old = '''<div class="funding-tracker-container">
<h2>Funding Alignment Outreach Board</h2>
<div class="body-text">
<p>This board maps grant, corporate, university, philanthropic, and public-sector opportunities that align with New World Kids, AI for Good, food security, youth programs, regenerative agriculture, digital equity, and community resilience.</p>
<p>Each target can be marked as called, notes can be saved locally in the browser, and the red strike line makes completed outreach easy to scan during follow-up work.</p>
</div>'''
new = '''<div class="funding-tracker-container">
<h2>Funding Alignment Outreach Board</h2>
<div class="body-text">
<p>While I’m here in Seattle, I’ve been mapping grants, partners, universities, companies, and public programs that could support New World Kids.</p>
<p>I’m using the board below to track who I contact, what they say, and what the next step is.</p>
</div>'''
if old not in s:
    raise SystemExit('Expected funding intro not found')
s = s.replace(old, new, 1)
old2 = '<span>Click to open the full outreach board when you are ready to review or make calls. The rest of the document stays short and easy to scan.</span>'
new2 = '<span>Open the full outreach board to see the organizations I’m working through.</span>'
if old2 not in s:
    raise SystemExit('Expected funding summary not found')
s = s.replace(old2, new2, 1)
p.write_text(s, encoding='utf-8')
