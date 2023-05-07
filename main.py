from channel_processor import channel_processor

def main_menu():
    print("1. Use a function")
    print("2. Display channel or parameter")
    print("3. Quit")

def function_menu():
    print("1. Y = mX + c")
    print("2. B = A + Y & b = mean(B)")
    print("3. A = 1 / X")
    print("4. C = X + b")

def variable_menu():
    print("Channels: A, B, C, X, Y")
    print("Parameters: m, c, b")

if __name__ == "__main__":
    cp = channel_processor()
    while True:
        main_menu()
        choice = input("Enter your choice: ")
        if choice == "1":
            function_menu()
            f_choice = input("Enter your choice: ")
            if f_choice == "1": cp.func1()
            elif f_choice == "2": cp.func2()
            elif f_choice == "3": cp.func3()
            elif f_choice == "4": cp.func4()
            else: print("Aborting - input needs to be between 1 and 4.")
            print()

        elif choice == "2":
            variable_menu()
            c_choice = input("Select which channel or parameter to view (Input variable's letter)")
            if c_choice ==  "A": print(cp.A)
            elif c_choice ==  "B": print(cp.B)
            elif c_choice ==  "C": print(cp.C)
            elif c_choice ==  "X": print(cp.X)
            elif c_choice ==  "Y": print(cp.Y)
            elif c_choice ==  "m": print(cp.m)
            elif c_choice ==  "c": print(cp.c)
            elif c_choice ==  "b": print(cp.b)
            else: print("Aborting - input needs to be one of the variables")
            print()
            
        elif choice == "3": 
            print("Aborting")
            break