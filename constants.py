"""
CONSTANTS

"""

# List of your favourites movies
SEARCH_LIST = ['star wars the phantom menace',
               'star wars attack of the clones',
               'star wars revenge of the sith',
               'star wars a new hope',
               'star wars the empire strikes back',
               'star wars return of the jedi',
               'star wars the force awakens']

# Your The Movie Database's API KEY
API_KEY = '2d04713836b6c361c0878f8334ff9bd7'

# URLs required to run script
SEARCH_URL = 'https://api.themoviedb.org/3/search/movie?api_key={api_key}&query={query}'  # NOQA
INFO_URL = 'https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}&language=en-US&append_to_response=videos'  # NOQA
IMAGE_URL = 'http://image.tmdb.org/t/p/w342/{poster_path}'
YOUTUBE_URL = 'https://www.youtube.com/watch?v={youtube_key}'
