# lab04-UnityCrew

Group Assignment Submission by Unity Crew

## Group Name
Unity Crew

## Who Did What

| Member                          | GitHub Username | File                                 |
| ------------------------------- | --------------- | ------------------------------------ |
| Aeint Kyi Pyar Soe (6705140003) | AeintKyiPyarSoe | bank.py, test_deposit.py, .gitignore |
| Htet Soe Lin (6705140023) | Tyzonn22 | conftest.py |
| Khun Maung Aye (6705140019) | KhunMaungAye | test_teardown.py |

# How to run

To see the setup/teardown output clearly, use:

```bash
pytest -s test_teardown.py
```

The `-s` flag disables pytest output capturing, so the `print("[setup]")` and `print("[teardown]")` messages are visible.

## 3. Our Merge Conflict
## The Conflict Markers Encountered

During the merge of concurrent changes into [README.md], Git stopped the merge process and inserted conflict markers into the file:

```markdown
<<<<<<< HEAD
=======
Creating Conflict
>>>>>>> 9c01c370d7f8aebacb35cc50d5f483f9a77915ae
```

### Breakdown of the Markers
* **`<<<<<<< HEAD`**: Marks the beginning of the conflicting region and displays the changes made in the currently checked-out branch (local `main`). In this local branch, the line `Creating Conflict` had been deleted.
* **`=======`**: Serves as the dividing boundary between the two conflicting sets of changes.
* **`>>>>>>> 9c01c370d7f8aebacb35cc50d5f483f9a77915ae`**: Marks the end of the conflict section and identifies the incoming commit/branch being merged (commit `9c01c37` from Khun Maung Aye), where `Creating Conflict` was preserved alongside the new table row.

---

## The Final Decision Made by the Team

The team reviewed both versions and decided to:
1. **Retain Member Contributions:** Keep Khun Maung Aye's newly added row in the `Who Did What` table (`| Khun Maung Aye (6705140019) | KhunMaungAye | test_teardown.py |`).
2. **Remove Artificial Conflict Text:** Discard the placeholder test string `Creating Conflict`.
3. **Strip Conflict Markers:** Completely remove the `<<<<<<< HEAD`, `=======`, and `>>>>>>> ...` marker lines.
4. **Establish Uniform Formatting:** Introduce a dedicated `## Group Name` heading (`Unity Crew`) and preserve the pytest run instructions (`pytest -s test_teardown.py`).

The resolved section in [README.md] became:

```markdown
## Group Name
Unity Crew

## Who Did What

| Member                          | GitHub Username | File                                 |
| ------------------------------- | --------------- | ------------------------------------ |
| Aeint Kyi Pyar Soe (6705140003) | AeintKyiPyarSoe | bank.py, test_deposit.py, .gitignore |
| Htet Soe Lin (6705140023)       | Tyzonn22        | conftest.py                          |
| Khun Maung Aye (6705140019)     | KhunMaungAye    | test_teardown.py                     |
```

---

## 4. Why Git Could Not Automatically Resolve the Conflict

Git relies on a three-way merge algorithm comparing three snapshots: the common ancestor commit (`1ca4fd1`) and the tips of both branches (`99702a1` and `9c01c37`). 

Git could not resolve this automatically because **both branches concurrently modified the exact same contiguous lines** at the bottom of [README.md]:
- In the common ancestor (`1ca4fd1`), the line `Creating Conflict` existed.
- Branch A (Aeint Kyi Pyar Soe) deleted that line.
- Branch B (Khun Maung Aye) inserted a new table row immediately above that line while modifying the line ending.

Because both branches altered the identical file region in conflicting ways, Git had no objective programmatic logic to determine whether the user intended to delete the line, keep it, or append the table row. To prevent accidental data loss, Git halted the merge and handed control to the developers to resolve the ambiguity manually.

---
