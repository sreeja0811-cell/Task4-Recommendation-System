movies = {
"action": [
"Avengers",
"Batman Begins",
"Mad Max: Fury Road",
"John Wick",
"Mission Impossible"
],

"comedy": [
    "The Mask",
    "Home Alone",
    "Mr. Bean",
    "Jumanji",
    "Rush Hour"
],

"science fiction": [
    "Interstellar",
    "Inception",
    "The Matrix",
    "Avatar",
    "The Martian"
],

"drama": [
    "The Pursuit of Happyness",
    "Forrest Gump",
    "The Shawshank Redemption",
    "Green Book",
    "A Beautiful Mind"
]


}

print("=" * 60)
print("🎬 MOVIE RECOMMENDATION SYSTEM")
print("=" * 60)

print("\nAvailable Genres:")

for genre in movies:
    print(f"- {genre.title()}")

user_choice = input("\nEnter your favorite genre: ").lower()

if user_choice in movies:
    print("\n🎯 Recommended Movies:\n")

    for movie in movies[user_choice]:
        print("⭐", movie)

else:
    print("\n❌ Genre not found.")
    print("Please choose from the available genres.")

