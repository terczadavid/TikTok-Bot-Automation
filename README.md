# TikTok Automation Bot

This project is a powerful **TikTok Automation Bot** that automates various tasks such as logging in, posting comments, following users, and uploading videos. It's designed to help streamline interaction with TikTok using Python and Selenium.

## Features
- **Automatic Login**: Uses cookies for faster login or manual login if cookies are unavailable.
- **Commenting**: Automatically posts a set number of comments on the user's latest TikTok video.
- **Following Users**: Follows a specified TikTok user.
- **Video Uploading**: Automates the upload of videos directly from your local storage to TikTok.

## Technologies Used
- **Python**: For the main logic and automation scripts.
- **Selenium**: For web automation.
- **SeleniumBase**: For enhanced Selenium capabilities.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/terczadavid/TikTok-Bot-Automation.git
   ```
2. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the bot:
   ```bash
   python main.py
   ```

## Usage
The TikTok Video Upload Bot automates video uploads to TikTok with support for:
- Video file upload
- Custom captions
- Hashtag support
- Environment variable configuration
- Automatic login with cookie persistence
- Detailed logging

### Environment Variables
The bot supports configuration through environment variables:
- `TIKTOK_EMAIL`: Your TikTok account email
- `TIKTOK_PASSWORD`: Your TikTok account password
- `VIDEO_PATH`: Path to the video file to upload (default: my_video.mp4 in script directory)
- `VIDEO_CAPTION`: Video caption text (default: "Check out this cool video!")
- `VIDEO_HASHTAGS`: Comma-separated list of hashtags (default: "tiktok,viral")

### Running the Bot
1. Set up environment variables:
```bash
# Create .env file
TIKTOK_EMAIL=your-email@example.com
TIKTOK_PASSWORD=your-password
VIDEO_PATH=/path/to/your/video.mp4
VIDEO_CAPTION="Your custom caption"
VIDEO_HASHTAGS="hashtag1,hashtag2,hashtag3"
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the bot:
```bash
python main.py
```

The bot will:
1. Log in to TikTok (using saved cookies if available)
2. Navigate to the upload page
3. Upload the specified video file
4. Add the caption and hashtags
5. Post the video

### Logging
The bot maintains detailed logs in `tiktok_uploader.log` with:
- Login attempts and status
- Video upload progress
- Error tracking and debugging information

### Error Handling
The bot includes robust error handling for:
- Invalid video files
- Login failures
- Network issues
- TikTok page loading delays
- Missing elements or DOM changes

### Tips for Success
1. Ensure your video file meets TikTok's requirements:
   - Maximum size: 1.5GB
   - Supported formats: MP4, MOV, AVI
   - Maximum duration: 3 minutes
2. Use relevant and popular hashtags
3. Keep captions concise (maximum 150 characters)
4. Allow sufficient time between uploads to avoid rate limiting

## Future Enhancements
- Add support for more social media platforms like Instagram and YouTube.
- Build a more dynamic system that can interact with multiple TikTok accounts simultaneously.
- Add multi-language support for users worldwide.

## **Level Up Your TikTok Presence: Beyond Basic Automation**

This TikTok Automation Bot is just the beginning. Imagine harnessing even more advanced capabilities to truly dominate the platform. If you're serious about scaling your TikTok influence, consider these powerful, TikTok-specific automation projects. Each offers a unique opportunity to **boost engagement, save time, and amplify your reach.**

### **Advanced TikTok Automation Projects: Unlock Unprecedented Growth**

-   **TikTok Auto DM Bot**: Develop a sophisticated bot that automatically sends **personalized direct messages (DMs)** based on user interactions (e.g., new followers, specific comments, or even keywords in their bio). 

-   **TikTok Mass DM & Campaign Bot**: Build a tool for **targeted mass direct messaging campaigns**. This bot would allow you to send customized messages to a predefined list of users, ideal for promotions, announcements, or outreach to potential collaborators. Integrate scheduling and message personalization for maximum impact.

-   **TikTok Live Stream Interaction Bot**: Create a bot that automatically interacts with **live streams**. This could involve sending automated comments during live broadcasts, answering frequently asked questions in real-time, or even participating in polls, driving engagement during critical live events.

-   **TikTok Content Curation & Reposting Bot**: Design a bot that identifies **trending content within specific niches**, automatically downloads videos (with proper attribution), and schedules them for reposting to maintain a dynamic content pipeline. Incorporate filters for quality and relevance to ensure your feed remains high-quality.

-   **TikTok Comment & Mention Sentiment Analysis Bot**: Build a bot that analyzes comments and mentions on your TikTok videos for **sentiment (positive, negative, neutral)**. This can help you quickly identify customer feedback, manage your brand reputation, and prioritize responses.

## **Ready to Automate Your TikTok Empire?**
