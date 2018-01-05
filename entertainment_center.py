import media
import fresh_tomatoes

# Creates Movie objects for each of my favorite movies
the_fountain = media.Movie("The Fountain", "Hugh Jackman tries to find "
                           "the cure for cancer.",
                           "https://images-na.ssl-images-amazon."
                           "com/images/M/MV5BMTU5OTczMTcxMV5BMl5BanBnXkFtZTc"
                           "wNDg3MTEzMw@@._V1_UX182_CR0,0,182,268_AL_.jpg",
                           "https://www.youtube.com/watch?v=dAuxryJ6pv8")

eternal_sunshine = media.Movie("Eternal Sunshine of the Spotless Mind",
                               "Jim Carrey goes through a mind bending "
                               "journey while trying to erase his "
                               "ex-girlfriend from his memory",
                               "https://i.ytimg.com/vi/NnqPCBAp2fM/"
                               "movieposter.jpg",
                               "https://www.youtube.com/watch?v=GBEke6JixyE")

drive = media.Movie("Drive", "Ryan Gosling is a Hollywood stuntman that "
                    "also acts as a getaway driver.",
                    "http://t3.gstatic.com/images?"
                    "q=tbn:ANd9GcR_8gJBIwyEVuJsJRU0JQmm7ZJhZ3"
                    "_uS8dpWW4Xd2_Kgv8wIPx4",
                    "https://www.youtube.com/watch?v=KBiOF3y1W0Y")

movies = [the_fountain, eternal_sunshine, drive]

print(movies[0].__doc__)
# Calls provided function to generate a web page
fresh_tomatoes.open_movies_page(movies)
