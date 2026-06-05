import json
import os

IGNORE = {".git", ".github", "__pycache__"}


def build_tree(path):
    node = {
        "name": os.path.basename(path) if path != "." else "",
        "path": "/" + path.replace("\\", "/") if path != "." else "/",
        "type": "dir",
        "children": [],
    }

    for name in sorted(os.listdir(path)):
        if name in IGNORE or name.startswith("."):
            continue

        full = os.path.join(path, name)

        if os.path.isdir(full):
            node["children"].append(build_tree(full))
        else:
            node["children"].append(
                {"name": name, "path": "/" + full.replace("\\", "/"), "type": "file"}
            )

    return node


def write_redirect_index(path):
    os.makedirs(path, exist_ok=True)

    index_path = os.path.join(path, "index.html")

    # DO NOT overwrite real pages
    if os.path.exists(index_path):
        return

    with open(index_path, "w", encoding="utf-8") as f:
        f.write("""<!doctype html>
<html>
<head>
  <meta charset="utf-8">
  <meta http-equiv="refresh" content="0; url=/" />
  <title>Redirecting...</title>
</head>
<body>
  <script>
    window.location.href = "/";
  </script>
</body>
</html>
""")


def walk_dirs_for_redirects(path):
    for name in os.listdir(path):
        if name in IGNORE or name.startswith("."):
            continue

        full = os.path.join(path, name)

        if os.path.isdir(full):
            write_redirect_index(full)
            walk_dirs_for_redirects(full)


tree = build_tree(".")
with open("tree.json", "w", encoding="utf-8") as f:
    json.dump(tree, f, indent=2)

walk_dirs_for_redirects(".")

print("done")
