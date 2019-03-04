baseball = ["Ramirez", "Rizzo", "Chavez", "Altuve", "Verlander", "Miley", "Incarnacion"]

print(f"Length of my array is {len(baseball)}")

for index in range (0,len(baseball)):
    print (baseball[index])

for baseballs in baseball:
    print (baseballs)

baseball.append("Harry")
for baseballs in baseball: 
    print(baseballs)

baseball.insert(1, "Twat")
for baseballs in baseball:
    print(baseballs)