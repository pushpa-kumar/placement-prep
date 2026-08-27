import sys, os, re, json, argparse
sys.path.insert(0, os.path.dirname(__file__))
from gen_concept_page import build_page as build_concept_page, GROUP_FILES
from gen_cpguide_page import build_page as build_cpguide_page, TOPIC_PAGES
from gen_hubs import build_cpguide_hub, build_concepts_hub
from gen_further_reading import build_page as build_further_reading_page

SCRATCH = os.path.dirname(__file__)
DEFAULT_OUT_DIR = os.path.expanduser("~/quant-hft-interview-prep")

INDEX_URL = "https://claude.ai/code/artifact/df9ba560-181f-4187-adaa-194dd194165f"

def resolve_placeholders(html, page_url_map):
    def repl(m):
        slug = m.group(1)
        anchor = m.group(2) or ""
        url = page_url_map.get(slug, "#")
        return url + anchor
    return re.sub(r'__PAGE__:([a-z0-9-]+)(#[a-z0-9-]*)?', repl, html)

def write(path, content):
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"wrote {path} ({len(content):,} bytes)")

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--url-map", default=None, help="path to JSON file mapping slug->url")
    ap.add_argument("--out-dir", default=DEFAULT_OUT_DIR, help="directory to write generated pages into")
    args = ap.parse_args()

    OUT_DIR = args.out_dir
    os.makedirs(OUT_DIR, exist_ok=True)

    page_url_map = {"index": INDEX_URL}
    if args.url_map and os.path.exists(args.url_map):
        page_url_map.update(json.load(open(args.url_map)))

    nav_urls = {
        "index": page_url_map.get("index", "#"),
        "cpguide": page_url_map.get("cpguide-hub", "#"),
        "concepts": page_url_map.get("concepts-hub", "#"),
    }

    # 14 CP guide topic pages
    for jfs, slug, title in TOPIC_PAGES:
        html = build_cpguide_page(jfs, slug, title, nav_urls)
        html = resolve_placeholders(html, page_url_map)
        write(f"{OUT_DIR}/cp-{slug}.html", html)

    # 7 concept pages
    for fname, title in GROUP_FILES:
        html = build_concept_page(fname, title, nav_urls)
        html = resolve_placeholders(html, page_url_map)
        d = json.load(open(f"{SCRATCH}/{fname}"))
        write(f"{OUT_DIR}/concepts-{d['slug']}.html", html)

    # topic_urls / concept_urls for hubs (slug -> url, only meaningful once url-map populated)
    topic_urls = {slug: page_url_map.get(slug, "#") for _, slug, _ in TOPIC_PAGES}
    concept_urls = {}
    for fname, _ in GROUP_FILES:
        d = json.load(open(f"{SCRATCH}/{fname}"))
        concept_urls[d["slug"]] = page_url_map.get(d["slug"], "#")

    cpguide_hub_html = resolve_placeholders(build_cpguide_hub(nav_urls, topic_urls), page_url_map)
    write(f"{OUT_DIR}/cp-guide.html", cpguide_hub_html)

    concepts_hub_html = resolve_placeholders(build_concepts_hub(nav_urls, concept_urls), page_url_map)
    write(f"{OUT_DIR}/concepts.html", concepts_hub_html)

    further_reading_html = resolve_placeholders(build_further_reading_page(nav_urls), page_url_map)
    write(f"{OUT_DIR}/cp-further-reading.html", further_reading_html)

if __name__ == "__main__":
    main()
