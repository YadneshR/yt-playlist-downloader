from flask import Flask, request, jsonify
import yt_dlp
import os

app = Flask(__name__)

@app.route('/download', methods=['POST'])
def download_playlist():
    data = request.get_json()
    playlist_url = data.get('url')
    if not playlist_url:
        return jsonify({"message": "No URL provided!"}), 400

    download_dir = 'YouTube_Playlist'
    os.makedirs(download_dir, exist_ok=True)

    ydl_opts = {
        'format': 'best',
        'outtmpl': os.path.join(download_dir, '%(title)s.%(ext)s'),
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([playlist_url])

        return jsonify({"message": "Playlist downloaded successfully!"})
    except Exception as e:
        return jsonify({"message": f"Error: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(debug=True)
