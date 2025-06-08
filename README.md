# Video Downloader Website

![Python Version](https://img.shields.io/badge/python-3.9+-blue.svg)
![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![yt-dlp](https://img.shields.io/badge/yt--dlp-enabled-brightgreen)
![Gunicorn](https://img.shields.io/badge/Gunicorn-499848?style=for-the-badge&logo=gunicorn&logoColor=white)
![License](https://img.shields.io/badge/license-Unlicensed-blue.svg)

This website allows users to download videos from various supported URLs via a web interface.

## Features
- Web interface for pasting video URLs.
- Downloads videos using yt-dlp (supports YouTube, Facebook, Instagram, TikTok, and many more sites).
- Provides video information (title, thumbnail) before download.
- Allows users to download the video file directly.
- Uses Flask as the web framework and Gunicorn for deployment.

## Setup Instructions

1.  **Clone the repository (if applicable):**
    ```bash
    git clone <your-repository-url>
    cd <repository-directory>
    ```

2.  **Create and activate a virtual environment (recommended):**
    ```bash
    python -m venv venv
    # On Windows
    venv\Scripts\activate
    # On macOS/Linux
    source venv/bin/activate
    ```

3.  **Install the required dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Prepare `cookies.txt` (Optional but Recommended for some sites):**
    - For sites that require login or to bypass bot detection (like YouTube sometimes), you'll need to provide a `cookies.txt` file in the Netscape format.
    - Place this file in the root directory of the project.
    - See yt-dlp documentation for how to export cookies:
        - [How to pass cookies to yt-dlp](https://github.com/yt-dlp/yt-dlp/wiki/FAQ#how-do-i-pass-cookies-to-yt-dlp)
        - [Exporting YouTube cookies](https://github.com/yt-dlp/yt-dlp/wiki/Extractors#exporting-youtube-cookies)

5.  **Run the development server:**
    ```bash
    python app.py
    ```
    The application will be accessible at `http://localhost:5002` by default.

6.  **Run with Gunicorn (for production-like environment):**
    ```bash
    gunicorn --bind 0.0.0.0:5002 app:app
    ```

## Usage

1.  Open your web browser and navigate to `http://localhost:5002` (or the address where it's hosted).
2.  Paste the video URL into the input field.
3.  Click the "Get Info" or "Download" button.
4.  The website will:
    - Fetch video information (title, thumbnail).
    - Download the video to the server's `downloads` directory.
    - Provide a link to download the video file.

## Supported Sites

This website supports all sites that yt-dlp can handle, including:
- YouTube
- Facebook
- Instagram
- TikTok
- Twitter
- Vimeo
- And many more!

## Notes

- Ensure the `downloads` directory exists or the application has permission to create it.
- For some sites, a valid `cookies.txt` file is crucial for successful downloads.
- Ensure enough storage space on the server for temporary video downloads.
