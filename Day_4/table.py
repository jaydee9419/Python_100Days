line1 = [" ", " ", " "]
line2 = [" ", " ", " "]
line3 = [" ", " ", " "]
map = [line1, line2, line3]


print("Hiding your treasure: X marks the spot.")

position = input("Please enter the position: ")

latter = position[0].lower()

abc = ['a', 'b', 'c']
latter_index = abc.index(latter)
number_index = int(position[1]) -1
map[number_index][latter_index] = 'x'

print(f"{line1}\n{line2}\n{line3}")


