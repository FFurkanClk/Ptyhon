from youtubesearchpython import VideosSearch
import webbrowser

def play_song(song_name):
    search = VideosSearch(song_name)
    result = search.result()

    # Extract the URL of the first video from the search results
    video_url = result["result"][0]["link"]
    
    # Open the video URL in a web browser to play the song
    webbrowser.open(video_url)

# Take user input for the song name
song_name = input("Enter song name: ")

play_song(song_name)
print("Song will play....")
x1 = "q"
while True:
    print("For exit press 'q'")

    x = input("")
    if( x1 == x):
      print("For exit press q")
      break
        
