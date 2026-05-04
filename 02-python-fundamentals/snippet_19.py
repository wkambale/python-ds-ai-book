# A list of tags for a blog post, with duplicates
tags_list = ["technology", "africa", "python", "ai", "africa", "data"]

# Convert the list to a set to get only the unique tags
unique_tags = set(tags_list)
print(f"List with duplicates: {tags_list}")
print(f"Set of unique tags: {unique_tags}")

# Sets are highly optimized for membership testing
print(f"Is 'python' a tag? {'python' in unique_tags}")
print(f"Is 'business' a tag? {'business' in unique_tags}")