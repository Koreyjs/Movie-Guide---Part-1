def movie_guide():
    print("The Movie List Program")
    print()
    print("COMMAND MENU")
    print()
    print("list - List all movies")
    print("add - Add a movie")
    print("delete - Delete a movie")
    print("exit - Close the application")

def list(movie_list):
    for i, movie in enumerate(movie_list, start = 1):
        print(f"{i}. {movie}")
        print()

def add(movie_list):
    movie = input("Name:    ")
    movie_list.append(movie)
    print(f"{movie} was added. \n")

def delete(movie_list):
    number = int(input("Number: "))
    if number < 1 or number > len(movie_list):
        print("Invalid movie number.    \n")
    else:
        movie = movie_list.pop(number - 1)
        print(f"{movie} was deleted. \n")



