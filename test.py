from pytube import YouTube
def Download(link):
    youtube = YouTube(link)
    youtube = youtube.streams.get_lowest_resolution()
    try:
        youtube.download()
        print("Video downloaded successfully")
    except:
        print("An unexcepted error occured")

link = input("Enter youtube link here => ")
Download(link)