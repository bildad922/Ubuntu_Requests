import os
import requests
from urllib.parse import urlparse
from pathlib import Path

def fetch_image():
    """
    Ubuntu-Inspired Image Fetcher
    Prompts user for an image URL, creates a directory for fetched images,
    and downloads the image with proper error handling.
    """
    print("=" * 50)
    print("Ubuntu-Inspired Image Fetcher")
    print("=" * 50)
    print("In the spirit of Ubuntu: 'I am because we are'")
    print("This tool helps you respectfully fetch and organize images from the web community")
    print("=" * 50)
    
    # Prompt user for URL
    url = input("Please enter the URL of the image you wish to fetch: ").strip()
    
    if not url:
        print("No URL provided. Exiting.")
        return
    
    # Create directory for fetched images
    try:
        os.makedirs("Fetched_Images", exist_ok=True)
        print("✓ Fetched_Images directory ready")
    except OSError as e:
        print(f"✗ Error creating directory: {e}")
        return
    
    # Extract filename from URL or generate one
    try:
        parsed_url = urlparse(url)
        path = Path(parsed_url.path)
        filename = path.name
        
        if not filename:
            # If we can't extract a filename, generate one
            filename = f"downloaded_image_{int(time.time())}.jpg"
        
        filepath = os.path.join("Fetched_Images", filename)
        
        # Check if file already exists
        if os.path.exists(filepath):
            print(f"Note: {filename} already exists. It will be overwritten.")
    except Exception as e:
        print(f"✗ Error processing filename: {e}")
        return
    
    # Fetch the image
    print(f"Fetching image from {url}...")
    try:
        headers = {
            'User-Agent': 'UbuntuImageFetcher/1.0 (https://example.com/ubuntu-fetcher)'
        }
        response = requests.get(url, headers=headers, timeout=30)
        response.raise_for_status()  # Raise exception for HTTP errors
        
        # Check if content is an image
        content_type = response.headers.get('content-type', '')
        if 'image' not in content_type:
            print("Warning: The URL does not appear to point to an image file.")
            proceed = input("Do you want to continue anyway? (y/N): ").lower()
            if proceed != 'y':
                print("Download cancelled.")
                return
        
        # Save the image
        with open(filepath, 'wb') as f:
            f.write(response.content)
        
        print(f"✓ Successfully downloaded: {filename}")
        print(f"✓ Image saved to: {os.path.abspath(filepath)}")
        print("Thank you for using the Ubuntu-Inspired Image Fetcher!")
        
    except requests.exceptions.RequestException as e:
        print(f"✗ Error fetching the image: {e}")
    except Exception as e:
        print(f"✗ An unexpected error occurred: {e}")

if __name__ == "__main__":
    import time
    fetch_image()