def count_of_digits(number):

    digits = 0
    while number > 0:
        digits += 1
        number //= 10
    return digits


def is_armstrong(number):

    digits = count_of_digits(number)
    reverse_number = 0

    original_number = number

    while number > 0:
        rem = number % 10
        reverse_number += rem ** digits
        number //= 10
    return reverse_number == original_number



def main():

    print("Welcome to the Armstrong Number Checker!")
    print("Enter a number and I will check if it's an Armstrong number.")
    print("Type -1 to quit.\n")

    while True:

        try:

            number = int(input("Enter the number :\n"))

            if number == -1:
                print('Goodbye!')
                break
            
            if number < 0:
                print('Please enter a non-negative number.')
                continue

            if is_armstrong(number=number):
                print(f'Given Number is the Armstrong Number - {number}')
            else:
                print(f'Given Number is not the Armstrong Number - {number}')
        
        except ValueError:
            print("Invalid input! Please enter a valid integer.")


if __name__ == '__main__':
    main()

