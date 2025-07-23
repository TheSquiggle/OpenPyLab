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

# Get video resolution
video_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
video_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Get terminal size
try:
    cols_terminal, rows_terminal = os.get_terminal_size()
except OSError:
    cols_terminal, rows_terminal = 120, 40  # fallback if can't detect

# Leave some margin for prompt and color codes
cols = min(video_width, cols_terminal - 4)
rows = min(video_height, rows_terminal - 4)

fps = cap.get(cv2.CAP_PROP_FPS)
if fps == 0:
    fps = 30  # fallback if FPS can't be detected

start_time = time.time()
frame_idx = 0

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    # Resize for terminal (auto-fits to terminal size)
    small = cv2.resize(frame, (cols, rows))
    # Clear terminal
    os.system('cls' if os.name == 'nt' else 'clear')
    for i in range(rows):
        line = ""
        for j in range(cols):
            b, g, r = small[i, j]
            line += f"\033[38;2;{r};{g};{b}m█"
        line += "\033[0m"
        print(line)
    frame_idx += 1
    target_time = frame_idx / fps
    sleep_time = start_time + target_time - time.time()
    if sleep_time > 0:
        time.sleep(sleep_time)
    else:
        time.sleep(1 / fps)  # fallback to normal frame rate if behind