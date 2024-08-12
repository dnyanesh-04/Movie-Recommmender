from django.shortcuts import render
from .models import Movie
from django.core.exceptions import ObjectDoesNotExist

def home(request):
    # Get all movies
    all_movies = Movie.objects.all()

    # Get the set of all recommended movies
    recommended_movies = set()
    for movie in all_movies:
        for recommendation in movie.recommendations.all():
            recommended_movies.add(recommendation)

    # Filter out recommended movies from the list of all movies
    selectable_movies = [movie for movie in all_movies if movie not in recommended_movies]

    selected_movie = None
    recommendations = []

    if request.method == 'POST':
        movie_id = request.POST.get('movie_id')

        if movie_id:
            try:
                # Fetch the selected movie and its recommendations
                selected_movie = Movie.objects.get(id=movie_id)
                recommendations = selected_movie.recommendations.all()
            except Movie.DoesNotExist:
                # If movie doesn't exist, just reset selected_movie and recommendations
                selected_movie = None
                recommendations = []
        else:
            # Keep the same recommendations if no new movie is selected
            recommendations = recommendations

    context = {
        'movies': selectable_movies,
        'selected_movie': selected_movie,
        'recommended_movies': recommendations,
    }
    
    # Render the same page with the context
    return render(request, 'recommendations/home.html', context)
