print("Hello")

def check_adulthood(year_of_birth):
    current_year = 2024
    age = current_year - year_of_birth
    if age >= 18:
         print("Ви повнолітній.")
    else:
         print("Ви не повнолітній.")

year_of_birth = int(input("Ведіть ваш вік: "))
check_adulthood(year_of_birth)
