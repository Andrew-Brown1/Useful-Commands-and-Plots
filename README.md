# Useful_Commands
A growing list of useful commands that I have Google'd to many times...

# FFMPEG 

- cropping a video, starting from top left corner (0,0)

*ffmpeg -i in.mp4 -filter:v "crop=out_w:out_h\:0:0" out.mp4*
