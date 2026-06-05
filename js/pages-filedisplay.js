(function () {
  const container = document.createElement("div");
  container.style.fontFamily = "monospace";
  container.style.padding = "20px";
  document.body.innerHTML = "";
  document.body.appendChild(container);

  let currentPath = window.location.pathname;

  async function load(path) {
    container.innerHTML = "Loading...";

    if (!path.endsWith("/")) path += "/";

    try {
      const res = await fetch(path + "index.json");
      const files = await res.json();
      render(files, path);
    } catch (e) {
      container.innerHTML = "No index.json found in " + path;
    }
  }

  function render(files, path) {
    container.innerHTML = "";

    const title = document.createElement("h3");
    title.textContent = "Index of " + path;
    container.appendChild(title);

    if (path !== "/") {
      const up = document.createElement("div");
      up.textContent = "..";
      up.style.cursor = "pointer";
      up.onclick = () => {
        const parent = path.split("/").slice(0, -2).join("/") + "/";
        load(parent === "//" ? "/" : parent);
      };
      container.appendChild(up);
    }

    files.forEach(f => {
      const row = document.createElement("div");
      row.style.cursor = "pointer";

      if (f.type === "dir") {
        row.textContent = "📁 " + f.name;
        row.onclick = () => load(path + f.name + "/");
        row.style.color = "blue";
      } else {
        row.textContent = "📄 " + f.name;
        row.onclick = () => window.open(path + f.name, "_blank");
      }

      container.appendChild(row);
    });
  }

  load(currentPath);
})();
