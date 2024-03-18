from movies import Movies

movies = Movies('./movies.txt')

def __menu__():

    while True:
        print("\n\n-- Movie Menu --")
        print("[l] : View movie list")
        print("[s] : Search for a movie")
        print("[c] : Search movies by cast member")
        print("[q] : Exit")

        menu = input("\nEnter an option: ")

        if menu == "q" :
            print("Exiting the program.")
            exit()
        elif menu == "l":
            i = 1
            for movie in movies._movies:
                print(i,": ", movie['name'])
                i += 1
        elif menu == "s":
            searchMovie = input("\nSearch for a movie: ")
            __search__(searchMovie)
        elif menu == "c":
            searchCast = input("\nSearch for a cast member: ")
            __search_by_cast__(searchCast)
        else:
            print("Invalid option. Please, enter again: ")

def __search__(search):
    found_movies = movies.search_movies(search)
    if found_movies:
        print(", ".join(found_movies))
    else:
        print("No movies found.")

def __search_by_cast__(search_cast):
    found_movies = movies.search_cast(search_cast)
    if found_movies:
        for movie, cast_member in found_movies:
            print(movie)
            print(f"['{cast_member.strip()}']")
    else:
        print("No cast members found.")

__menu__()
