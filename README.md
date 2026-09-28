# lab04-UnityCrew

Group Assignment Submission by Unity Crew

## 1. Group Name

Unity Crew

## 2. Who Did What

| Member                          | GitHub Username | File                                 |
| ------------------------------- | --------------- | ------------------------------------ |
| Aeint Kyi Pyar Soe (6705140003) | AeintKyiPyarSoe | bank.py, test_deposit.py, .gitignore |
| Htet Soe Lin (6705140023)       | Tyzonn22        | conftest.py                          |
| Khun Maung Aye (6705140019)     | KhunMaungAye    | test_teardown.py                     |
| Chan Myae Aung (6705140010)     | ChanMyaeAung    | test_shared.py                       |
| Kaung Khant Htoo (6705140027)   | kxkhantx        | test_withdraw.py                     |

## 3. Our Merge Conflict
## Overview of Conflicts Solved

Throughout the collaborative workflow in `lab04-UnityCrew`, the team encountered and resolved four distinct merge conflicts:

| Conflict | Commits Involved | Target File | Nature of Collision |
|---|---|---|---|
| **Conflict 1 (Lab Core Exercise)** | `e6054b4`, `637c74e` | `README.md` | Concurrent edits to the placeholder line `Creating Conflict` vs. new member table row. |
| **Conflict 2 (Formatting & Run Instructions)** | `57844b5` | `README.md` | Group header formatting updates colliding with the addition of pytest execution instructions. |
| **Conflict 3 (4th Member & Withdraw Tests)** | `c113fc8`, `b981ab1` | `README.md` | Documentation lines colliding with 4th member's row. |
| **Conflict 4 (5th Member & Shared Fixture Tests)** | `fb62bba` | `README.md` | Local conflict explanations colliding with 5th member's row, `test_shared.py`, and `.gitignore`. |

---

## Conflict 1: The README Table & Marker Conflict (Lab Core Exercise)

### Conflict Markers Encountered
During the merge of concurrent changes into [README.md], Git halted automatic merging and inserted standard conflict markers:

```markdown
<<<<<<< HEAD
=======
Creating Conflict
>>>>>>> 9c01c370d7f8aebacb35cc50d5f483f9a77915ae
```

#### Breakdown of the Markers
* **`<<<<<<< HEAD`**: Marks the beginning of the conflicting region and displays the changes made in the currently checked-out branch (local `main`). In this local branch, the line `Creating Conflict` had been deleted.
* **`=======`**: Serves as the dividing boundary between the two conflicting sets of changes.
* **`>>>>>>> 9c01c370d7f8aebacb35cc50d5f483f9a77915ae`**: Marks the end of the conflict section and identifies the incoming commit/branch being merged (commit `9c01c37` from Khun Maung Aye), where `Creating Conflict` was preserved alongside the new table row.

### Final Decision Made by the Team
The team reviewed both versions and decided to:
1. **Retain Member Contributions:** Keep Khun Maung Aye's newly added row in the `Who Did What` table (`| Khun Maung Aye (6705140019) | KhunMaungAye | test_teardown.py |`).
2. **Remove Artificial Conflict Text:** Discard the placeholder test string `Creating Conflict`.
3. **Strip Conflict Markers:** Completely remove the `<<<<<<< HEAD`, `=======`, and `>>>>>>> ...` marker lines.
4. **Establish Uniform Formatting:** Introduce a dedicated `## Group Name` heading (`Unity Crew`) and preserve the pytest run instructions (`pytest -s test_teardown.py`).

### Why Git Could Not Automatically Resolve It
Git relies on a three-way merge algorithm comparing three snapshots: the common ancestor commit (`1ca4fd1`) and the tips of both branches (`99702a1` and `9c01c37`).

Git could not resolve this automatically because **both branches concurrently modified the exact same contiguous lines** at the bottom of [README.md]:
- In the common ancestor (`1ca4fd1`), the line `Creating Conflict` existed.
- Branch A (Aeint Kyi Pyar Soe) deleted that line.
- Branch B (Khun Maung Aye) inserted a new table row immediately above that line while modifying the line ending.

Because both branches altered the identical file region in conflicting ways, Git had no objective programmatic logic to determine whether the user intended to delete the line, keep it, or append the table row. To prevent accidental data loss, Git halted the merge and handed control to the developers to resolve the ambiguity manually.

---

## Conflict 2: Group Header Formatting vs. Run Instructions

### Conflicting Changes Encountered
In merge commit `57844b5`, two parallel developments collided on [README.md]:
- Local commit `43f616e` standardized the group header syntax (`## Group Name\nUnity Crew`) and cleaned table borders.
- Remote commit `3940cb8` (by Khun Maung Aye) appended a `# How to run` section with pytest instructions (`pytest -s test_teardown.py`).

### Final Decision Made by the Team
The team combined both contributions:
1. Retained the clean `## Group Name` and formatted table from `43f616e`.
2. Preserved the `# How to run` pytest execution guide from `3940cb8`.
3. Verified markdown structure so all team documentation and execution guides were cleanly visible.

