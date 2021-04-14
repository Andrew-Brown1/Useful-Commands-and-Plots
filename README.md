# Useful_Commands
A growing list of useful commands that I have Google'd to many times...

# FFMPEG 

- cropping a video, starting from top left corner (0,0)

*ffmpeg -i in.mp4 -filter:v "crop=out_w:out_h\:0:0" out.mp4*

# LaTeX

- order the references (e.g. [2,1,6] --> [1,2,6])

*\usepackage[numbers,sort]{natbib}*

# Command Line

- recursively count all files in directory 

*find . -type f | wc -l*

- quickly check size of directories in current directory

*for i in `ls ` ; do nice du -sh $i ; done*
