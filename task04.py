#task 4
all_students = {"Alice", "Bob", "Charlie", "David", "Eve", "Frank"}
football_players = {"Alice", "Bob", "David"}
cricket_players = {"Bob", "Charlie", "Eve"}

both = football_players & cricket_players

only_one = football_players ^ cricket_players

none = all_students - (football_players | cricket_players)

print("Students who play both football and cricket:", both)
print("Students who play only one of the two:", only_one)
print("Students who play neither:", none)
