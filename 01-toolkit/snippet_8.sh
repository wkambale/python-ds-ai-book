# 1. Check the status. Git sees a new, "untracked" file in your working directory.
git status

# 2. Add the file to the staging area.
git add analysis.py

# 3. Check the status again. Git now sees the file is "staged for commit."
git status

# 4. Commit the staged changes to the repository with a clear message.
git commit -m "Initial commit: Add load_data function"