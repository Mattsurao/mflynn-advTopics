import time

# checks if a number is even
# x should be an integer
def even_check(x):
    return x % 2 == 0:

# checks if a number is divisible by any of the numbers in a given list
# factors should be a list of integers
# x should be an integer
def check_for_factors(factors, x):
    for i in factors:
        if x % i == 0:
            return 

    while prime and i < int(x ** 0.5) + 1:
        if x % i == 0:
            prime = False
            factor = test[i]
        i += 2


def main():
    yn = "y" # input by the user if they want to check another number
    while yn == "y":
        # get a number from the user
        num = input("Enter a positive integer:  ")
        # make sure that the number is a number
        while not num.isdigit():
            num = input("That's not a positive integer! Try again:  ")
        num = int(num)
        # start the timer
        start_time = time.clock()
        # begin checking the number for factors
        prime = True
        factor = 0
        if num != 2:
            # see if it's even
            if even_check(num):
                prime = False
                factor = 2
            # test all the numbers found above
            else:
                i = 3
                while prime and i < len(test):
                    if num % test[i] == 0:
                        prime = False
                        factor = test[i]
                    i += 2
        if prime:
            print("Your number is prime! Sell it to the government now!")
        else:
            print("Your number isn't prime... what a shame.  "
            "It can be divided by " + str(factor))
        # find and display how long it took to test the number
        timer = time.clock() - start_time
        print("It took " + str(timer) + " seconds to figure that out")
        # ask the user for more numbers
        yn = input("Do you have anymore numbers? (y/n):  ")
        print("")
        yn = yn[0].lower()
    print("Goodbye")

main()
