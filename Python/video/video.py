# IMPORTANT: This script requires OpenCV and ffplay (from ffmpeg) to be installed.
import cv2
import os
import time
import threading

# Use the user's Videos folder
from pathlib import Path
video_folder = str(Path.home() / "Videos")
video_files = [f for f in os.listdir(video_folder) if f.lower().endswith(('.mp4', '.avi', '.mov', '.mkv'))]

if not video_files:
    print("No video files found in your 'Videos' folder.")
    exit()

print("Select a video to play:")
for idx, fname in enumerate(video_files):
    print(f"{idx + 1}: {fname}")

choice = input("Enter the number of the video: ")
try:
    video_path = os.path.join(video_folder, video_files[int(choice) - 1])
except (IndexError, ValueError):
    print("Invalid selection.")
    exit()

def play_audio(path):
    os.system(f'ffplay -nodisp -autoexit "{path}"')

audio_thread = threading.Thread(target=play_audio, args=(video_path,), daemon=True)
audio_thread.start()

cap = cv2.VideoCapture(video_path)

video_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
video_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

try:
    cols_terminal, rows_terminal = os.get_terminal_size()
except OSError:
    cols_terminal, rows_terminal = 120, 40

cols = min(video_width, cols_terminal - 4)
rows = min(video_height, rows_terminal - 4)

fps = cap.get(cv2.CAP_PROP_FPS)
if fps == 0:
    fps = 30

start_time = time.time()
frame_idx = 0

render_chars = (
    " .'`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"
)  # 95 chars sorted by visual brightness (light to dark)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    small = cv2.resize(frame, (cols, rows))
    frame_str = ""
    for i in range(rows):
        line = ""
        for j in range(cols):
            b, g, r = small[i, j]
            brightness = 0.2126 * r + 0.7152 * g + 0.0722 * b
            char_idx = int(brightness / 256 * (len(render_chars) - 1))
            render_char = render_chars[char_idx]
            line += f"\033[38;2;{r};{g};{b}m{render_char}"
        line += "\033[0m\n"
        frame_str += line
    print(frame_str, end="")
    frame_idx += 1
    target_time = frame_idx / fps
    sleep_time = start_time + target_time - time.time()
    if sleep_time > 0:
        sleep_time = 0
        time.sleep(sleep_time)
