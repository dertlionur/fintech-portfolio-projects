from pytube import YouTube

video_url = "https://youtube.com/shorts/V8DOOl4AG1M?si=UwsRrtUp2oQTgzu5"
yt = YouTube(video_url)

# En basit video akışını seç
stream = yt.streams.filter(progressive=True, file_extension='mp4').first()

# Videoyu indir
stream.download(output_path="Downloads")

print("Video başarıyla indirildi!")
