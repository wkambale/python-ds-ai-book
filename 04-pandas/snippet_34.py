# Knowledge Check: Filter and aggregation
# Expression:
# df[df['amount'] > 1000]['category'].value_counts()
#
# a) All rows where amount > 1000
# b) The count of each category for rows where amount > 1000 (Correct)
# c) An error because of chained indexing
# d) The sum of amounts by category