def main():
    x = int(input("what is r: "))
    if is_even(x):
        print("r is even")
    else:
        print("r is odd")

def is_even(n):
    return n % 2 == 0
main()