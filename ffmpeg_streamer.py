# ffmpeg_streamer.py
import subprocess
from config import AUDIO_DEVICE, INPUT_DEVICE, PRESET

def build_ffmpeg_command(platform_info):
    output = []
    for platform in platform_info:
        platform_url = platform_info[platform]["url"]
        streamkey = platform_info[platform]["streamkey"]
        s = f"[f=flv]{platform_url}/{streamkey}"
        output.append(s)
    final_string = "|".join(output)
    return [
        "ffmpeg",
        "-f", "dshow",
        "-i", INPUT_DEVICE,
        "-f", "dshow",
        "-i", AUDIO_DEVICE,
        "-map",
        "0:v",
        "-map",  "1:a",
        "-vcodec", "libx264",
        "-preset", PRESET,
        "-tune", "fastdecode",
        "-pix_fmt", "yuv422p",
        "-g",  "120", "-keyint_min", "30","-b:v", "2500k",
        "-maxrate", "2500k", "-bufsize" , "5000k", "-acodec", "aac", "-ar", "44100", "-b:a", "192k",
        "-f", "tee",
        final_string
    ]

def launch_stream(platform_info):
    cmd = build_ffmpeg_command(platform_info)
    print("Launching FFmpeg with command:")
    print(" ".join(cmd))
    try:
        process = subprocess.Popen(cmd)
        process.wait()
    except KeyboardInterrupt:
        print("Interrupted. Terminating stream.")
        process.terminate()