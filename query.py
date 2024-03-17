from movies import Movies

movies = Movies('./movies.txt')

def __menu__():

    while True:
        menu = input("Enter an option (or 'q' for quit): ")

        if menu == "q" :
            print("Exiting the program.")
            exit()
        else:
            print("Invalid option. Please, enter again: ")

__menu__()
