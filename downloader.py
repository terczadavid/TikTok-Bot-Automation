import os
import subprocess
from datetime import datetime
import logging
from loguru import logger

def download_video():
    """
    Download video using yt-dlp.
    Prompts user for video URL and downloads it with yt-dlp.
    """
    try:
        print("\n=== Video Downloader ===")
        url = input("Please enter the video URL to download: ").strip()
        
        if not url:
            logger.error("URL cannot be empty")
            return
            
        # Create downloads directory if it doesn't exist
        downloads_dir = os.path.join(os.path.dirname(__file__), "downloads")
        os.makedirs(downloads_dir, exist_ok=True)
        
        # Generate output filename based on current timestamp
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_file = os.path.join(downloads_dir, f"video_{timestamp}.mp4")
        
        print(f"\nDownloading video from: {url}")
        print(f"Output file will be saved as: {output_file}")
        
        # Run yt-dlp command
        try:
            command = [
                "yt-dlp",
                url,
                "-o",
                output_file,
                "-f",
                "mp4"
            ]
            
            result = subprocess.run(
                command,
                capture_output=True,
                text=True,
                check=True
            )
            
            print("\nDownload completed successfully!")
            print(f"Video saved to: {output_file}")
            
        except subprocess.CalledProcessError as e:
            logger.error(f"Download failed: {e.stderr}")
            print(f"\nDownload failed! Error: {e.stderr}")
            
    except Exception as e:
        logger.error(f"Error in download process: {str(e)}")
        print(f"\nAn error occurred: {str(e)}")

if __name__ == "__main__":
    print("""
    ******************************************************
    Video Downloader
    
    This script helps you download videos using yt-dlp.
    Simply enter the video URL when prompted.

    Developed by: tercz

    ******************************************************
    """)
    download_video()