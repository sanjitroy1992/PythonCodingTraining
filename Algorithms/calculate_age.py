from datetime import date


def calculate_age(birthDate):
    today = date.today()
    boolean_condition = ((today.month, today.day) < (birthDate.month, birthDate.day))
    age = today.year - birthDate.year - boolean_condition
    return age

# Driver code
print(calculate_age(date(1992, 12, 12)), "years")