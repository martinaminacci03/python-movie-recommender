import random

movies = {
    "azione": [
        "Mad Max: Fury Road",
        "John Wick",
        "The Dark Knight",
        "Gladiator"
    ],
    "commedia": [
        "The Mask",
        "Superbad",
        "Step Brothers",
        "Mean Girls"
    ],
    "fantascienza": [
        "Interstellar",
        "The Matrix",
        "Inception",
        "Blade Runner 2049"
    ]
}

print("🎬 Movie Recommendation System")

genre = input("Scegli un genere (azione, commedia, fantascienza): ").lower()

if genre in movies:
    recommendation = random.choice(movies[genre])
    print("Ti consiglio di guardare:", recommendation)
else:
    print("Genere non trovato.")