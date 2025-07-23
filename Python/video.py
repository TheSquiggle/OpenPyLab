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

# Auto-set cols and rows to video resolution
video_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)/10)
video_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)/10)
cols = video_width
rows = video_height

fps = cap.get(cv2.CAP_PROP_FPS)
if fps == 0:
    fps = 30  # fallback if FPS can't be detected

start_time = time.time()
frame_idx = 0

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    # Resize for terminal (now matches video resolution)
    small = cv2.resize(frame, (cols, rows))
    # Convert to grayscale and threshold for ASCII mask
    gray = cv2.cvtColor(small, cv2.COLOR_BGR2GRAY)
    _, bw = cv2.threshold(gray, 128, 255, cv2.THRESH_BINARY)
    # Clear terminal
    os.system('cls' if os.name == 'nt' else 'clear')
    for i, row in enumerate(bw):
        line = ""
        for j, pixel in enumerate(row):
            if pixel == 0:
                # Get color from original frame for black area
                b, g, r = small[i, j]
                line += f"\033[38;2;{r};{g};{b}m#"
            else:
                # Set foreground to white for white area
                line += "\033[38;2;255;255;255m#"
        line += "\033[0m"
        print(line)
    frame_idx += 1
    target_time = frame_idx / fps
    sleep_time = start_time + target_time - time.time()
    if sleep_time > 0:
        time.sleep(sleep_time)
    else:
        time.sleep(1 / fps)  # fallback to normal frame rate if behind