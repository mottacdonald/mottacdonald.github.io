class MDViewer {
    static async view(fileUrl) {
        if (typeof marked === 'undefined') {
            await new Promise((resolve) => {
                const script = document.createElement('script');
                script.src = 'https://cdn.jsdelivr.net/npm/marked/marked.min.js';
                script.onload = resolve;
                document.head.appendChild(script);
            });
        }
        if (!document.getElementById('mdviewer-styles')) {
            const style = document.createElement('style');
            style.id = 'mdviewer-styles';
            style.textContent = `
                body { background-color: #121212; color: #e0e0e0; font-family: system-ui, -apple-system, sans-serif; line-height: 1.6; padding: 2rem; max-width: 800px; margin: 0 auto; }
                a { color: #bb86fc; text-decoration: none; } a:hover { text-decoration: underline; }
                pre, code { background: #1e1e1e; border-radius: 6px; font-family: monospace; font-size: 0.9em; }
                code { padding: 0.2em 0.4em; } pre { padding: 1rem; overflow-x: auto; border: 1px solid #333; }
                pre code { padding: 0; border: none; background: transparent; }
                blockquote { border-left: 4px solid #bb86fc; margin: 0; padding-left: 1rem; color: #a0a0a0; background: #1a1a1a; padding: 0.5rem 1rem; border-radius: 0 4px 4px 0; }
                h1, h2, h3, h4, h5, h6 { color: #ffffff; margin-top: 1.5em; margin-bottom: 0.5em; border-bottom: 1px solid #2a2a2a; padding-bottom: 0.3em; }
                table { border-collapse: collapse; width: 100%; margin: 1rem 0; }
                th, td { border: 1px solid #333; padding: 0.75rem; text-align: left; }
                th { background-color: #1a1a1a; }
                img { max-width: 100%; border-radius: 6px; }
            `;
            document.head.appendChild(style);
        }
        try {
            const response = await fetch(fileUrl);
            if (!response.ok) throw new Error(`Status ${response.status}`);
            const markdownText = await response.text();
            const container = document.createElement('div');
            container.innerHTML = marked.parse(markdownText);
            document.body.appendChild(container);
            
        } catch (error) {
            document.body.innerHTML = `<h3 style="color: #cf6679;">Error loading Markdown file: ${fileUrl}</h3><p>${error.message}</p>`;
        }
    }
}
