<!-- .github/copilot-instructions.md: Project-specific guidance for AI coding assistants -->

# Quick orientation

This repo is a set of standalone student lab exercises for a Network Programming course. Each lab lives in its own top-level folder (`Lab1`, `Lab2`, ...). Instruction PDFs and assignment text are in `Lab_txt` (for example: `Lab_txt/NetProgLab01.pdf`).

Primary language: Python (simple scripts). There is no package structure, CI, or test harness by default.

# Big picture (brief)
- Purpose: standalone scripts and small examples per lab folder. Work should preserve that per-lab isolation.
- Data flow: most files are simple input/process/print scripts. Expect plain stdout-based examples (see `Lab1/hello.py`).
- Why: these are teaching exercises — prefer minimal, clear edits rather than large refactors.

# Developer workflows (how to run / debug)
- Run a single lab script from PowerShell (Windows):

```powershell
cd "c:\Users\HP\Desktop\Skola3\Network programing\Lab1"
python .\hello.py
```

- If creating a virtual env (recommended for extended work):

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python --version
```

# Project-specific conventions and patterns
- Folder-per-lab: keep code and any artifacts (images, sample data, PDFs) inside the same `LabN` folder.
- File names: lower-case script files (e.g. `hello.py`).
- Minimal external dependencies: most labs rely on the Python stdlib only. Check `Lab_txt` for assignment details before adding libraries.
- Coding style: small, didactic scripts — prefer explicit, simple code over compact/clever solutions.

# Examples from the repo
- `Lab1/hello.py` demonstrates common beginner patterns: printing, slicing, multi-line strings. Note: the file currently contains syntax issues (for example it uses `/n` instead of `\n`). When fixing, prefer minimal, focused corrections that keep the educational intent.

Example suggested small fix (what an AI may do automatically):

Replace occurrences of `/n` with `\n` in `Lab1/hello.py` so prints behave as intended.

# Integration points & external deps
- There are no external services, databases, or network servers defined in the repo. If a lab requires network interaction, look for instructions inside the corresponding `Lab_txt` PDF.

# Guidance for AI edits
- Keep changes small and localized to the relevant `LabN` folder unless the user asks for wider refactors.
- When adding files, update a top-level `README.md` if you introduce a new shared workflow or dependency (none exists currently).
- If you modify code that solves a lab task, leave a short comment in the file explaining why the change was made (one-line).

# Files to inspect first (priorities)
1. `Lab_txt/NetProgLab01.pdf` — assignment text for Lab1.
2. `Lab1/hello.py` — a representative script with learner-oriented code.
3. Other `LabN` folders — each contains standalone exercises.

# If you see a .github/copilot-instructions.md already present
- Merge minimally: preserve any environment/setup commands and any non-generic, project-specific tips. Add/update the small examples above as needed.

Please review these notes and tell me if you'd like: (a) a stricter style guide for the labs, (b) automated linting/tests added, or (c) converting the lab scripts into importable modules with tests — I can draft next-step changes.
