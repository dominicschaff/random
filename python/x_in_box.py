# #########
# #   @   #
# #  @ @  #
# # @   @ #
# #@     @#
# # @   @ #
# #  @ @  #
# #   @   #
# #########


def display(size):
    h = size // 2
    for y in range(size):
        line = ''
        for x in range(size):
            char = ' '
            if y == 0 or y == size - 1 or x == 0 or x == size - 1:
                char = '#'
            if 0 < x < size - 1 and 0 < y < size - 1:
                if h - x + 1 == y:
                    char = '@'
                if x - h + 1 == y:
                    char = '@'
                if size - (h - x + 1) == y + 1:
                    char = '@'
                if size - (x - h + 1) == y + 1:
                    char = '@'

            line += char
        print(line)

for i in range(5, 16, 2):
    print(f"Showing for {i}")
    display(i)
