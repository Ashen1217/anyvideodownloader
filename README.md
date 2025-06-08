# Telegram Video Downloader Userbot

![Python Version](https://img.shields.io/badge/python-3.9+-blue.svg)
![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![yt-dlp](https://img.shields.io/badge/yt--dlp-enabled-brightgreen)
![Gunicorn](https://img.shields.io/badge/Gunicorn-499848?style=for-the-badge&logo=gunicorn&logoColor=white)
![License](https://img.shields.io/badge/license-Unlicensed-blue.svg)

This userbot automatically downloads videos from supported URLs and uploads them to a specified Telegram group.

## Features
- Automatically detects video URLs in messages
- Downloads videos using yt-dlp (supports YouTube, Facebook, Instagram, TikTok, and many more sites)
- Uploads videos to a specified Telegram group
- Automatically deletes downloaded videos after upload
- Shows download and upload status updates

## Setup Instructions

1. Install the required dependencies:
```bash
pip install -r requirements.txt
```

2. Get your Telegram API credentials:
   - Go to https://my.telegram.org/
   - Log in with your phone number
   - Click on "API Development tools"
   - Create a new application
   - Copy the `api_id` and `api_hash`

3. Configure the userbot:
   - Open `userbot.py`
   - Replace `YOUR_API_ID` with your API ID
   - Replace `YOUR_API_HASH` with your API Hash
   - Replace `TARGET_GROUP_ID` with your target group ID (where videos will be uploaded)

4. Get your target group ID:
   - Forward any message from your target group to @userinfobot
   - The bot will reply with group information including the ID
   - Use the negative number as your group ID (e.g., -1001234567890)

5. Run the userbot:
```bash
python userbot.py
```

6. On first run:
   - You'll be prompted to enter your phone number
   - Enter the verification code sent to your Telegram
   - The userbot will create a session file

## Usage

1. Simply send a video URL to any chat where the userbot account is present
2. The userbot will:
   - Download the video
   - Upload it to the specified group
   - Delete the downloaded file
   - Show status updates

## Supported Sites

The userbot supports all sites that yt-dlp can handle, including:
- YouTube
- Facebook
- Instagram
- TikTok
- Twitter
- Vimeo
- And many more!

## Notes

- Keep your API credentials private
- Don't share your session file
- The userbot must be a member of the target group
- Ensure enough storage space for temporary video downloads
