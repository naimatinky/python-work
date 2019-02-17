from datetime import datetime
def ageBracket():
    try:
        current_year=datetime.now().year
        input_year=int(input("Please enter your year of Birth \n"))
        current_age = current_year  - input_year
        if(current_age <18):
                print("You are a Minor")
        elif(current_age>=18 and current_age< 36):
                print("You are a Youth")
        else:
             print("You are an Elder")
    except ValueError:
        print("This is not a valid year")

if __name__== "__main__":
    ageBracket()
