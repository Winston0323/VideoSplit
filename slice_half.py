import os
from moviepy.editor import VideoFileClip, vfx

# Define the path to the directory with the videos
video_directory = "./Chimp"
left_result_directory = video_directory + "/left"
right_result_directory = video_directory + "/right"
if not os.path.exists(left_result_directory):
    os.makedirs(left_result_directory)
if not os.path.exists(right_result_directory):
    os.makedirs(right_result_directory)
# Iterate over all files in the directory
for filename in os.listdir(video_directory):
    if filename.endswith(('.mp4', '.mov', '.avi')):  # Add any other video formats you need to handle
        # Construct the full file path
        video_path = os.path.join(video_directory, filename)
        
        # Load the video file
        clip = VideoFileClip(video_path)
        
        # Get the width and height of the video
        width, height = clip.size
        
        # Crop the video into two halves
        left_clip = clip.fx(vfx.crop, x1=0, y1=0, x2=width/2, y2=height)
        right_clip = clip.fx(vfx.crop, x1=width/2, y1=0, x2=width, y2=height)
        
        # Define the output file paths
        base, ext = os.path.splitext(filename)
        left_filename = os.path.join(left_result_directory, f"{base}_left{ext}")
        right_filename = os.path.join(right_result_directory, f"{base}_right{ext}")
        
        # Write the output video files
        left_clip.write_videofile(left_filename, codec='libx264', audio_codec='aac')
        right_clip.write_videofile(right_filename, codec='libx264', audio_codec='aac')

        # Close the clips to free up system resources
        clip.close()
        left_clip.close()
        right_clip.close()
        
print("Processing completed.")