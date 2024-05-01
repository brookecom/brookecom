"""Project 3: Music Library by Brooke Comstock
    Purpose: Allows users to easily manage songs, playlists, and a play queue. """

class Song:
    # Initialize a Song object with specified attributes.
    # Default value for 'liked' is set to False.
    def __init__(self, title, album, artist, genre, year, rating):
        self.title = title
        self.album = album
        self.artist = artist
        self.genre = genre
        self.year = year
        self.rating = rating
        self.liked = False

class Library:
    # Initialize a music library with an empty list of songs.
    def __init__(self):
        self.songs = []

    # Add a new song to the library's collection.
    # Use the append method to add the song to the list.
    def add_song(self, song):
        self.songs.append(song)
        print(f"Song '{song.title}' added to the library!")

    # Mark a specific song as liked in the library.
    # Iterate through the list and updates the 'liked' attribute.
    def like_song(self, title):
        for song in self.songs:
            if song.title == title:
                song.liked = True
                print(f"Song '{title}' has been liked!")
            else:
                print(f"Song '{title}' not found in the library.")

    # Change the rating of a specific song in the library.
    # Iterate through the list and updates the 'rating' attribute
    def change_song_rating(self, title, new_rating):
        for song in self.songs:
            if song.title == title:
                song.rating = new_rating
                print(f"Rating for '{title}' updated to {new_rating}.")
            else:
                print(f"Song '{title}' not found in the library.")

    # Search for songs in the library based on the specified query.
    # Return a list of matching song titles.
    def search_songs(self, query):
        matching_songs = [ ]
        for song in self.songs:
            if song.title == query:
                matching_songs.append(song.title)
        if query in matching_songs:
            print(f"Song matches:")
            for song in matching_songs:
                print(f"- {song}")
        else:
            print(f"No songs found for '{query}'.")
        return matching_songs

class Playlist:
    # Initialize a playlist with an empty list of songs.
    def __init__(self):
        self.names = []
        self.plstsongs = []
    
    # Create a new playlist with the given name.
    # Use the append method to add the playlist name to the list.
    def create_playlist(self, name):
        self.name = name
        self.names.append(name)
        print(f"You've created the playlist '{name}'!")

    # Add a song to a specific playlist.
    # Use the append method to add the song to the playlist's song list.
    def add_song(self, song, playlist_name):
        self.plstsongs.append(song)
        print(f"Song '{song}' added to '{playlist_name}' playlist!")

    # Remove a song from the playlist.
    # Use the remove method to remove the song from the playlist's song list.
    def remove_song(self, title):
        if title in self.plstsongs:
            self.plstsongs.remove(title)
            print(f"Song '{title}' removed from '{self.name}' playlist!")
        else:
            print(f"Song '{title}' not found in '{self.name}' playlist.")

class Queue:
    
    # Initialize a play queue with an empty list of songs.
    def __init__(self):
        self.songs = []

    # Add a song to the play queue.
    # Use the append method to add the song to the list.
    def add_to_queue(self, song):
        self.songs.append(song)
        print(f"Song '{song}' added to the play queue!")

    # Play the songs in the queue and clear the queue.
    # Print the songs in the queue and reset the list to an empty state.
    def play_queue(self):
        if not self.songs:
            print("The play queue is empty.")
            return

        print("Now playing:")
        for song in self.songs:
            print(f"- {song}")

        self.songs = []  # Clear the queue after playing

