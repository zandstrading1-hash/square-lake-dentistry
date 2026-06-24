# OPEN ME FIRST — Square Lake Family Dentistry (Google Drive sync)

This folder **is** the live project, synced across your devices by **Google Drive**. Edit here on
either device; Google Drive carries your changes to the other one. GitHub is the publisher + backup.

## ⚠️ Golden rules (so Google Drive never corrupts the project)
This folder includes a `.git` history. File-syncers can corrupt `.git` if two devices touch it at
once. To stay safe:
1. **Work on ONE device at a time.**
2. **Before switching devices:** wait until Google Drive shows **"up to date / fully synced"** on the
   device you just used — and give the other device a moment to finish downloading before you open files.
3. **Commit + push to GitHub often** — it's your backup and how the live site updates:
   ```
   git add -A && git commit -m "what changed" && git push
   ```
   If Drive ever mangles something, you can recover from GitHub (see `.gdrive-ignore-notes.md`).

## ▶ One-time setup on the OTHER device
1. Install **Google Drive for Desktop** and sign in with the **same Google account**.
2. Let it sync, then find this folder:
   - Windows: `G:\My Drive\Projects\square-lake-dentistry`  _(drive letter may differ)_
   - Mac: `~/Library/CloudStorage/GoogleDrive-<you>/My Drive/Projects/square-lake-dentistry`
3. Right-click the folder → **Offline access → Available offline** (so git works and files are always
   present, not online-only).
4. Install **git**, and sign in to GitHub once (so `git push` works from that device).

## ▶ Day-to-day
- Edit the `.html` / `.css` / `.js` (and optional Python) files directly.
- Save → Google Drive syncs them to your other device automatically.
- To publish to the live website: `git add -A && git commit -m "..." && git push`.

- **Live site:** https://zandstrading1-hash.github.io/square-lake-dentistry/
- **Repo / backup:** https://github.com/zandstrading1-hash/square-lake-dentistry
- Full context: `.claude-handoff/`  •  sync do/don't: `.gdrive-ignore-notes.md`
