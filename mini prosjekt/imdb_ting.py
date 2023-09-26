movie_runtimes = {
    "The Batman": 0,
    "No Time To Die": 163,
    "Dune": 155,
    "Avengers: Endgame": 181,
    "The Godfather": "x",
    "The Lord of the Rings: The Return of the King": 201,
    "Seven Samurai": 207,
    "Gone With The Wind": 238,
    "Lawrence of Arabia": 227,
    "The Clock": 1440
}

print(movie_runtimes)

def fiks(dict):
    for film, tid in dict.items():
        if not isinstance(tid,int):
            movie_runtimes[film]=0

fiks(movie_runtimes)
print(movie_runtimes)