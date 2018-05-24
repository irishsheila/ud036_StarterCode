import fresh_tomatoes
import media

#instances of movies created to be used by fresh_tomatoes file

star_wars_4 = media.Movie("Star Wars: A New Hope",
                          "A young man saves the galaxy against the evil Empire.",
                          "https://upload.wikimedia.org/wikipedia/en/8/87/StarWarsMoviePoster1977.jpg",  # NOQA
                          "https://www.youtube.com/watch?v=1g3_CFmnU7k")  

harry_potter_1 = media.Movie("Harry Potter & The Sorcerer's Stone",
                            " A boy wizard battles for his life with the Dark "
                             "Lord who murdered his parents.",
                             "https://vignette.wikia.nocookie.net/harrypotter/images/6/64/Harry-Potter-and-the-Sorcerers-Stone-2001-Hindi-Dubbed-Movie-Watch-Online.jpg/revision/latest?cb=20130803161550",  # NOQA
                             "https://www.youtube.com/watch?v=VyHV0BRtdxo")

hunger_games = media.Movie("Hunger Games",
                           "Teens fight to the death.",
                           "https://upload.wikimedia.org/wikipedia/en/4/42/HungerGamesPoster.jpg", # NOQA
                           "https://www.youtube.com/watch?v=4S9a5V9ODuY")

avengers = media.Movie("The Avengers",
                       "Superheroes save the world from aliens.",
                       "https://upload.wikimedia.org/wikipedia/en/f/f9/TheAvengers2012Poster.jpg", # NOQA
                       "https://www.youtube.com/watch?v=VnLnkwpIBpA")

deadpool = media.Movie("Deadpool",
                       "Ugly snarky antihero saves his girlfriend.",
                       "https://upload.wikimedia.org/wikipedia/en/4/46/Deadpool_poster.jpg", # NOQA
                       "https://www.youtube.com/watch?v=Xithigfg7dA")

thirteen_thirty = media.Movie("13 Going On 30",
                              "A teen wishes herself to adulthood.",
                              "https://upload.wikimedia.org/wikipedia/en/a/aa/13_Going_on_30_film_poster.png",  # NOQA
                               "https://www.youtube.com/watch?v=SApIKVq1iJQ")

infinity_war = media.Movie("The Avengers: Infinity War",
                           "The Avengers attempt to stop Thanos from finding "
                           "all the Infinity Stones.",
                           "https://upload.wikimedia.org/wikipedia/en/4/4d/Avengers_Infinity_War_poster.jpg",  # NOQA
                           "https://www.youtube.com/watch?v=6ZfuNTqbHE8")

lotr_fellowship = media.Movie("Lord of the Rings: Fellowship of the Ring",
                              "A hobbit sets out to destroy the One Ring.",
                              "https://upload.wikimedia.org/wikipedia/en/9/9d/The_Lord_of_the_Rings_The_Fellowship_of_the_Ring_%282001%29_theatrical_poster.jpg",  # NOQA
                              "https://www.youtube.com/watch?v=aStYWD25fAQ")

serenity = media.Movie("Serenity",
                       "Movie for the best cancelled TV show ever",
                       "https://upload.wikimedia.org/wikipedia/en/9/9e/Serenity_One_Sheet.jpg",  # NOQA
                       "https://www.youtube.com/watch?v=w8JNjmK5lfk")

thor_ragnarok = media.Movie("Thor: Ragnarok",
                            "Thor battles his sister Hella for control of Asgard.",
                            "https://upload.wikimedia.org/wikipedia/en/7/7d/Thor_Ragnarok_poster.jpg",  #NOQA
                            "https://www.youtube.com/watch?v=ue80QwXMRHg")

oceans_11 = media.Movie("Ocean's 11",
                        "Ocean assembles a team to rob a casino.",
                        "https://upload.wikimedia.org/wikipedia/en/6/68/Ocean%27s_Eleven_2001_Poster.jpg",  # NOQA
                        "https://www.youtube.com/watch?v=ImMGNQ2OEjo")

holiday = media.Movie("The Holiday",
                      "Two women switch lives to get away from heartbreak",
                      "https://upload.wikimedia.org/wikipedia/en/6/60/Theholidayposter.jpg",  # NOQA
                      "https://www.youtube.com/watch?v=BDi5zH18vxU")

# array for arguement to be used for the open_movies function
movies = [star_wars_4, serenity, harry_potter_1, hunger_games, avengers,
          deadpool,thirteen_thirty, infinity_war, lotr_fellowship,
          thor_ragnarok, oceans_11, holiday]

# calls the open_movies function from the fresh_tomatoes file with the movies
# array as its argument
fresh_tomatoes.open_movies_page(movies)

                        
