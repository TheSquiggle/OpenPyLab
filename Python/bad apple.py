# IMPORTANT: This script requires OpenCV to be installed.
import cv2
import os
import time

folder = os.path.dirname(__file__)
video_path = os.path.join(folder, "vid1.mp4")  # Looks in its own folder

cap = cv2.VideoCapture(video_path)
cols = 80  # Width of ASCII output
rows = 40  # Height of ASCII output

fps = cap.get(cv2.CAP_PROP_FPS)
if fps == 0:
    fps = 30  # fallback if FPS can't be detected

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    # Convert to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Resize for terminal
    small = cv2.resize(gray, (cols, rows))
    # Threshold to 2 colors
    _, bw = cv2.threshold(small, 128, 255, cv2.THRESH_BINARY)
    # Convert to ASCII
    os.system('cls' if os.name == 'nt' else 'clear')
    for row in bw:
        print("".join(['⬜' if pixel == 0 else ' ' for pixel in row]))
    time.sleep(1 / fps)  # Auto-adjust