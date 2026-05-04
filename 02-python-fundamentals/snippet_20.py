python_developers = {"Alice", "Bob", "Charlie", "Diana"}
data_scientists = {"Charlie", "Diana", "Eve", "Frank"}

# Union: People who are either Python developers OR data scientists (or both)
all_tech = python_developers | data_scientists
print(f"Union: {all_tech}")

# Intersection: People who are BOTH Python developers AND data scientists
both_skills = python_developers & data_scientists
print(f"Intersection: {both_skills}")

# Difference: Python developers who are NOT data scientists
python_only = python_developers - data_scientists
print(f"Difference: {python_only}")