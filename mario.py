def print_square(size):
    # for each row in a square
    for i in range(size):
        # print a row of size hashes / bricks
        for j in range(size):
            # print a single brick
            print("#", end="")
        print()

def main():
    print_square(3)

main()