#Correctly call back each appropriate class function in the user interface:
def run_interface(library, playlist, queue):

    option = 1

    while option in range(1,11):

        print("\nOptions:")
        print("\n1. Add a song to library")
        print("2. Like a song")
        print("3. Change song rating")
        print("4. Search for songs")
        print("5. Create a playlist")
        print("6. Add a song to a playlist")
        print("7. Remove a song from a playlist")
        print("8. View all playlists")
        print("9. Add a song to queue")
        print("10. Play the queue")
        print("11. Exit\n")

        option = int(input("\nEnter your choice: "))

        # Prompts user for song details and calls the add_song method.
        if option == 1:
            title = input("Enter song title: ")
            album = input("Enter song album: ")
            artist = input("Enter song artist: ")
            genre = input("Enter song genre: ")
            year = input("Enter song year: ")
            rating = int(input("Enter song rating (1-5): "))
            song = Song(title, album, artist, genre, year, rating)
            library.add_song(song)

        # Prompts user for the song title and calls the like_song method.
        elif option == 2:
            title = input("Enter song title to like: ")
            library.like_song(title)

        #Prompts user for song title and new rating, then calls change_song_rating.
        elif option == 3:
            title = input("Enter song title: ")
            new_rating = int(input("Enter new rating (1-5): "))
            library.change_song_rating(title, new_rating)

        # Prompts user for search criteria and calls the search_songs method.
        elif option == 4:
            query = input(f"Enter song title: ")
            library.search_songs(query)

        # Prompts user for the playlist name and calls the create_playlist method.
        elif option == 5:
            name = input("Enter name for the new playlist: ")
            playlist.create_playlist(name)

        # Prompts user for song title and playlist name, then calls add_song method.
        elif option == 6:
            title = input("Enter song title: ")
            playlist_name = input("Enter playlist name: ")
            matching_songs = library.search_songs(title)

            if title in matching_songs:
                playlist_found = playlist.names
                if playlist_name in playlist_found:
                    playlist.add_song(title, playlist_name)
                else:
                    print(f"Playlist '{playlist_name}' not found.")

        # Prompts user for song title and playlist name, then calls remove_song method.
        elif option == 7:
            title = input("Enter song title to remove: ")
            playlist_name = input("Enter playlist name: ")
            matching_songs = library.search_songs(title)

            if title in matching_songs:
                playlist_found = playlist.names
                if playlist_name in playlist_found:
                    playlist.remove_song(title)
                else:
                    print(f"Playlist '{playlist_name}' not found.")
        
        # Calls print method to show names of all playlists.
        elif option == 8:
            print(f"Available playlists: {playlist.names}")

        # Prompts user for song title and calls add_to_queue method.
        elif option == 9:
            title = input("Enter song title: ")
            song = library.search_songs(title)[0]
            queue.add_to_queue(song)

        # Calls play_queue method to print and clear the play queue.
        elif option == 10:
            queue.play_queue()

        # Prints a farewell message and exits the loop.
        elif option == 11:
            print("Thank you for using the music library. Goodbye!")

        else:
            print("Invalid option. Please choose a valid option.")

# Test the addition of a song to the library.
def test_add_song():
    library = Library()
    song = Song("Test Song", "Test Album", "Test Artist", "Test Genre", 2021, 4)
    library.add_song(song)
    assert song in library.songs, "Adding a song to the library failed"

# Test the functionality of liking a song in the library.
def test_like_song():
    library = Library()
    song = Song("Test Song", "Test Album", "Test Artist", "Test Genre", 2021, 4)
    library.add_song(song)
    library.like_song("Test Song")
    assert any(song.liked for song in library.songs), "Liking a song failed"

# Test the functionality of changing the rating of a song in the library.
def test_change_song_rating():
    library = Library()
    song = Song("Test Song", "Test Album", "Test Artist", "Test Genre", 2021, 4)
    library.add_song(song)
    library.change_song_rating("Test Song", 5)
    updated_song = next((s for s in library.songs if s.title == "Test Song"), None)
    assert updated_song.rating == 5, "Changing song rating failed"

# Test the search functionality for songs in the library.
def test_search_songs():
    library = Library()
    song1 = Song("Song1", "Album1", "Artist1", "Genre1", 2020, 4)
    song2 = Song("Song2", "Album2", "Artist2", "Genre2", 2019, 5)
    library.add_song(song1)
    library.add_song(song2)

    matching_songs = library.search_songs("Song1")
    assert matching_songs == ["Song1"], "Search for songs failed"
    matching_songs = library.search_songs("Song2")
    assert matching_songs == ["Song2"], "Search for songs failed"


# Run the tests
test_add_song()
test_like_song()
test_change_song_rating()
test_search_songs()

library = Library()
playlist = Playlist()
queue = Queue()

 # Run the user interface for interacting with the music library
run_interface(library, playlist, queue)
