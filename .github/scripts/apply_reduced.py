from pathlib import Path
import re

p = Path('index.html')
s = p.read_text(encoding='utf-8')

replacements = [
    ('<meta content="Veronika Dimitrov — Strategic Briefing" property="og:title"/>', '<meta content="Veronika Dimitrov — Reduced Version" property="og:title"/>'),
    ('<div class="hero-tagline">A Strategic Briefing</div>', '<div class="hero-tagline">Reduced Version</div>\n<div style="font-family:var(--sans);font-size:12px;letter-spacing:0.12em;text-transform:uppercase;color:#888580;margin-top:-18px;">Updated September 6, 2026</div>'),
    ('can figure things out', 'could figure things out'),
    ('very cheap to pay the bills', 'very inexpensive to pay the bills'),
    ('active funded project, with real students', 'active funded project with real students'),
    ('mangos', 'mangoes'),
    ('<div class="qa-question">Progress Report: How would you describe the progress achieved over the last two years?</div>', '<div class="qa-question">How would you describe the progress you\'ve achieved over the last 2 years?</div>'),
    ("<div class=\"qa-question\">Hiring Context: Why did you hire me two years ago if the primary focus at that stage was just 'letting the garden mature'?</div>", '<div class="qa-question">One question that keeps coming up for me is this: why did you hire me two years ago to help if the primary focus at that stage was allowing the garden to mature?</div>'),
    ('<div class="qa-question">Transparency Gap: Why is the progression currently unclear to an observer?</div>', '<div class="qa-question">I think the bigger question right now is why the progression isn\'t clearer. Usually, when someone feels deeply connected to a mission, they\'re naturally thinking about how it grows and evolves over time. Since I\'m not hearing that level of specificity, I\'m wondering why. Is it something you haven\'t thought through yet? Does planning feel overwhelming? Or is there something else?</div>'),
    ('<div class="qa-question">Milestone Planning: What are your specific, concrete goals for 1, 3, and 5 years from now that bridge the gap from where you are today to your long-term vision?</div>', '<div class="qa-question">What are your goals 1 year from now? 3 years from now? Five years from now?</div>'),
    ('Notes and status are saved locally in their browser.', 'Notes and status are saved locally in your browser.'),
    ('Click to open the full outreach board when she is ready to review or make calls.', 'Click to open the full outreach board when you are ready to review or make calls.'),
    ('<div class="section-tag" style="color:var(--gold);">Section 8</div>\n', ''),
]

for old, new in replacements:
    if old not in s:
        raise SystemExit(f'Missing expected text: {old[:120]}')
    s = s.replace(old, new)

s = s.replace('NWKids and .', 'NWKids.')

old_scaling = """<div class=\"qa-question\">Scaling Vision: What does 'taking this model elsewhere' look like in practice?</div><p>Take what worked in Puerto Vallarta, bring it back to Seattle, test it with youth in the community, and prove the model before trying to scale further.</p>
<div class=\"qa-answer\"></div>"""
new_scaling = """<div class=\"qa-question\">One last question. You mentioned wanting to take this model elsewhere. Can you paint a specific picture for me? What does that look like? Do you picture acquiring another piece of land? Training community leaders? etc</div>
<div class=\"qa-answer\">Take what worked in Puerto Vallarta, bring it back to Seattle, test it with youth in the community, and prove the model before trying to scale further.</div>"""
if old_scaling not in s:
    raise SystemExit('Missing expected scaling block')
s = s.replace(old_scaling, new_scaling)

income_pattern = re.compile(r'\n<div class="qa-item">\s*\n<div class="qa-question">Income Velocity: Is there a faster way for you to make money online without starting a business for it\?</div>\s*\n<div class="qa-answer">.*?</div>\s*\n</div>', re.S)
s, n = income_pattern.subn('', s, count=1)
if n != 1:
    raise SystemExit(f'Income Velocity block removal count={n}')

for x in ['Reduced Version','Updated September 6, 2026',"How would you describe the progress you've achieved over the last 2 years?",'What are your goals 1 year from now? 3 years from now? Five years from now?','very inexpensive to pay the bills']:
    if x not in s:
        raise SystemExit(f'Expected result missing: {x}')
for x in ['A Strategic Briefing','Income Velocity:','Section 8</div>','NWKids and .','their browser','when she is ready','mangos']:
    if x in s:
        raise SystemExit(f'Stale text still present: {x}')

p.write_text(s, encoding='utf-8')

t = Path('nwkids_funding_alignment_call_tracker_v2.html')
if t.exists():
    ts = t.read_text(encoding='utf-8')
    ts = ts.replace('Interactive grant and partnership outreach checklist for NWKids and The Pauli Effect.', 'Interactive grant and partnership outreach checklist for NWKids.')
    ts = ts.replace('NWKids / Pauli Funding Tracker', 'NWKids Funding Tracker')
    ts = ts.replace('Notes and status are saved locally in their browser.', 'Notes and status are saved locally in your browser.')
    t.write_text(ts, encoding='utf-8')
