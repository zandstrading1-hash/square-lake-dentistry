# DECISIONS — why things are the way they are

- **Hosting = GitHub Pages, legacy branch build** (branch `main`, `/` root). Zero-cost static
  hosting tied to the repo. Consequence: force-pushes need a manual Pages build trigger.
- **Repo owner = `zandstrading1-hash`** (public). That's the GitHub account the site is published
  under and where the live URL comes from.
- **Commit author identity** comes from the origin machine's global git config and differs from the
  repo owner account — harmless (author metadata ≠ repo ownership), just don't be surprised by it.
- **Phone-first booking, no online scheduler.** Every primary CTA is "Call to book." Deliberate
  product decision for this practice.
- **`index.html` is hand-authored**; all other pages are generated from Python content modules so the
  shared header/footer stay consistent. Editing HTML directly is fine; only re-run the generator if
  you change the shared chrome.
- **Accuracy pass (commit `2dbeb7a`)** removed every claim that couldn't be verified against the
  practice's own public listings: star rating / `aggregateRating`, "25+ years", sedation / technology /
  financing claims, named insurers, and the brand name "Invisalign" → "clear aligners". Added 6 real,
  attributed Google reviews for Dr. Hanna. Rationale: do not publish unverifiable medical/credential claims.
- **Multi-device strategy = whole project in Google Drive** (`My Drive/Projects/square-lake-dentistry`),
  synced across devices; GitHub is the publisher + backup. Chosen by the owner for a single-folder,
  edit-anywhere workflow (work from PC or laptop, whichever is at hand). Accepted trade-off: a
  file-syncer can corrupt a live `.git` folder if two devices write at once — so the rule is
  single-writer-at-a-time, let Drive settle before switching devices, and push to GitHub often.
  See `../OPEN-ME-FIRST.md` and `../.gdrive-ignore-notes.md`.
