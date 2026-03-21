from datetime import datetime
import os

mood = input("how is your mood now: ")
work = input("What you did today: ")
goal = input("What is your goal for tomorrow: ")
date = datetime.now().strftime("%Y-%m-%d")

filename = f"{date}.txt"
with open(filename, "a") as diary:
  diary.write(f"Date: {date}\n")
  diary.write(f"Mood: {mood}\n")
  diary.write(f"Work: {work}\n")
  diary.write(f"Goal: {goal}\n")
  diary.write("--------------------\n")

search = input("Enter Keyword: ")

total = 0
for file in os.listdir():
  if file.endswith(".txt"):
    with open(file, 'r') as diary:
      content = diary.read()
      appearance = content.lower().count(search.lower())
      total += appearance

print(f"Total occurrences in all files: {total}")