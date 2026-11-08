# Miniclip Yo Me! Avatar Archival Pipeline

An automated Python data mining and digital preservation tool designed to extract, filter, and archive user-created **Yo Me!** avatars from legacy Miniclip accounts prior to platform deprecation.

This tool successfully processed **25 million account IDs** (IDs 1 through 25,000,000), using byte-level image comparison algorithms to filter out default placeholders and retain only unique, user-customized avatars. The resulting historical collection is hosted publicly on the [Internet Archive]([https://archive.org/download/miniclip_yo_me_collection](https://archive.org/details/miniclip_yo_me_collection)).

---

## Key Features

* **Byte-Level Asset Deduplication:** Employs Python's `filecmp` module to compare fetched binary payloads against pre-defined baseline assets, automatically discarding default/unmodified profiles.
* **Resilient Stateful Checkpointing:** Dynamically reads and updates execution bounds (`uidstart.txt` / `uidend.txt`), enabling seamless recovery and resumption following network interruptions or restarts.
* **Continuous Uptime Integration:** Features a background Flask web server thread (`webserver.py`) to facilitate continuous execution on cloud runners and web monitoring services.
* **Large-Scale Archival Impact:** Executed a high-volume data pipeline scanning 25,000,000 unique endpoints to preserve early web history artifacts[cite: 1, 2].

---

## Pipeline Architecture

1. **Endpoint Polling:** Interrogates legacy content distribution network (CDN) endpoints (`avatars-live.pool.miniclippt.com`) for sequential account IDs.
2. **Template Comparison:** Evaluates fetched avatar files against a local directory of default avatar templates using shallow and deep byte comparison.
3. **Automated Cleanup:** Instantly purges default placeholders to optimize disk storage while retaining customized user avatars.
4. **State Persistence:** Flushes updated progress markers back to disk on each iteration to safeguard execution state.

---

## Project Structure

```text
├── main.py              # Core scraper engine & file comparison pipeline
├── webserver.py         # Lightweight Flask server for keeping host environment active
├── config/
│   ├── uidstart.txt     # Starting account ID marker
│   └── uidend.txt       # Ending account ID marker
└── premade/             # Reference default template images used for duplicate filtering
