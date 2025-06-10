from flask import Flask, render_template, request, jsonify, send_file
import yt_dlp
import os
from urllib.parse import urlparse
import re

app = Flask(__name__)

# Create downloads directory if it doesn't exist
if not os.path.exists('downloads'):
    os.makedirs('downloads')

def sanitize_filename(filename):
    """Remove invalid characters from filename"""
    return re.sub(r'[<>:"/\\|?*]', '', filename)

def get_safe_filename(url, info):
    """Generate a safe filename for the video"""
    # Try to get title from info dict
    if info and 'title' in info:
        title = sanitize_filename(info['title'])
    else:
        # Fallback to URL parsing if no title
        parsed = urlparse(url)
        title = sanitize_filename(os.path.basename(parsed.path))
        if not title:
            title = 'video'
    
    return f"{title}.mp4"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/download', methods=['POST'])
def download_video():
    try:
        url = request.json.get('url')
        if not url:
            return jsonify({'error': 'URL is required'}), 400

        # Configure yt-dlp options
        ydl_opts = {
            'format': 'best',  # Download best quality
            'outtmpl': 'downloads/%(title)s.%(ext)s',
            'quiet': True,
            'no_warnings': True,
            # 'cookiefile': 'cookies.txt' # Commented out for Render.com deployment
        }

        # Get video info first
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            try:
                info = ydl.extract_info(url, download=False)
                filename = get_safe_filename(url, info)
                full_path = os.path.join('downloads', filename)
                
                # Download the video
                ydl_opts['outtmpl'] = full_path
                with yt_dlp.YoutubeDL(ydl_opts) as ydl_download:
                    ydl_download.download([url])
                
                return jsonify({
                    'success': True,
                    'message': 'Video downloaded successfully',
                    'filename': filename
                })
                
            except Exception as e:
                return jsonify({
                    'error': f'Download failed: {str(e)}'
                }), 500

    except Exception as e:
        return jsonify({
            'error': f'Server error: {str(e)}'
        }), 500

@app.route('/api/video/<filename>')
def serve_video(filename):
    try:
        return send_file(
            os.path.join('downloads', filename),
            as_attachment=True,
            download_name=filename
        )
    except Exception as e:
        return jsonify({
            'error': f'File not found: {str(e)}'
        }), 404

@app.route('/api/video-info', methods=['POST'])
def video_info():
    try:
        url = request.json.get('url')
        if not url:
            return jsonify({'error': 'URL is required'}), 400

        ydl_opts = {
            'quiet': True,
            'no_warnings': True,
            # 'cookiefile': 'cookies.txt' # Commented out for Render.com deployment
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            try:
                info = ydl.extract_info(url, download=False)
                title = info.get('title', 'Unknown Title')
                thumbnail = info.get('thumbnail', '')
                return jsonify({
                    'success': True,
                    'title': title,
                    'thumbnail': thumbnail
                })
            except Exception as e:
                return jsonify({
                    'error': f'Failed to fetch video info: {str(e)}'
                }), 500
    except Exception as e:
        return jsonify({
            'error': f'Server error: {str(e)}'
        }), 500

if __name__ == '__main__':
    # Use environment variable for port, which is required by Render.com
    port = int(os.environ.get('PORT', 5000))
    # Set debug=False for production and bind to 0.0.0.0
    app.run(host='0.0.0.0', port=port, debug=False)
