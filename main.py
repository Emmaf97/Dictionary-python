import json

def load_dictionary(file_path: str) -> dict:                                  
    with open(file_path, 'r') as file:
        data: dict = json.load(file)
    return data

def check_match(user_input: str, dictionary: dict):
    found = False
    for key,value in dictionary.items():
        if key == user_input.lower():
            found = True
            print("{} and the meaning of this word is: {}".format(key,value))
    if found == False: 
        print("No such word exists.")

        
def main():
    dictionary = load_dictionary("dictionary.json")
    while True:
        user_input: str = input("Enter a word to look up definition: ")
        if user_input.lower == quit:
            break
        
        check_match(user_input,dictionary)

if __name__ == '__main__':
    main()