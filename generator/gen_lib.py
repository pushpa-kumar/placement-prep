import re, html, json

# Set True only for the GitHub Pages (docs/) build -- Claude Artifacts sandbox
# blocks the outbound network calls progress.js needs, so it's left False
# (the default) for the top-level Claude-mirror build.
PROGRESS_ENABLED = False

def esc(s):
    return html.escape(s or "", quote=True)

def done_checkbox_html(item_id, item_type):
    if not PROGRESS_ENABLED:
        return ""
    return (f'<button type="button" class="done-checkbox" data-item-id="{esc(item_id)}" '
            f'data-item-type="{esc(item_type)}" aria-pressed="false">Mark done</button>')

def progress_script_tag():
    if not PROGRESS_ENABLED:
        return ""
    return '<script type="module" src="progress.js"></script>'

def inline_code(s):
    """Escape then restore `code` spans, and turn \\n\\n into paragraph breaks."""
    e = esc(s)
    e = re.sub(r'`([^`]+)`', r'<code>\1</code>', e)
    paras = e.split("\n\n")
    return "".join(f"<p>{p.replace(chr(10), '<br>')}</p>" for p in paras if p.strip())

_CPP_KEYWORDS = (
    r'alignas|alignof|and|and_eq|asm|auto|bitand|bitor|bool|break|case|catch|char|'
    r'char8_t|char16_t|char32_t|class|compl|concept|const|consteval|constexpr|constinit|'
    r'const_cast|continue|co_await|co_return|co_yield|decltype|default|delete|do|double|'
    r'dynamic_cast|else|enum|explicit|export|extern|false|final|float|for|friend|goto|if|'
    r'inline|int|long|mutable|namespace|new|noexcept|not|not_eq|nullptr|operator|or|or_eq|'
    r'override|private|protected|public|register|reinterpret_cast|requires|return|short|'
    r'signed|sizeof|static|static_assert|static_cast|struct|switch|template|this|'
    r'thread_local|throw|true|try|typedef|typeid|typename|union|unsigned|using|virtual|'
    r'void|volatile|wchar_t|while|xor|xor_eq'
)
_CPP_TYPES = (
    r'string|vector|map|unordered_map|unordered_set|set|multiset|multimap|pair|tuple|'
    r'queue|priority_queue|stack|deque|array|list|forward_list|bitset|complex|size_t|'
    r'ssize_t|int8_t|int16_t|int32_t|int64_t|uint8_t|uint16_t|uint32_t|uint64_t'
)
_CPP_TOKEN_RE = re.compile(
    r'(?P<comment>//[^\n]*|/\*[\s\S]*?\*/)'
    r'|(?P<preproc>^[ \t]*#.*)'
    r'|(?P<string>"(?:\\.|[^"\\\n])*")'
    r'|(?P<char>\'(?:\\.|[^\'\\\n])*\')'
    r'|(?P<number>\b0[xX][0-9a-fA-F]+[uUlL]*\b|\b\d+\.?\d*(?:[eE][+-]?\d+)?[fFuUlL]*\b)'
    r'|(?P<keyword>\b(?:' + _CPP_KEYWORDS + r')\b)'
    r'|(?P<type>\b(?:' + _CPP_TYPES + r')\b)',
    re.MULTILINE,
)

def highlight_cpp(code):
    """Syntax-highlight a C++ snippet into HTML with <span class="tok-*"> wrappers."""
    code = code or ""
    out = []
    pos = 0
    for m in _CPP_TOKEN_RE.finditer(code):
        if m.start() > pos:
            out.append(esc(code[pos:m.start()]))
        out.append(f'<span class="tok-{m.lastgroup}">{esc(m.group())}</span>')
        pos = m.end()
    out.append(esc(code[pos:]))
    return "".join(out)

