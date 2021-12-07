w = float(input())
h = float(input())

desk = 2
door = 1

rows_workspaces = (h - 1) // 0.7
columns_workspaces = w // 1.2
workspaces = rows_workspaces * columns_workspaces - desk - door
print(workspaces)