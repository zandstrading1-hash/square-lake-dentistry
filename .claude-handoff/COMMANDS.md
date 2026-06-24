# COMMANDS

## First command on a new device (RECOMMENDED: git via GitHub)
Clone the repo from GitHub. **This is the multi-device sync mechanism** — do not rely on
Drive-syncing the `.git` folder. Clone OUTSIDE Google Drive / OneDrive (e.g. `C:\dev\` or `~/dev/`):
```bash
git clone https://github.com/zandstrading1-hash/square-lake-dentistry.git
cd square-lake-dentistry
```
- Start each session with: `git pull`
- After changes:           `git add -A && git commit -m "what changed" && git push`
- Pushing to `main` auto-republishes the live site.

## Dependencies / install
- **Nothing to install.** The website has no runtime dependencies.
- The optional Python page generator uses the **standard library only** — no `pip install` needed.
- (Only if you'll run the generator) check Python: `python --version`  → need **3.8+**.

## Virtual environment
- This project has **no virtualenv and needs none.** If you want one for isolation:
  ```bash
  python -m venv .venv
  # Windows:      .venv\Scripts\activate
  # macOS/Linux:  source .venv/bin/activate
  ```
  **Do not copy/sync `.venv/` between devices** — recreate it per device. It is git-ignored
  and listed in `.gdrive-ignore-notes.md`.

## Build / regenerate pages (optional)
Only needed if you edit the Python content modules or the shared header/footer:
```bash
python build.py          # regenerate all generated pages + sitemap.xml + robots.txt
python resync_index.py   # re-apply shared header/footer to the hand-authored index.html
```
`index.html` is hand-authored and is NOT overwritten by `build.py`.

## Tests
- **No automated test suite** (no pytest/unittest in this project).
- Manual checks: open the `.html` files in a browser. The README describes a lightweight
  per-page audit (single `<h1>`, `lang`, meta description, image `alt`, iframe titles).
  For formal accessibility sign-off, run Lighthouse or axe + a screen reader.

## Preview locally
```bash
python -m http.server 8000     # then open http://localhost:8000
```

## Publish (GitHub Pages)
- Normal flow: commit + push to `main` → Pages rebuilds automatically (~1 min).
- Live URL: https://zandstrading1-hash.github.io/square-lake-dentistry/
- After a **force-push** (history rewrite), Pages does NOT auto-rebuild. Trigger one by making
  any tiny commit and pushing, or re-saving the source under GitHub → Settings → Pages.
