import unittest
from datetime import time

import python_task
class TestMovieSystem(unittest.TestCase):

    def setUp(self):
        python_task.movies.clear()

    def test_add_movie(self):
        result = python_task.add_movie("Inception")
        self.assertIn("Inception", python_task.movies)
        self.assertIn("added", python_task.movies["Inception"])
        self.assertTrue(result.startswith("Movie 'Inception' added on"))

    def test_add_duplicate_movie(self):
        python_task.add_movie("Inception")
        result = python_task.add_movie("Inception")
        self.assertEqual(result, "Movie 'Inception' already exists.")

    def test_rate_movie_valid(self):
        python_task.add_movie("Inception")
        result = python_task.rate_movie("Inception", 5)
        self.assertEqual(result, "Rating 5 added for 'Inception'.")
        self.assertEqual(python_task.movies["Inception"]["ratings"], [5])

    def test_rate_movie_invalid_rating(self):
        python_task.add_movie("Inception")
        result = python_task.rate_movie("Inception", 6)
        self.assertEqual(result, "Rating must be between 1 and 5.")

    def test_rate_movie_not_found(self):
        result = python_task.rate_movie("Unknown", 3)
        self.assertEqual(result, "Movie not found.")

    def test_average_rating_with_ratings(self):
        python_task.add_movie("Inception")
        python_task.rate_movie("Inception", 4)
        python_task.rate_movie("Inception", 5)
        result = python_task.get_average_rating_for_movie("Inception")
        self.assertEqual(result, "Average rating for 'Inception': 4.50")

    def test_average_rating_without_ratings(self):
        python_task.add_movie("Inception")
        result = python_task.get_average_rating_for_movie("Inception")
        self.assertEqual(result, "No ratings yet for 'Inception'.")

    def test_average_rating_movie_not_found(self):
        result = python_task.get_average_rating_for_movie("Unknown")
        self.assertEqual(result, "Movie not found.")

    def test_average_ratings_all(self):
        python_task.add_movie("Inception")
        python_task.add_movie("Interstellar")
        python_task.rate_movie("Inception", 4)
        python_task.rate_movie("Inception", 2)
        python_task.rate_movie("Interstellar", 5)
        result = python_task.get_average_ratings_all()
        self.assertEqual(len(result), 2)
        self.assertTrue(result[0].startswith("Inception: 3.00"))
        self.assertTrue(result[1].startswith("Interstellar: 5.00"))

    def test_average_ratings_all_no_movies(self):
        result = python_task.get_average_ratings_all()
        self.assertEqual(result, ["No movies in the system."])



