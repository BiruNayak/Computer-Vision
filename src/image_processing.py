import cv2 as cv
import os

# Function to load an image
def load_image(path):
    image = cv.imread(path)
    if image is None:
        raise FileNotFoundError(f"Image not found at: {path}")
    return image

# Function to convert to grayscale
def convert_to_grayscale(image):
    return cv.cvtColor(image, cv.COLOR_BGR2GRAY)

# Function to apply Gaussian blur
def apply_gaussian_blur(image, kernel_size=(5, 5), sigma=0):
    return cv.GaussianBlur(image, kernel_size, sigma)

# Function to apply Canny edge detection
def apply_canny_edge_detection(image, threshold1=100, threshold2=200):
    return cv.Canny(image, threshold1, threshold2)

# Function to save image to file
def save_image(image, filename):
    cv.imwrite(filename, image)
    print(f"Saved: {filename}")

# Function to process a single image and save outputs
def process_image_file(input_path, output_dir):
    filename = os.path.splitext(os.path.basename(input_path))[0]
    image = load_image(input_path)

    # Process steps
    gray = convert_to_grayscale(image)
    blurred = apply_gaussian_blur(gray)
    edges = apply_canny_edge_detection(blurred)

    # Save outputs
    save_image(gray, os.path.join(output_dir, f"{filename}_grayscale.jpg"))
    save_image(blurred, os.path.join(output_dir, f"{filename}_blur.jpg"))
    save_image(edges, os.path.join(output_dir, f"{filename}_edges.jpg"))

# Main function to process all images in a folder
def process_folder(folder_path, output_dir=None):
    if output_dir is None:
        output_dir = folder_path  # Save in same folder if not specified
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Supported image formats
    valid_extensions = ('.jpg', '.jpeg', '.png', '.bmp')

    for file in os.listdir(folder_path):
        if file.lower().endswith(valid_extensions):
            full_path = os.path.join(folder_path, file)
            try:
                process_image_file(full_path, output_dir)
            except Exception as e:
                print(f"Error processing {file}: {e}")

# Entry point
if __name__ == "__main__":
    input_folder = "../Dataset/Images"  
    output_folder = "../Outputs"  
    process_folder(input_folder, output_folder)
