# IMPORTANT: This script requires OpenCV and ffplay (from ffmpeg) to be installed.
import cv2
import os
import time
import threading

folder = os.path.dirname(__file__)
video_path = os.path.join(folder, "video.mp4")  # Looks in its own folder

# Function to play audio using ffplay (must have ffmpeg installed)
def play_audio(path):
    os.system(f'ffplay -nodisp -autoexit "{path}"')

# Start audio playback in a separate thread
audio_thread = threading.Thread(target=play_audio, args=(video_path,), daemon=True)
audio_thread.start()

cap = cv2.VideoCapture(video_path)
cols = 80  # Width of ASCII output
rows = 40  # Height of ASCII output

fps = cap.get(cv2.CAP_PROP_FPS)
if fps == 0:
    fps = 30  # fallback if FPS can't be detected

start_time = time.time()
frame_idx = 0

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
        print("".join(['#' if pixel == 0 else ' ' for pixel in row]))
    for row in bw:
        print("".join(['#' if pixel == 0 else ' ' for pixel in row]))
    frame_idx += 1
    target_time = frame_idx / fps
    sleep_time = start_time + target_time - time.time()
    if sleep_time > 0:
        time.sleep(sleep_time)
    else:
        time.sleep(1 / fps)  # fallback to normal frame rate if behind