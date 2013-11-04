FFmpeg
======

1. detect volume:
    ffmpeg -i c.aud -filter:a volumedetect -f wav -y /dev/null
