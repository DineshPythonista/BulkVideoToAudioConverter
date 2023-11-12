from moviepy.editor import VideoFileClip
import os

def convert_videos_to_audio(input_folder, output_folder):
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # List all video files in the input folder
    video_files = [f for f in os.listdir(input_folder) if f.endswith(('.mp4', '.avi', '.mkv'))]

    for video_file in video_files:
        video_path = os.path.join(input_folder, video_file)
        output_audio_path = os.path.join(output_folder, os.path.splitext(video_file)[0] + ".mp3")

        # Convert video to audio
        video_clip = VideoFileClip(video_path)
        audio_clip = video_clip.audio
        audio_clip.write_audiofile(output_audio_path)

        # Close the clips to free up resources
        audio_clip.close()
        video_clip.close()

if __name__ == "__main__":
    input_folder = "/Users/dinesh/Desktop/videos"
    output_folder = "/Users/dinesh/Desktop/audio"

    convert_videos_to_audio(input_folder, output_folder)
