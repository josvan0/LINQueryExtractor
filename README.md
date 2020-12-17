# LINQ Query Extractor

When do a SQL profile on a LINQ request, extract the query from LINQ instruction with params values setted for evaluate query perfomance.

## Exe file generation instructions

1. Install **pyinstaller**.
2. Execute the follow command in folder **src** location:

```python
pyinstaller --onefile extractor.py
```

3. **Exe file is located in:** `./dist/extractor.exe`
