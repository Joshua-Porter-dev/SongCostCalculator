SongAmmount = float(input("How many songs would you like to purchase today? "))
TotalCost = SongAmmount * 0.99

print(f"You wanted to buy {SongAmmount} songs, that will cost you ${TotalCost}")

# SongAmmount must be turned into a float because by default, the value returned from an input is a string
# The print statement utailizes f strings as a way to pass variables directly into a strings
