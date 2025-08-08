INPUT_DEVICE = "video=OBS Virtual Camera"
AUDIO_DEVICE = "audio=Microphone (Realtek(R) Audio)"
PRESET = "slow"

# ffmpeg -f dshow -i video="OBS Virtual Camera" -f dshow -i audio="Microphone (Realtek(R) Audio)" -map 0:v -map 1:a -vcodec libx264 -preset ultrafast -tune zerolatency -pix_fmt yuv420p -g 60 -keyint_min 60 -b:v 3000k -maxrate 3000k -bufsize 6000k -acodec aac -ar 44100 -b:a 128k -f tee "[f=flv]rtmp://a.rtmp.youtube.com/live2/xpzd-eu1m-yu7d-u3qs-4kkb|[f=flv]rtmps://live-api-s.facebook.com:443/rtmp/FB-1300984624926679-0-Ab1BZMQYnUqnp7L6JIvsds0i"


