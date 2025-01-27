import time
import cv2
import numpy as np
from arducam import ArducamSDK

# Initialize the Arducam module
def initialize_camera():
    try:
        camera = ArducamSDK.open_camera()
        print("Camera initialized successfully!")
        return camera
    except Exception as e:
        print(f"Error initializing the camera: {e}")
        return None

# Capture a single image
def capture_image(camera):
    try:
        print("Capturing image...")
        frame = camera.capture()  # Captures a single frame
        if frame is None:
            print("Failed to capture image!")
            return None
        
        # Convert the image data into a format OpenCV can process
        image = np.frombuffer(frame.image, dtype=np.uint8)
        image = cv2.imdecode(image, cv2.IMREAD_COLOR)

        print("Image captured successfully!")
        return image
    except Exception as e:
        print(f"Error capturing image: {e}")
        return None

# Save the image to a file
def save_image(image, filename="output.jpg"):
    try:
        cv2.imwrite(filename, image)
        print(f"Image saved as {filename}")
    except Exception as e:
        print(f"Error saving image: {e}")

# Main function
if __name__ == "__main__":
    camera = initialize_camera()
    if not camera:
        exit()

    try:
        while True:
            # Capture an image and save it
            image = capture_image(camera)
            if image is not None:
                save_image(image)

            # Wait for 5 seconds before capturing the next image
            time.sleep(5)
    except KeyboardInterrupt:
        print("Exiting program.")
    finally:
        # Release the camera resources
        camera.close()
        print("Camera released.")
