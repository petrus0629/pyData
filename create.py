import sqlite3

print(sqlite3.version)
print(sqlite3.sqlite_version)
print("Made by Peter")

conn = sqlite3.connect("test.db")

c = conn.cursor()
