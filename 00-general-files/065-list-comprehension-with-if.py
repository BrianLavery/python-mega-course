temps = [221, 234, 340, -9999, 230] # Sometimes orgs use a specific value to mean no data

new_temps = [temp / 10 for temp in temps if temp != -9999]

print(new_temps)