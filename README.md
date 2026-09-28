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

# How to run

To see the setup/teardown output clearly, use:

```bash
pytest -s test_teardown.py
```

The `-s` flag disables pytest output capturing, so the `print("[setup]")` and `print("[teardown]")` messages are visible.
