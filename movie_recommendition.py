def get_movies_by_genre(genre, movie_data):
    """
    Function to filter movies by genre.
    Args:
        genre (str): the genre to filter by.
        movie_data (list): A list of moviue dictionaries.
    returns:
        list: A list of movies matching the genre"""
    
    matching_movies = []

    for movie in movie_data:

        if genre.lower() in movie['genre'].lower():
            matching_movies.append(movie)

    return matching_movies

def recommend_movies(user_genre):
    """
    Function to recommend movies based on user genre.
    Args:
        user_genre(str): The genre provided by the user.
    returns:
        None
    """
    
    movie_data = [
        
        {"title": "The Shawshank Redemption", "genre": "Drama"},
        {"title": "The Godfather", "genre": "Crime, Drama"},
        {"title": "The Dark Knight", "genre": "Action, Crime, Drama"},
        {"title": "Pulp Fiction", "genre": "Crime, Drama"},
        {"title": "The Lord of the Rings: The Fellowship of the Ring", "genre": "Adventure, Fantasy"},
        {"title": "Forrest Gump", "genre": "Drama, Romance"},
        {"title": "Inception", "genre": "Action, Adventure, Sci-Fi"},
        {"title": "Fight Club", "genre": "Drama"},
        {"title": "Interstellar", "genre": "Adventure, Drama, Sci-Fi"},
        {"title": "The Matrix", "genre": "Action, Sci-Fi"},

    ]

    recommendations = get_movies_by_genre(user_genre, movie_data)

    if recommendations:
        print(f"Here are some {user_genre} movies you might like:")
        for movie in recommendations:
            print(f"- {movie['title']}")
    else:
        print(f"Sorry, no{user_genre} movies were found in our database.")


# Main program
print("Welcome to the Movie Recommmendation System!")
user_input_genre = input("Enter a genre (e.g., Drama, Action, Sci-Fi):")
recommend_movies(user_input_genre)