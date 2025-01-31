import yt_dlp

def download_playlist(url, download_dir='downloads'):
    ydl_opts = {
        'format': 'best',
        'outtmpl': f'{download_dir}/%(title)s.%(ext)s',
    }
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

if __name__ == "__main__":
    playlist_url = input("Enter the YouTube Playlist URL: ")
    download_playlist(playlist_url)
