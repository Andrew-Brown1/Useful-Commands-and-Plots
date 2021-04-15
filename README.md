# Useful_Commands
A growing list of useful commands that I have Google'd too many times...

- /plots contains scripts for specific python plots

# FFMPEG 

- cropping a video, starting from top left corner (0,0)

*ffmpeg -i in.mp4 -filter:v "crop=out_w:out_h\:0:0" out.mp4*

- convert MKV file to MP4

*ffmpeg -i in.mkv -c copy -c:a aac out.mp4*

- cut an mp4 of length "duration" starting from time "start" (seconds)

*ffmpeg -i in.mp4 -ss start -t duration -async 1 out.mp4*

# LaTeX

- order the references (e.g. [2,1,6] --> [1,2,6])

*\usepackage[numbers,sort]{natbib}*

# Command Line

- recursively count all files in directory 

*find . -type f | wc -l*

- quickly check size of directories in current directory

*for i in `ls ` ; do nice du -sh $i ; done*

- untar a tar.gz into current directory

*tar -xzvf file.tar.gz*