HEAD_CSS = """
<script async src="https://www.googletagmanager.com/gtag/js?id=G-YDBHJ7316D"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'G-YDBHJ7316D');
</script>

<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@500;600;700&family=IBM+Plex+Sans:wght@400;500;600;700&display=swap" rel="stylesheet">

<style>
  :root{
    --bg:#f7f5ef; --surface:#ffffff; --surface-2:#efece2; --border:#dbd6c8;
    --text:#1d1f23; --text-muted:#5c6070; --text-faint:#83879a;
    --accent:#a3711f; --accent-strong:#8a5e18; --accent-soft:#f1e3c8;
    --real:#217a52; --real-soft:#dcf0e3; --practice:#4a5b7d; --practice-soft:#e4e9f3;
    --gen:#7a4fae; --gen-soft:#efe6f7; --wrong:#b3432b; --wrong-soft:#fbe4dd;
    --code-kw:#1f5fae; --code-type:#0e7c86; --code-str:#1f7a4f; --code-num:#a3711f;
    --code-pre:#7a4fae; --code-com:#83879a;
    --shadow: 0 1px 2px rgba(30,25,10,.06), 0 4px 16px rgba(30,25,10,.05);
    --radius: 10px;
    --mono: 'IBM Plex Mono', ui-monospace, 'SF Mono', Menlo, Consolas, monospace;
    --sans: 'IBM Plex Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
  }
  @media (prefers-color-scheme: dark){
    :root:not([data-theme="light"]){
      --bg:#10131a; --surface:#171b24; --surface-2:#1e2330; --border:#2b3142;
      --text:#e9e7df; --text-muted:#9098ac; --text-faint:#6b7387;
      --accent:#d3a256; --accent-strong:#e8bb72; --accent-soft:#3a2f1c;
      --real:#6fbf8b; --real-soft:#183226; --practice:#8b9bc4; --practice-soft:#1c2333;
      --gen:#c79bea; --gen-soft:#2c2338; --wrong:#e08a72; --wrong-soft:#3a2018;
      --code-kw:#7aa8e0; --code-type:#4fd1d9; --code-str:#6fbf8b; --code-num:#d3a256;
      --code-pre:#c79bea; --code-com:#6b7387;
      --shadow: 0 1px 2px rgba(0,0,0,.4), 0 8px 24px rgba(0,0,0,.35);
    }
  }
  :root[data-theme="dark"]{
    --bg:#10131a; --surface:#171b24; --surface-2:#1e2330; --border:#2b3142;
    --text:#e9e7df; --text-muted:#9098ac; --text-faint:#6b7387;
    --accent:#d3a256; --accent-strong:#e8bb72; --accent-soft:#3a2f1c;
    --real:#6fbf8b; --real-soft:#183226; --practice:#8b9bc4; --practice-soft:#1c2333;
    --gen:#c79bea; --gen-soft:#2c2338; --wrong:#e08a72; --wrong-soft:#3a2018;
    --code-kw:#7aa8e0; --code-type:#4fd1d9; --code-str:#6fbf8b; --code-num:#d3a256;
    --code-pre:#c79bea; --code-com:#6b7387;
    --shadow: 0 1px 2px rgba(0,0,0,.4), 0 8px 24px rgba(0,0,0,.35);
  }

  *{box-sizing:border-box;}
  body{
    margin:0; background:var(--bg); color:var(--text); font-family:var(--sans);
    -webkit-font-smoothing:antialiased; line-height:1.5;
  }
  ::selection{ background:var(--accent-soft); }
  a{ color:var(--accent-strong); }
  a:focus-visible, button:focus-visible, input:focus-visible, select:focus-visible, summary:focus-visible{
    outline:2px solid var(--accent); outline-offset:2px;
  }
  h1,h2,h3{ font-family:var(--mono); font-weight:600; text-wrap:balance; margin:0; }
  code{ font-family:var(--mono); background:var(--surface-2); border-radius:4px; padding:.1em .35em; font-size:.92em; }
  p{ margin:0 0 .8em; }
  p:last-child{ margin-bottom:0; }

  .app{ max-width:1400px; margin:0 auto; padding:0 20px 64px; }

  /* ---------- Shared site nav ---------- */
  .site-nav{
    display:flex; flex-wrap:wrap; gap:4px 18px; align-items:center;
    padding:12px 20px; border-bottom:1px solid var(--border);
    font-family:var(--mono); font-size:.78rem; background:var(--surface);
  }
  .site-nav .brand{ color:var(--text-faint); margin-right:auto; letter-spacing:.04em; }
  .site-nav a{ text-decoration:none; color:var(--text-muted); padding:4px 2px; }
  .site-nav a:hover{ color:var(--accent-strong); }
  .site-nav a.current{ color:var(--accent-strong); border-bottom:2px solid var(--accent); }

  /* ---------- Header ---------- */
  .topbar{ padding:36px 0 20px; border-bottom:1px solid var(--border); }
  .eyebrow{
    font-family:var(--mono); font-size:.72rem; letter-spacing:.12em; text-transform:uppercase;
    color:var(--accent-strong); margin:0 0 10px;
  }
  .topbar h1{ font-size:clamp(1.6rem,3vw,2.2rem); letter-spacing:-.01em; }
  .tagline{ color:var(--text-muted); max-width:66ch; margin:10px 0 0; font-size:.98rem; }

  .stats-strip{ display:flex; flex-wrap:wrap; gap:10px; margin-top:22px; }
  .stat-tile{
    background:var(--surface); border:1px solid var(--border); border-radius:var(--radius);
    padding:10px 16px; min-width:110px; box-shadow:var(--shadow);
  }
  .stat-tile .n{ font-family:var(--mono); font-variant-numeric:tabular-nums; font-size:1.35rem; font-weight:700; }
  .stat-tile .l{ font-size:.72rem; color:var(--text-muted); text-transform:uppercase; letter-spacing:.06em; }

  /* ---------- Layout ---------- */
  .layout{ display:grid; grid-template-columns:250px 1fr; gap:28px; margin-top:24px; align-items:start; }
  @media (max-width:900px){ .layout{ grid-template-columns:1fr; } .sidebar{ order:2; position:static !important; } }

  .sidebar{ position:sticky; top:16px; max-height:calc(100vh - 32px); overflow-y:auto; padding-right:4px; }
  .sidebar h2{ font-size:.72rem; text-transform:uppercase; letter-spacing:.08em; color:var(--text-faint); margin:22px 0 10px; }
  .sidebar h2:first-child{ margin-top:0; }
  .nav-list{ list-style:none; margin:0; padding:0; display:flex; flex-direction:column; gap:2px; }
  .nav-list a{
    display:flex; justify-content:space-between; gap:8px; text-decoration:none; color:var(--text-muted);
    font-size:.85rem; padding:6px 8px; border-radius:6px;
  }
  .nav-list a:hover{ background:var(--surface); color:var(--text); }
  .nav-list .cnt{ font-family:var(--mono); font-variant-numeric:tabular-nums; color:var(--text-faint); font-size:.78rem; }

  .sidebar-note{ font-size:.82rem; color:var(--text-muted); line-height:1.6; }
  .sidebar-note p{ margin:0 0 10px; }
  .sidebar-note strong{ color:var(--text); }

  /* ---------- Section / topic blocks ---------- */
  .topic-section{ margin-bottom:44px; scroll-margin-top:16px; }
  .topic-head{ display:flex; align-items:baseline; gap:10px; margin-bottom:4px; flex-wrap:wrap; }
  .topic-head h2{ font-size:1.2rem; }
  .topic-head .cnt{ font-family:var(--mono); color:var(--text-faint); font-size:.85rem; }
  .topic-desc{ color:var(--text-muted); font-size:.9rem; margin:2px 0 18px; max-width:75ch; }

  .cards{ display:flex; flex-direction:column; gap:10px; }
  .empty-state{ color:var(--text-faint); font-size:.9rem; padding:40px 0; text-align:center; }

  /* ---------- Concept cards ---------- */
  .concept-card{
    background:var(--surface); border:1px solid var(--border); border-radius:var(--radius);
    padding:20px 22px; box-shadow:var(--shadow); margin-bottom:20px; scroll-margin-top:16px;
  }
  .concept-card h3{
    font-size:1.15rem; margin-bottom:12px;
    display:flex; align-items:center; justify-content:space-between; gap:10px; flex-wrap:wrap;
  }
  .concept-card .intro{ font-size:.93rem; color:var(--text-muted); line-height:1.7; margin:0 0 16px; }
  .concept-card .intro p{ margin:0 0 .9em; }
  .example-box{ background:var(--surface-2); border-radius:10px; padding:14px 16px; margin:0 0 14px; }
  .example-box .ex-title{ font-family:var(--mono); font-size:.82rem; font-weight:600; color:var(--accent-strong); margin-bottom:8px; }
  .example-box pre{ background:var(--bg); border:1px solid var(--border); border-radius:8px; padding:12px 14px; overflow-x:auto; margin:0 0 10px; }
  .example-box pre code{ background:none; padding:0; font-size:.8rem; line-height:1.55; white-space:pre; }
  .example-box .ex-explain{ font-size:.87rem; color:var(--text-muted); line-height:1.6; }
  .pitfalls{ margin:14px 0; padding:12px 14px; background:var(--wrong-soft); border-radius:10px; border-left:3px solid var(--wrong); }
  .pitfalls .p-label{ font-family:var(--mono); font-size:.72rem; text-transform:uppercase; letter-spacing:.06em; color:var(--wrong); font-weight:600; margin-bottom:8px; }
  .pitfalls ul{ margin:0; padding-left:18px; font-size:.87rem; color:var(--text); line-height:1.6; }
  .pitfalls li{ margin-bottom:6px; }
  .why-box{ font-size:.85rem; color:var(--accent-strong); border-left:2px solid var(--accent); padding:2px 0 2px 12px; margin:14px 0 0; }
  .related-row{ display:flex; flex-wrap:wrap; gap:6px; margin-top:14px; align-items:center; }
  .related-row .r-label{ font-family:var(--mono); font-size:.72rem; color:var(--text-faint); text-transform:uppercase; letter-spacing:.05em; margin-right:4px; }
  .related-tag{
    font-family:var(--mono); font-size:.74rem; background:var(--surface-2); border:1px solid var(--border);
    color:var(--text-muted); padding:3px 9px; border-radius:100px; text-decoration:none;
  }
  .related-tag:hover{ border-color:var(--accent); color:var(--accent-strong); }

  /* ---------- CP guide theory + example ---------- */
  .theory-block{ font-size:.93rem; color:var(--text-muted); line-height:1.75; margin:0 0 16px; max-width:80ch; }
  .callout-row{ display:flex; flex-wrap:wrap; gap:10px; margin-bottom:18px; }
  .callout{
    flex:1 1 260px; background:var(--surface); border:1px solid var(--border); border-radius:10px;
    padding:12px 14px; font-size:.85rem; color:var(--text-muted); line-height:1.55;
  }
  .callout .c-label{ font-family:var(--mono); font-size:.7rem; text-transform:uppercase; letter-spacing:.06em; color:var(--accent-strong); font-weight:600; display:block; margin-bottom:6px; }

  .example-card{
    background:var(--surface); border:1px solid var(--border); border-radius:var(--radius);
    padding:18px 20px; box-shadow:var(--shadow); margin-bottom:18px; scroll-margin-top:16px;
  }
  .example-card h4{
    font-family:var(--mono); font-size:1rem; margin-bottom:12px; color:var(--text);
    display:flex; align-items:center; justify-content:space-between; gap:10px; flex-wrap:wrap;
  }
  .example-card .section-label{ font-family:var(--mono); font-size:.7rem; text-transform:uppercase; letter-spacing:.06em; color:var(--text-faint); margin:14px 0 6px; }
  .example-card .section-label:first-of-type{ margin-top:0; }
  .example-card .prose{ font-size:.88rem; color:var(--text-muted); line-height:1.65; }
  .example-card pre{ background:var(--surface-2); border-radius:8px; padding:12px 14px; overflow-x:auto; margin:0; }
  .example-card pre code{ background:none; padding:0; font-size:.8rem; line-height:1.55; white-space:pre; }
  .tok-keyword{ color:var(--code-kw); font-weight:600; }
  .tok-type{ color:var(--code-type); }
  .tok-string, .tok-char{ color:var(--code-str); }
  .tok-number{ color:var(--code-num); }
  .tok-preproc{ color:var(--code-pre); }
  .tok-comment{ color:var(--code-com); font-style:italic; }
  .io-row{ display:grid; grid-template-columns:1fr 1fr; gap:10px; }

  /* ---------- Progress tracking ---------- */
  .done-checkbox{
    font-family:var(--mono); font-size:.72rem; font-weight:500; letter-spacing:.02em;
    padding:4px 10px; border-radius:100px; border:1px solid var(--border); background:var(--surface);
    color:var(--text-muted); cursor:pointer; white-space:nowrap;
  }
  .done-checkbox:hover{ border-color:var(--accent); color:var(--accent-strong); }
  .done-checkbox.done{ background:var(--real-soft); border-color:var(--real); color:var(--real); }
  .auth-slot{ margin-left:auto; display:flex; align-items:center; gap:8px; }
  .auth-btn{
    font-family:var(--mono); font-size:.76rem; font-weight:600; padding:6px 12px; border-radius:100px;
    border:1px solid var(--accent); background:var(--accent-soft); color:var(--accent-strong); cursor:pointer;
  }
  .auth-btn:hover{ background:var(--accent); color:var(--surface); }
  .auth-user{ font-family:var(--mono); font-size:.76rem; color:var(--text-muted); }
  .progress-summary{
    display:flex; flex-wrap:wrap; gap:10px; margin:0 0 24px;
  }
  .progress-summary .stat-tile{ cursor:default; }
  .progress-signin-hint{ font-size:.87rem; color:var(--text-muted); margin:0 0 24px; }
  @media (max-width:640px){ .io-row{ grid-template-columns:1fr; } }
  .io-row pre{ background:var(--bg); border:1px solid var(--border); }

  /* ---------- Problem tables ---------- */
  .problems-toolbar{ display:flex; flex-wrap:wrap; gap:10px; margin-bottom:14px; }
  .problems-toolbar input{
    flex:1 1 240px; background:var(--surface); border:1px solid var(--border); color:var(--text);
    border-radius:8px; padding:8px 12px; font-family:var(--sans); font-size:.88rem;
  }
  .table-wrap{ overflow-x:auto; border:1px solid var(--border); border-radius:var(--radius); background:var(--surface); box-shadow:var(--shadow); }
  table.problems{ width:100%; border-collapse:collapse; font-size:.87rem; }
  table.problems th{
    text-align:left; font-family:var(--mono); font-size:.72rem; text-transform:uppercase; letter-spacing:.05em;
    color:var(--text-faint); padding:10px 14px; border-bottom:1px solid var(--border); white-space:nowrap;
  }
  table.problems td{ padding:10px 14px; border-bottom:1px solid var(--border); vertical-align:top; }
  table.problems tr:last-child td{ border-bottom:none; }
  table.problems a{ text-decoration:none; font-weight:500; }
  table.problems a:hover{ text-decoration:underline; }
  .judge-badge{ font-family:var(--mono); font-size:.72rem; padding:2px 8px; border-radius:5px; background:var(--surface-2); color:var(--text-muted); white-space:nowrap; }
  .judge-badge.cf{ background:#e7edf7; color:#2a4a8a; }
  .judge-badge.cses{ background:var(--accent-soft); color:var(--accent-strong); }
  .judge-badge.lc{ background:var(--real-soft); color:var(--real); }
  :root:not([data-theme="light"]) .judge-badge.cf{ background:#1c2740; color:#9db6e8; }
  :root[data-theme="dark"] .judge-badge.cf{ background:#1c2740; color:#9db6e8; }
  .diff-badge{ font-family:var(--mono); font-size:.78rem; color:var(--text-muted); }
  .subtopic-cell{ font-size:.82rem; color:var(--text-faint); }
  .desc-cell{ font-size:.85rem; color:var(--text-muted); max-width:340px; }

  /* ---------- Roadmap ---------- */
  .roadmap-grid{ display:flex; flex-direction:column; gap:10px; margin-top:8px; }
  .roadmap-stage{
    display:grid; grid-template-columns:44px 1fr; gap:16px; align-items:start;
    background:var(--surface); border:1px solid var(--border); border-radius:var(--radius);
    padding:16px 18px; box-shadow:var(--shadow);
  }
  .roadmap-num{
    width:36px; height:36px; border-radius:50%; background:var(--accent-soft); color:var(--accent-strong);
    font-family:var(--mono); font-weight:700; font-size:.95rem; display:flex; align-items:center; justify-content:center;
  }
  .roadmap-body h3{ font-size:1rem; margin-bottom:6px; }
  .roadmap-goal{ font-size:.87rem; color:var(--text-muted); line-height:1.6; margin:0 0 10px; max-width:75ch; }
  .roadmap-items{ flex-direction:row; flex-wrap:wrap; gap:8px; }
  .roadmap-items li{ list-style:none; }
  .roadmap-items a{
    display:inline-block; background:var(--surface-2); border:1px solid var(--border); border-radius:100px;
    padding:5px 12px; font-size:.8rem; color:var(--text); text-decoration:none;
  }
  .roadmap-items a:hover{ border-color:var(--accent); color:var(--accent-strong); }

  /* ---------- Hub grids ---------- */
  .hub-grid{ display:grid; grid-template-columns:repeat(auto-fill, minmax(280px,1fr)); gap:14px; margin-top:8px; }
  .hub-card{
    display:block; background:var(--surface); border:1px solid var(--border); border-radius:var(--radius);
    padding:18px 20px; box-shadow:var(--shadow); text-decoration:none; color:var(--text);
    transition:transform .12s, border-color .12s;
  }
  .hub-card:hover{ border-color:var(--accent); transform:translateY(-2px); }
  .hub-card h3{ font-size:1rem; margin-bottom:8px; color:var(--text); }
  .hub-card p{ font-size:.86rem; color:var(--text-muted); line-height:1.55; margin:0 0 10px; }
  .hub-card .meta{ font-family:var(--mono); font-size:.72rem; color:var(--text-faint); }

  footer{ margin-top:60px; padding-top:20px; border-top:1px solid var(--border); color:var(--text-faint); font-size:.78rem; }

  @media (prefers-reduced-motion: reduce){ *{ transition:none !important; } }
</style>
"""

