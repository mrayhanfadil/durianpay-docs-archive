# Durianpay documentation — private archive

Private, searchable Markdown snapshot of the official documentation at <https://docs.durianpay.id/>.

This is an unofficial personal archive, not a Durianpay project. The repo owner reports that a Durianpay sales engineer said the docs may be copied and used with ChatGPT or Claude; the docs UI also offers “Copy Page”, “Open in ChatGPT”, “Open in Claude”, and “View as Markdown”. This repository is intentionally **private**. That permission is not presented here as a public redistribution or open-source license. Keep the repository private and check with Durianpay before sharing or changing its visibility.

No license is granted by this repository for Durianpay’s source documentation. Copyright and other rights remain with their respective owners.

## Contents

- `content/docs/` — documentation pages discovered from the official `llms.txt` index
- `content/reference/` — API reference pages in the same index
- `source/llms.txt` — captured source index
- `assets/` — embedded images and directly linked document files captured from pages
- `manifest.json` — source URLs, retrieval timestamp, SHA-256 digests, page/asset status, and any fetch failures
- `scripts/sync_docs.py` — standard-library-only snapshot updater

## Refresh

```bash
python3 scripts/sync_docs.py
```

Preview the pages currently listed by the upstream index without downloading them:

```bash
python3 scripts/sync_docs.py --dry-run
```

The updater follows the current public `llms.txt` and its same-origin Markdown page links. It records page and asset fetch failures in `manifest.json`; it does not silently treat failed fetches as a complete mirror. It does not delete pages that disappear from a later upstream index.
