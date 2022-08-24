
def email_parser(email):
    '''
    Receive the email as input in form of firstname.lastname@domain and return first name, last name and domain.
    '''
    name, host = email.split('@')
    first_name, last_name = name.split('.')
    host, domain_name = host.split('.')
    return first_name, last_name, host


def integer_to_roman(num:int) -> str:
    '''
    Given a Positive Intger, return the Roman numeral representation
    '''
    if not (0 < num < 4000):
        return 'Invalid Input'
    roman_numeral_map = (('M',  1000),
                         ('CM', 900),
                         ('D',  500),
                         ('CD', 400),
                         ('C',  100),
                         ('XC', 90),
                         ('L',  50),
                         ('XL', 40),
                         ('X',  10),
                         ('IX', 9),
                         ('V',  5),
                         ('IV', 4),
                         ('I',  1))
    result = ''
    for numeral, value in roman_numeral_map:
        while num >= value:
            result += numeral
            num -= value
    return result

def bmi(height:int, weight: int) -> str:
    '''
    Given Height and Weight, calculate the BMI and categorize the result in Underweight, Normal, Overweight or Obese.
    '''
    bmi = weight / (height / 100) ** 2
    if bmi < 18.5:
        return 'Underweight'
    elif bmi < 25:
        return 'Normal'
    elif bmi < 30:
        return 'Overweight'
    else:
        return 'Obese'


def email_parser_runner():
    email = input('Enter your email: ')
    first_name, last_name, host = email_parser(email)
    print(f'First Name: {first_name}')
    print(f'Last Name: {last_name}')
    print(f'Host: {host}')

def integer_to_roman_runner():
    num = int(input('Enter a number: '))
    print(f"Roman Representation of {num} is {integer_to_roman(num)}")

def bmi_runner():
    height = int(input('Enter your height(cm): '))
    weight = int(input('Enter your weight(kg): '))
    print("You are ",bmi(height, weight))

def main():
    '''
    Create A menu based runner for the above functions.
    '''
    while True:
        print(" ------------------------------- ")
        print('1. Email Parser')
        print('2. Integer to Roman')
        print('3. BMI')
        print('4. Exit')
        choice = int(input('Enter your choice: '))
        if choice == 1:
            email_parser_runner()
        elif choice == 2:
            integer_to_roman_runner()
        elif choice == 3:
            bmi_runner()
        elif choice == 4:
            break
        else:
            print('Invalid Choice')

if __name__ == "__main__":
    main()
# a Major thanks to Github and Github Copilot for the help in this program.