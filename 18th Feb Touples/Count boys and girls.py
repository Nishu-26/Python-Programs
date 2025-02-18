def cricket():
 tp = [ ('Rohit', 'Shubman'), 'Smriti', ('Virat', 'SHreyas'), 'Perry', 'Harmanpreet']
 boys = sum(1 for i in tp if isinstance(i,tuple) for _ in i)
 girls = sum(1 for i in tp if isinstance(i,str))

 print("Number of Boys:", boys)
 print("Number of Girls:", girls)
 print("Total = Thala for a reason.")
cricket()