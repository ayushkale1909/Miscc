from pytube import YouTube
from youtube_transcript_api import YouTubeTranscriptApi

def download_video_with_subtitles(url):
    try:
        video = YouTube(url)
        
        stream = video.streams.get_highest_resolution()
        
        stream.download()
        
        print("Download complete!")
        
        transcript_list = YouTubeTranscriptApi.get_transcript(video.video_id)
        
        for transcript in transcript_list:
            print(transcript["text"])
            
    except Exception as e:
        print("An error occurred:", str(e))

video_url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"  # Replace with your YouTube video URL
download_video_with_subtitles(video_url)
