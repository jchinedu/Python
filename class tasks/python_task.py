from datetime import datetime

movies = {}

def add_movie(name):
    if name in movies:
        return f"Movie '{name}' already exists."
    movies[name] = {
        "added": datetime.now(),
        "ratings": []
    }
    return f"Movie '{name}' added on {movies[name]['added']}"

def rate_movie(name, rating):
    if name not in movies:
        return "Movie not found."
    if not (1 <= rating <= 5):
        return "Rating must be between 1 and 5."
    movies[name]['ratings'].append(rating)
    return f"Rating {rating} added for '{name}'."


def get_average_rating_for_movie(name):
    if name not in movies:
        return "Movie not found."
    ratings = movies[name]['ratings']
    if not ratings:
        return f"No ratings yet for '{name}'."
    avg = sum(ratings) / len(ratings)
    return f"Average rating for '{name}': {avg:.2f}"


def get_average_ratings_all():
    if not movies:
        return ["No movies in the system."]
    result = []
    for name, info in movies.items():
        ratings = info['ratings']
        avg = sum(ratings) / len(ratings) if ratings else 0
        result.append(f"{name}: {avg:.2f} (added on {info['added']})")
    return result

