import cv2
# Open the video file
video_capture = cv2.VideoCapture('nature.mp4')
# Check if the video file was opened successfully
if not video_capture.isOpened():
    print("Error: Could not open video file.")
    exit()
# Create a directory to save the frames (if it doesn't exist)
import os
if not os.path.exists('frames'):
    os.makedirs('frames')

# Initialize variables
frame_count = 0
while True:
    # Read a frame from the video
    ret, frame = video_capture.read()
    # Break the loop if we have reached the end of the video
    if not ret:
        break
    # Save the frame as an image
    frame_filename = f'frames/frame_{frame_count:04d}.jpg'
    cv2.imwrite(frame_filename, frame)
    frame_count += 1
# Release the video capture object
video_capture.release()
print(f"Frames extracted: {frame_count}")
