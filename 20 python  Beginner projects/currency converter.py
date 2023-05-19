def main():
    print("This program convert US dollars to pound Sterling")
    print()


dollars =eval(input("Enter ammount in dollars: "))
pounds = convert_to_pounds(dollars)

print("That is" , pounds, "pounds. ")

convert_to_pounds = lambda dollars: dollars * 0.82

main()
