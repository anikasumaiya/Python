# you are given a list of programming languages: ["python", "java", "C++", "python", "C"]
# Convert it into a list and print how many unique languages that divya knows.

programmingLang = ["python", "java", "C++", "python", "C"]

print(type(programmingLang))
print(programmingLang)

programmingSet = set(programmingLang )
print(type(programmingSet))
print(programmingLang)
print("Divya knows unique languages", len(programmingSet))
