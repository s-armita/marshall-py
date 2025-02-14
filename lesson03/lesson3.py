# Lesson 3
# Maximum square side length based on input
tiles = input("Enter the number of tiles: ")
tiles = int(tiles)
calculation = int((tiles ** 0.5) // 1)
print(f"The maximum side length is: {calculation}")