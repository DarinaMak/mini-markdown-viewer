import os

inp = "markdown/example.md"
outp = "output/example.html"

with open(inp, "r", encoding="utf-8") as f:
    md = f.readlines()

html = ["<html><body>\n"]

for line in md:
    if line.startswith("# "):
        html.append(f"<h1>{line[2:].strip()}</h1>\n")
    elif line.startswith("- "):
        html.append(f"<li>{line[2:].strip()}</li>\n")
    elif "*" in line:
        html.append(f"<p>{line.replace('*', '')}</p>\n")
    else:
        html.append(f"<p>{line.strip()}</p>\n")

html.append("</body></html>")

with open(outp, "w", encoding="utf-8") as f:
    f.writelines(html)

print("Converted to HTML:", outp)
