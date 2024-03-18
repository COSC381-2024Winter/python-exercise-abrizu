from movies import Movies

movies = Movies('./movies.txt')

def __menu__():

    while True:
        print("\n\n-- Movie Menu --")
        print("[l] : View movie list")
        print("[s] : Search for a movie")
        print("[q] : Exit")

        menu = input("\nEnter an option: ")

        if menu == "q" :
            print("Exiting the program.")
            exit()
        elif menu == "l":
            for movie in movies._movies:
                print(movie['name'])
        elif menu == "s":
            searchMovie = input("\nSearch for a movie: ")
            __search__(searchMovie)
        else:
            print("Invalid option. Please, enter again: ")

def __search__(search):
    found_movies = movies.search_movies(search)
    if found_movies:
        print(", ".join(found_movies))
    else:
        print("No movies found.")

__menu__()
