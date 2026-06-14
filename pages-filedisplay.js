(function () {
  const container = document.createElement("div");
  container.style.fontFamily = "monospace";
  container.style.padding = "16px";

  document.body.innerHTML = "";
  document.body.appendChild(container);

  let tree = null;

  async function loadTree() {
    const res = await fetch("/tree.json", { cache: "no-store" });
    tree = await res.json();
    render(tree);
  }

  function render(node, pathStack = []) {
    container.innerHTML = "";

    const title = document.createElement("h3");
    title.textContent = "/" + pathStack.join("/");
    container.appendChild(title);

    const children = node.children || [];

    children.forEach((child) => {
      const row = document.createElement("div");
      row.style.cursor = "pointer";
      row.style.padding = "2px 0";

      if (child.type === "dir") {
        row.textContent = "📁 " + child.name;

        row.onclick = () => {
          let path = child.path.replace(/\/+$/, "");
          window.location.href = path + "/";
        };
      } else {
        row.textContent = "📄 " + child.name;

        row.onclick = () => {
          window.location.href = child.path;
        };
      }

      container.appendChild(row);
    });

    if (!children.length) {
      const empty = document.createElement("div");
      empty.textContent = "Empty folder";
      container.appendChild(empty);
    }
  }

  loadTree();
})();
