total = 496
fonts_in_screen = 5
item = 496
if item + fonts_in_screen > total:
    fonts_in_screen = total - item
for i in range(fonts_in_screen):
    print(i+item)