### Why Git Could Not Automatically Resolve It
Both branches made concurrent modifications touching adjoining line ranges in [README.md]. Because the line contexts overlapped, Git required human confirmation to weave both changes together cleanly without overwriting either developer's additions.

---

## Conflict 3: Documentation Migration & 4th Member Integration

### Conflicting Changes Encountered
In merge commits `c113fc8` and `b981ab1`, two branches diverged:
- One branch extracted in-depth conflict logs out of [README.md] into this dedicated `conflict_resolution.md` report.
- Concurrently, Kaung Khant Htoo pushed commits (`cacf817`, `845ad68`, `66148bf`) adding [test_withdraw.py] and appending `| Kaung Khant Htoo (6705140027) | kxkhantx | test_withdraw.py |` to [README.md].

### Final Decision Made by the Team
1. **Incorporate New Member:** Retain Kaung Khant Htoo's member row in the `Who Did What` table.
2. **Modularize Lab Deliverables:** Keep [README.md] concise as a project overview.
3. **Harmonize Test Suite:** Ensure all tests from `test_deposit.py`, `test_teardown.py`, and `test_withdraw.py` run and pass synchronously.

### Why Git Could Not Automatically Resolve It
Both branches made concurrent changes to the `Who Did What` table rows and surrounding text. Git prevented automatic merging to avoid dropping either the new member row or the documentation restructuring.

---

## Conflict 4: 5th Member Integration & Shared Fixture Tests (Merge `fb62bba`)

### Conflicting Changes Encountered
In commit `fb62bba`, the local branch merged incoming changes from Chan Myae Aung (commit `d139c26`):
- Local commit `82b5e05` documented merge conflict resolutions in [README.md].
- Remote commit `d139c26` (Chan Myae Aung) added [test_shared.py], added essential exclusions to [.gitignore], and inserted Chan Myae Aung's row into the `Who Did What` table in [README.md].

When pulling and merging `d139c26`, Git detected conflicting concurrent edits at the bottom of the contributor table in [README.md].

### Final Decision Made by the Team
1. **Preserve All Member Contributions:** Retained Chan Myae Aung's row in the table (`| Chan Myae Aung (6705140010) | ChanMyaeAung | test_shared.py |`) alongside Kaung Khant Htoo's row.
2. **Incorporate Shared Fixture Tests:** Integrated [test_shared.py] into the automated test suite to verify shared fixture reusability.
3. **Preserve Environment Hygiene:** Accepted the [.gitignore] updates ignoring `.venv/` and pytest caches.
4. **Preserve Conflict Analysis:** Maintained comprehensive conflict documentation.

### Why Git Could Not Automatically Resolve It
Both branches concurrently modified the final rows of the markdown table in [README.md]. Because Git has no semantic knowledge of markdown table syntax or team rosters, it required manual developer verification to properly merge the new member row without discarding previous entries or documentation.

---

## Final Resolved State of README.md

After resolving all merge conflicts, the final state of [README.md] is:

```markdown
# lab04-UnityCrew

Group Assignment Submission by Unity Crew

## Group Name

Unity Crew

## Who Did What

| Member                          | GitHub Username | File                                 |
| ------------------------------- | --------------- | ------------------------------------ |
| Aeint Kyi Pyar Soe (6705140003) | AeintKyiPyarSoe | bank.py, test_deposit.py, .gitignore |
| Htet Soe Lin (6705140023)       | Tyzonn22        | conftest.py                          |
| Khun Maung Aye (6705140019)     | KhunMaungAye    | test_teardown.py                     |
| Chan Myae Aung (6705140010)     | ChanMyaeAung    | test_shared.py                       |
| Kaung Khant Htoo (6705140027)   | kxkhantx        | test_withdraw.py                     |
```

---
## 4. Git Contribution Summary
    17  Aeint Kyi Pyar Soe
     5  Kaung Khant Htoo
     5  Tyzon
     4  Khun Maung Aye
     2  karayuuco
     1  ChannMyaeAung
--- 

## 5. Answers to Lab Questions

### 1. Why was your push rejected, and how did you fix it?
> The push was rejected because the remote repository contained newer commits pushed by a collaborator that our local branch did not have. We fixed it by running `git pull origin main` to fetch and integrate the remote changes locally, resolving any merge conflicts, and then pushing again.

### 2. Why could Git not resolve the README conflict automatically?
> Git could not resolve the conflict automatically because two collaborators concurrently edited the exact same lines of `README.md` since their common ancestor commit. Because Git cannot infer human intent without risking data loss, it halted the merge and inserted conflict markers for manual resolution.

### 3. What is the difference between committing and pushing?
> Committing (`git commit`) saves a snapshot of staged changes locally on your computer without altering the remote repository. Pushing (`git push`) transfers those local commits to the remote repository so team members can access them.

### 4. How do fixtures reduce duplicated setup code in tests?
> Fixtures define reusable setup logic in one place and automatically pass the pre-configured objects into test functions as arguments. This eliminates repetitive copy-pasting of initialization code across tests, keeping the test suite clean and easy to maintain.

---