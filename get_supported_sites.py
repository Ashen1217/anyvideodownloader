import json
import subprocess
from typing import List, Dict

def get_supported_sites() -> List[str]:
    """Get list of all supported sites by yt-dlp"""
    try:
        # Run yt-dlp --list-extractors command using python -m
        result = subprocess.run(['python', '-m', 'yt_dlp', '--list-extractors'], 
                              capture_output=True, 
                              text=True)
        
        # Split output into lines and remove empty lines
        sites = [line.strip() for line in result.stdout.split('\n') if line.strip()]
        return sites
    except Exception as e:
        print(f"Error: {str(e)}")
        return []

def create_site_guide() -> Dict:
    """Create a guide with examples for popular sites"""
    guide = {
        "YouTube": {
            "description": "Download videos from YouTube",
            "examples": [
                {
                    "command": "yt-dlp https://www.youtube.com/watch?v=VIDEO_ID",
                    "description": "Download a single video"
                },
                {
                    "command": "yt-dlp -f 'bv*[height=1080]+ba' https://www.youtube.com/watch?v=VIDEO_ID",
                    "description": "Download 1080p video with best audio"
                },
                {
                    "command": "yt-dlp --playlist-items 1-3 https://www.youtube.com/playlist?list=PLAYLIST_ID",
                    "description": "Download first 3 videos from a playlist"
                }
            ]
        },
        "Facebook": {
            "description": "Download videos from Facebook",
            "examples": [
                {
                    "command": "yt-dlp https://www.facebook.com/video_url",
                    "description": "Download Facebook video"
                }
            ]
        },
        "Instagram": {
            "description": "Download posts, stories, and reels from Instagram",
            "examples": [
                {
                    "command": "yt-dlp https://www.instagram.com/p/POST_ID/",
                    "description": "Download Instagram post"
                },
                {
                    "command": "yt-dlp https://www.instagram.com/stories/username",
                    "description": "Download Instagram story"
                }
            ]
        },
        "TikTok": {
            "description": "Download videos from TikTok",
            "examples": [
                {
                    "command": "yt-dlp https://www.tiktok.com/@username/video/VIDEO_ID",
                    "description": "Download TikTok video"
                }
            ]
        }
    }
    return guide

def main():
    # Get all supported sites
    print("Fetching supported sites...")
    sites = get_supported_sites()
    
    if not sites:
        return
    
    # Create guide
    guide = create_site_guide()
    
    # Save to JSON
    data = {
        "supported_sites": sites,
        "usage_guide": guide
    }
    
    with open('yt_dlp_sites.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print("Created yt_dlp_sites.json")
    
    # Save to TXT
    with open('yt_dlp_sites.txt', 'w', encoding='utf-8') as f:
        f.write("YT-DLP SUPPORTED SITES AND USAGE GUIDE\n")
        f.write("=" * 40 + "\n\n")
        
        f.write("SUPPORTED SITES:\n")
        f.write("-" * 15 + "\n")
        for site in sites:
            f.write(f"- {site}\n")
        
        f.write("\n\nUSAGE GUIDE:\n")
        f.write("-" * 11 + "\n")
        for site, info in guide.items():
            f.write(f"\n{site}:\n")
            f.write(f"Description: {info['description']}\n")
            f.write("Examples:\n")
            for example in info['examples']:
                f.write(f"- {example['description']}:\n")
                f.write(f"  {example['command']}\n")
    print("Created yt_dlp_sites.txt")

if __name__ == "__main__":
    main()
