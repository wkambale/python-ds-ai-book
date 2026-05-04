age = 25
has_id = True
is_registered = False
# 'and' requires ALL conditions to be True
can_vote = age >= 18 and has_id and is_registered
print(f"Can vote (all conditions): {can_vote}")  # False
# 'or' requires AT LEAST ONE condition to be True
has_some_documentation = has_id or is_registered
print(f"Has some documentation: {has_some_documentation}")  # True
# 'not' inverts the boolean value
print(f"Is NOT registered: {not is_registered}")  # True