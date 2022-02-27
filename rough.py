# def get_integer_value():
#   user_value = input("Enter an integer: ")
#   print(type(user_value))
#   try:
#     return int(user_value)
#   except ValueError:
#     print(f"{user_value} is not a valid integer. Please try again.")
#     return get_integer_value()


# if __name__ == "__main__":
#   print(f"You have inserted: {get_integer_value()}")

def sumDigits(s):
    """Assumes s is a string
       Returns the sum of the decimal digits in s
       For example is s is 'a2b3c' it returns 5"""
    total = 0
    for i in s:
        try:
            total += int(i)
            print(total)
        except ValueError:
            print("Ignoring exception")
    return total

sumDigits('a2b3c')