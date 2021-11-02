temps = [221, 234, 340, -9999, 230] 

# Order for if statement only
if_temps = [temp / 10 for temp in temps if temp != -9999]

# Change order when have if else
if_else_temps = [temp / 10 if temp != -9999 else 0 for temp in temps]

print(if_temps)
print(if_else_temps)
