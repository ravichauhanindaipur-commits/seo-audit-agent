import urllib.request
from html.parser import HTMLParser

URL = "https://ravichauhanindaipur-commits.github.io/rohit-clinic-digital/"

class SEOParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.title = False
        self.title_text = []
        self.h1 = 0
        self.description = None
        self.robots = None
    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag.lower() == "title": self.title = True
        if tag.lower() == "h1": self.h1 += 1
        if tag.lower() == "meta":
            name = attrs.get("name", "").lower()
            if name == "description": self.description = attrs.get("content", "")
            if name == "robots": self.robots = attrs.get("content", "")
    def handle_endtag(self, tag):
        if tag.lower() == "title": self.title = False
    def handle_data(self, data):
        if self.title: self.title_text.append(data.strip())

print("Rohit Clinic Digital - SEO Audit")
print("=" * 35)
try:
    req = urllib.request.Request(URL, headers={"User-Agent": "RohitClinicSEOAudit/1.0"})
    with urllib.request.urlopen(req, timeout=20) as response:
        html = response.read().decode("utf-8", errors="replace")
        print("HTTP status:", response.status)
    parser = SEOParser()
    parser.feed(html)
    title = " ".join(x for x in parser.title_text if x)
    print("Page title:", title or "MISSING")
    print("Title length:", len(title))
    print("Meta description:", parser.description or "MISSING")
    print("H1 heading count:", parser.h1)
    print("Robots meta:", parser.robots or "Not specified")
    print("HTML size:", len(html.encode("utf-8")), "bytes")
    print("\nBasic recommendations:")
    if not title: print("- Add a descriptive page title.")
    elif len(title) > 60: print("- Consider shortening the page title.")
    if not parser.description: print("- Add a unique meta description.")
    if parser.h1 == 0: print("- Add a clear H1 heading.")
    elif parser.h1 > 1: print("- Review whether multiple H1 headings are appropriate.")
    print("- Verify sitemap.xml and robots.txt separately.")
    print("- Review mobile usability and Search Console indexing.")
except Exception as e:
    print("Audit failed:", type(e).__name__, str(e))


