from pytube import YouTube
from youtube_transcript_api import YouTubeTranscriptApi

# Function to download YouTube video in MP4 format
def download_video_with_subtitles(url):
    try:
        # Create a YouTube object
        video = YouTube(url)
        
        # Get the highest resolution progressive stream (MP4 format)
        stream = video.streams.get_highest_resolution()
        
        # Download the video
        stream.download()
        
        print("Download complete!")
        
        # Retrieve the transcript or subtitles
        transcript_list = YouTubeTranscriptApi.get_transcript(video.video_id)
        
        # Print the transcript
        for transcript in transcript_list:
            print(transcript["text"])
            
    except Exception as e:
        print("An error occurred:", str(e))

# Example usage
video_url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"  # Replace with your YouTube video URL
download_video_with_subtitles(video_url)
