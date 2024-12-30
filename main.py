import nltk
from nltk.corpus import stopwords
from nltk.probability import FreqDist
import string
from moviepy.editor import ImageSequenceClip, ImageClip
import moviepy
from PIL import Image, ImageDraw, ImageFont  # For generating images from text
import os
from PIL import Image, ImageDraw, ImageFont


print(moviepy.__version__)
from moviepy.editor import ImageSequenceClip
from moviepy.video.io.ImageSequenceClip import ImageSequenceClip

# Download necessary resources
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('punkt_tab')  # Adding this explicitly

# Ensure required NLTK resources are downloaded
nltk.download('punkt')
nltk.download('stopwords')

# Function to generate hashtags from content
def generate_hashtags(content):
    # Tokenize the content into words
    words = nltk.word_tokenize(content.lower())  # Convert to lowercase to standardize
    # Remove punctuation and stopwords
    stop_words = set(stopwords.words('english'))  # Common words to exclude
    words = [word for word in words if word not in stop_words and word not in string.punctuation]

    # Frequency distribution of words
    freq_dist = FreqDist(words)

    # Extract the top 5 most common words
    top_words = [word for word, freq in freq_dist.most_common(5)]

    # Convert words to hashtags
    hashtags = ['#' + word for word in top_words]
    return hashtags

# Function to remove characters from video (placeholder)
def remove_characters_from_video(input_video, output_video):
    print(f"Removing characters from video: {input_video}")
    # Add your video processing code here
    print(f"Character removal completed! Output saved to: {output_video}")

# Function to resize images to match the size of the first image in the list
def resize_images(images):
    from moviepy.editor import ImageClip
    
    # Get the size of the first image in the list
    first_image = ImageClip(images[0])
    first_image_size = first_image.size
    
    resized_images = []
    
    # Resize all images to the size of the first image
    for image in images:
        img_clip = ImageClip(image)
        img_clip = img_clip.resize(height=first_image_size[1])  # Resize keeping the aspect ratio
        resized_images.append(img_clip)
        
    return resized_images

# Function to create images from text (for video generation)
#from PIL import Image, ImageDraw, ImageFont

def create_image_from_text(text, image_path, width=640, height=480):
    """Generate an image from a text prompt."""
    img = Image.new('RGB', (width, height), color = (255, 255, 255))  # White background
    draw = ImageDraw.Draw(img)
    font = ImageFont.load_default()  # You can choose a font if desired
    
    # Calculate the bounding box of the text
    text_bbox = draw.textbbox((0, 0), text, font=font)
    text_width = text_bbox[2] - text_bbox[0]  # width = right - left
    text_height = text_bbox[3] - text_bbox[1]  # height = bottom - top
    
    # Position the text in the center of the image
    position = ((width - text_width) // 2, (height - text_height) // 2)
    
    draw.text(position, text, fill=(0, 0, 0), font=font)  # Black text
    img.save(image_path)


# Function to generate a video from text-based images
# Function to generate a video from text
from PIL import Image
from moviepy.editor import ImageSequenceClip
import os

# Function to generate a video from text
def generate_video_from_text():
    text_prompt = input("Enter the prompt for creating the video: ")
    
    # Create images based on the text prompt (you need to implement this part for creating images)
    # For now, we are assuming you are generating images and saving them in a folder
    images_folder = "/home/sourabh/GenAI_Task/images_folder"
    
    # Let's assume you have generated images, now create the video
    # Gather all images from the folder
    images = [os.path.join(images_folder, img) for img in sorted(os.listdir(images_folder)) if img.endswith('.jpg') or img.endswith('.png')]

    if len(images) == 0:
        print("No images found in the specified folder.")
        return
    
    # Resize images to the same size
    resized_images = []
    target_size = (640, 480)  # You can set this to any size you want (e.g., 640x480)

    for image_path in images:
        # Open the image and resize it
        img = Image.open(image_path)
        img_resized = img.resize(target_size)  # Resize to target size
        resized_image_path = image_path.replace(images_folder, images_folder + "_resized")  # Save resized images in a new folder
        os.makedirs(os.path.dirname(resized_image_path), exist_ok=True)
        img_resized.save(resized_image_path)  # Save the resized image
        resized_images.append(resized_image_path)  # Add the resized image path to the list

    # Prompt for the output video file name and path
    output_video = input("Enter the path where you want to save the generated video (including filename, e.g., /path/to/video.mp4): ")
    
    # Make sure you provide a filename like 'output_video.mp4'
    if not output_video.endswith(".mp4"):
        output_video += ".mp4"  # Ensure the file has a .mp4 extension
    
    # Create the video clip
    video_clip = ImageSequenceClip(resized_images, fps=24)
    
    # Save the video to the specified path
    video_clip.write_videofile(output_video, codec='libx264')
    
    print(f"Video generated and saved to {output_video}")


# Main function to interact with user and process video or text
def main():
    print("Choose an option:")
    print("1. Remove characters from video")
    print("2. Generate a video")
    print("3. Generate content")
    print("4. Generate hashtags")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        input_video = input("Enter input video path: ")
        output_video = input("Enter output video path: ")
        # Call character removal logic here
        remove_characters_from_video(input_video, output_video)

    elif choice == 2:
        # Video generation from text prompt
        generate_video_from_text()

    elif choice == 3:
        prompt = input("Enter the prompt for content generation: ")
        # Content generation logic here (simple example)
        print("Generated Content:")
        print("This is a sample content based on the prompt:", prompt)

    elif choice == 4:
        content = input("Enter content for hashtag generation: ")
        hashtags = generate_hashtags(content)
        print("\nGenerated Hashtags:")
        print(" ".join(hashtags))

    else:
        print("Option not implemented yet.")

if __name__ == "__main__":
    main()
