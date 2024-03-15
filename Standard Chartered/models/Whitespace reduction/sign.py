from PIL import Image

def crop_image(image_path, output_path):
    # Open the image
    image = Image.open(image_path)
    width, height = image.size
    
    # Convert the image to grayscale
    grayscale_image = image.convert('L')
    
    # Initialize bounding box coordinates
    left = width
    top = height
    right = 0
    bottom = 0
    
    # Define a threshold value for darkness
    threshold = 100  # Adjust this value as needed
    
    # Scan the image to find the bounding box for all sides
    for y in range(height):
        for x in range(width):
            pixel = grayscale_image.getpixel((x, y))
            if pixel < threshold:  # Check if pixel is darker than the threshold
                left = min(left, x)
                top = min(top, y)
                right = max(right, x)
                bottom = max(bottom, y)
    
    # Crop the image using the bounding box
    cropped_image = image.crop((left, top, right + 1, bottom + 1))  # Increment right and bottom by 1
    
    # Save the cropped image
    cropped_image.save(output_path)
    print("Cropped image saved successfully!")

# Example usage:
if __name__ == "__main__":
    # Path to input signature image
    input_image_path = 'C:/Users/bhava/OneDrive/Desktop/sign.jpg'
    
    # Path to output cropped image
    output_image_path = 'cropped_signature.png'
    
    # Crop the image
    crop_image(input_image_path, output_image_path)
