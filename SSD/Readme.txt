Keep these steps for smooth running the main file

1-Download all the necessary files from 2 folders (configure and videos resource)
2-Place a number right after hit the run button on IDE. 
    No 1: video link to workplace1.mp4.
    No 2: video link to workplace2.mp4.
    *They are bicycle tracking moments
3-If using real-time camera: 
    3.1. Hide the input command
    3.2. Set the camera path in line 6
    
4-If there is any detected object in frame, the title will show the name from identification list. If not, the notification will be displayed as 'Not Detect' in red.
5-All more video source:
    Prefer the low resolution videos, recommend 360p to 720p
    Adjust the input line and folder (if any)
6-Parameters modification:
    For better recognition: 
      +Increase setInputSize: the bigger size, the better model recognition, but the lower system pulse
      +Increase confThresold (approaching to 1.0), the higher number, the harder model recognition, but they are more confidence.
    For visualization: Fonts, Scale factors, thickness (as you want)
    ----------------------------------------------------------------
