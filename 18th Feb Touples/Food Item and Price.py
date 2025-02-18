def food():
    l = [("Burger", 40), ("Pizza", 200), ("Lasagna", 500)]
    for i in l:
        if isinstance(i, tuple):
            for j in i:
                 if isinstance(j,int):
                  min = j
food()