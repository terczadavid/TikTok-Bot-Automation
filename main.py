import time
import os
import logging
from pathlib import Path
from seleniumbase import Driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from dotenv import load_dotenv
import loguru

# Setup logging
logger = loguru.logger
logger.add("tiktok_uploader.log", rotation="500 MB", retention="7 days")

# Load environment variables
load_dotenv()

# Initialize driver
try:
    driver = Driver(uc=True)
    driver.maximize_window()
except Exception as e:
    logger.error(f"Failed to initialize driver: {str(e)}")
    raise

def login(email, password):
    """
    Login to TikTok using email and password.
    Args:
        email (str): TikTok account email
        password (str): TikTok account password
    """
    try:
        driver.get("https://www.tiktok.com/login")
        time.sleep(5)
        
        # Try to use cookies if available
        try:
            from social_media import tiktok
            cookies = tiktok.load_cookies('tiktok_cookies.txt')
            tiktok.login(driver, email, password, cookies)
            logger.info("Successfully logged in using cookies")
        except Exception as e:
            logger.warning(f"Cookie login failed: {str(e)}")
            # Fallback to manual login
            email_input = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.NAME, "email"))
            )
            email_input.send_keys(email)
            
            password_input = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.NAME, "password"))
            )
            password_input.send_keys(password)
            
            login_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Log in')]"))
            )
            login_button.click()
            
            # Wait for login to complete
            WebDriverWait(driver, 30).until(
                EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'user-info')]"))
            )
            logger.info("Successfully logged in manually")
            
            # Save cookies for future use
            tiktok.save_cookies(driver, 'tiktok_cookies.txt')
            logger.info("Saved login cookies for future use")
        
        time.sleep(3)
    except Exception as e:
        logger.error(f"Login failed: {str(e)}")
        raise

def upload_video(video_path, caption, hashtags=[]):
    """
    Upload a video to TikTok.
    Args:
        video_path (str): Path to the video file
        caption (str): Video caption
        hashtags (list): List of hashtags to add
    """
    try:
        # Validate video file
        video_path = Path(video_path)
        if not video_path.exists():
            logger.error(f"Video file not found: {video_path}")
            raise FileNotFoundError(f"Video file not found: {video_path}")
            
        # Navigate to upload page
        driver.get('https://www.tiktok.com/tiktokstudio/upload')
        
        # Wait for upload page to load
        WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.XPATH, "//input[@type='file']"))
        )
        
        # Upload video
        file_input = driver.find_element(By.XPATH, "//input[@type='file']")
        file_input.send_keys(str(video_path))
        logger.info(f"Video file uploaded: {video_path}")
        
        # Wait for video processing
        WebDriverWait(driver, 60).until(
            EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'video-preview')]"))
        )
        
        # Add caption
        caption_area = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//div[contains(@class,'public-DraftStyleDefault-block')]"))
        )
        caption_area.click()
        
        # Format caption with hashtags
        formatted_caption = caption
        if hashtags:
            formatted_caption += " " + " ".join([f"#{tag}" for tag in hashtags])
        
        ActionChains(driver).send_keys(formatted_caption).perform()
        logger.info(f"Caption added: {formatted_caption}")
        
        # Wait for caption to be processed
        time.sleep(3)
        
        # Check if additional fields are present and fill them
        try:
            # Add location if available
            location_button = driver.find_element(By.XPATH, "//button[contains(@aria-label, 'Location')]")
            location_button.click()
            time.sleep(2)
        except NoSuchElementException:
            logger.info("Location button not found, skipping")
        
        # Scroll to post button
        driver.execute_script("window.scrollBy(0, 200);")
        time.sleep(2)
        
        # Post the video
        post_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Post')]"))
        )
        post_button.click()
        
        # Wait for post confirmation
        WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.XPATH, "//div[contains(text(), 'Your video has been posted')]"))
        )
        logger.info("Video posted successfully")
        
        # Wait for upload to complete
        time.sleep(15)
        
    except Exception as e:
        logger.error(f"Failed to upload video: {str(e)}")
        raise

def run_bot():
    """
    Main bot execution function.
    Reads credentials from environment variables or prompts user.
    """
    try:
        # Get credentials from environment variables or prompt
        email = os.getenv('TIKTOK_EMAIL')
        password = os.getenv('TIKTOK_PASSWORD')
        
        if not email or not password:
            email = input("Please enter your TikTok email: ")
            password = input("Please enter your TikTok password: ")
        
        # Login
        login(email, password)
        
        # Get video path from environment variable or use default
        video_path = os.getenv('VIDEO_PATH', os.path.join(os.path.dirname(__file__)))
        
        # Get caption from environment variable or use default
        caption = os.getenv('VIDEO_CAPTION')
        
        # Get hashtags from environment variable (comma-separated)
        hashtags = os.getenv('VIDEO_HASHTAGS').split(',')
        
        try:
            upload_video(video_path, caption, hashtags)
            logger.info("Video upload completed successfully")
        except Exception as e:
            logger.error(f"Video upload failed: {str(e)}")
            raise
        
        print("Bot execution finished.")
        time.sleep(10)
    except Exception as e:
        logger.error(f"Bot execution failed: {str(e)}")
        raise

if __name__ == "__main__":
    print("""
    ******************************************************
    Welcome to the TikTok Automation Bot Project!
    
    Developed by: tercz
    
    ******************************************************
    """)
    run_bot()