def site_nav(urls, current):
    items = [
        ("cpguide", "CP / DSA Guide", urls.get("cpguide", "#")),
        ("concepts", "C++ Concepts", urls.get("concepts", "#")),
        ("index", "Interview Q&A + MCQ Bank", urls.get("index", "#")),
    ]
    links = []
    for key, label, url in items:
        cls = ' class="current"' if key == current else ""
        links.append(f'<a href="{esc(url)}"{cls}>{esc(label)}</a>')
    auth_slot = '<span id="authSlot" class="auth-slot"></span>' if PROGRESS_ENABLED else ""
    return f'<nav class="site-nav"><span class="brand">placement-prep</span>{"".join(links)}{auth_slot}</nav>'

FOOTER = '<footer>Compiled for personal interview/placement preparation from publicly accessible sources and independently authored reference material. Company and platform names belong to their respective owners; this is an unofficial, independently compiled study aid.</footer>'

def judge_class(judge):
    j = (judge or "").lower()
    if "codeforces" in j: return "cf"
    if "cses" in j: return "cses"
    if "leetcode" in j: return "lc"
    return ""

def problems_table_html(problems, table_id="problemsTable"):
    if not problems:
        return '<p class="theory-block">No curated problems recorded for this topic yet.</p>'
    rows = []
    for p in problems:
        jc = judge_class(p["judge"])
        done_cell = f"<td>{done_checkbox_html(p['link'], 'problem')}</td>" if PROGRESS_ENABLED else ""
        rows.append(f'''<tr data-search="{esc((p['name']+' '+p['judge']+' '+p['subtopic']+' '+p['description']).lower())}">
  <td><a href="{esc(p['link'])}" target="_blank" rel="noopener noreferrer">{esc(p['name'])}</a></td>
  <td><span class="judge-badge {jc}">{esc(p['judge'])}</span></td>
  <td class="diff-badge">{esc(p['difficulty'])}</td>
  <td class="subtopic-cell">{esc(p['subtopic'])}</td>
  <td class="desc-cell">{esc(p['description'])}</td>
  {done_cell}
</tr>''')
    done_th = "<th>Done</th>" if PROGRESS_ENABLED else ""
    return f'''<div class="problems-toolbar"><input type="search" id="{table_id}Search" placeholder="Filter problems…" autocomplete="off"></div>
<div class="table-wrap"><table class="problems" id="{table_id}">
<thead><tr><th>Problem</th><th>Judge</th><th>Difficulty</th><th>Subtopic</th><th>Description</th>{done_th}</tr></thead>
<tbody>{"".join(rows)}</tbody>
</table></div>
<script>
(function(){{
  var input = document.getElementById("{table_id}Search");
  var rows = document.querySelectorAll("#{table_id} tbody tr");
  input.addEventListener("input", function(){{
    var q = input.value.trim().toLowerCase();
    rows.forEach(function(r){{ r.style.display = r.dataset.search.includes(q) ? "" : "none"; }});
  }});
}})();
</script>'''
