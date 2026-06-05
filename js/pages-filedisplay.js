(function () {
  const container = document.createElement("div");
  container.style.fontFamily = "monospace";
  container.style.padding = "16px";

  document.body.innerHTML = "";
  document.body.appendChild(container);

  function getPath() {
    let path = window.location.pathname;
    if (!path.endsWith("/")) path += "/";
    return path;
  }

  async function load(path) {
    container.innerHTML = "Loading...";

    try {
      const res = await fetch(path + "index.json", {
        cache: "no-store", // ensures browser doesn't reuse stale index.json
      });

      if (!res.ok) throw new Error("No index.json");

      const files = await res.json();
      render(files, path);
    } catch (e) {
      container.innerHTML = `
        <div>Could not load <code>${path}</code></div>
      `;
      console.error(e);
    }
  }

  function render(files, path) {
    container.innerHTML = "";

    const title = document.createElement("h3");
    title.textContent = "Index of " + path;
    container.appendChild(title);

    // parent folder link
    if (path !== "/") {
      const up = document.createElement("div");
      up.textContent = "..";
      up.style.cursor = "pointer";
      up.style.color = "gray";

      up.onclick = () => {
        const parts = path.split("/").filter(Boolean);
        parts.pop();
        const parent = "/" + (parts.length ? parts.join("/") + "/" : "");
        load(parent);
      };

      container.appendChild(up);
    }

    files.forEach((f) => {
      const row = document.createElement("div");
      row.style.cursor = "pointer";
      row.style.padding = "2px 0";

      if (f.type === "dir") {
        row.textContent = "📁 " + f.name;
        row.style.color = "#2b6cb0";

        row.onclick = () => {
          load(path + f.name + "/");
        };
      } else {
        row.textContent = "📄 " + f.name;
        row.style.color = "#333";

        row.onclick = () => {
          window.open(path + f.name, "_blank");
        };
      }

      container.appendChild(row);
    });

    if (!files.length) {
      const empty = document.createElement("div");
      empty.textContent = "Empty folder";
      container.appendChild(empty);
    }
  }

  load(getPath());
})();
