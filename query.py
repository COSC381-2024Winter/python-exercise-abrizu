from movies import Movies

movies = Movies('./movies.txt')

def __menu__():

    while True:
        print("\n\n-- Movie Menu --")
        print("[l] : View movie list")
        print("[q] : Exit")

        menu = input("\nEnter an option: ")

        if menu == "q" :
            print("Exiting the program.")
            exit()
        elif menu == "l":
            for movie in movies._movies:
                print(movie['name'])
        else:
            print("Invalid option. Please, enter again: ")

__menu__()
