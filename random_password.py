import random
import string
def generate_password(length):
    if length<6:
        print("password should be atleast 6 characters  long for better security.")
        return None
    
    #Define possible characters: letters,digits and punctuation
    characters=string.ascii_letters+string.digits+string.punctuation

    #Use random.choices() to select random characters
    password=''.join(random.choices(characters,k=length))
    return password

def main():
    print("==Random Password generator==")
    try:
        length=int(input("Enter the desired password length:"))
        password=generate_password(length)
        if password:
            print(f"\nGenerated Password: {password}")
    except ValueError:
        print("Please enter a valid number.")
        
if __name__ == "__main__":
    main() 