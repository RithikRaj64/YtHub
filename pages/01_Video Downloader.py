import streamlit as st
from pytube import YouTube
import os

st.set_page_config(
    page_title="YtHub | Video Downloader",
    layout="centered",
    page_icon="🎥",
    initial_sidebar_state="auto",
)


def download_custom_resolution(
    link: str, custom_resolution: str | None, path: str | None
) -> None:
    yt = YouTube(link)

    # Define the desired resolution (e.g., '720p', '1080p')
    desired_resolution = custom_resolution

    if not desired_resolution:
        st.error("Please select a resolution from the dropdown.")
        return

    # Filter streams to find the one with the custom resolution
    video_stream = yt.streams.filter(progressive=True, file_extension="mp4", res=desired_resolution).first()  # type: ignore

    # Automatically get the path of windows downloads folder using os
    # This is where the video will be saved
    # You can change this path to your desired location
    # e.g., path = "C:/Users/MyUser/Downloads"
    if not path:
        path = os.path.join(os.path.expanduser("~"), "Downloads")

    if video_stream:
        video_stream.download(path)
        st.success(f"Downloaded the video in {desired_resolution} resolution.")
    else:
        st.error(
            f"Sorry, a video in {desired_resolution} resolution is not available for download."
        )


# Get the link from the user
link: str = st.text_input("Enter the link of the video")

# Dropdown to select video resolution
resolutions = ["144p", "240p", "360p", "480p", "720p", "1080p"]
selected_resolution = st.selectbox("Select Video Resolution", resolutions)

st.write(  # type: ignore
    "Video will be downloaded in the downloads folder. If you want to change the path, please enter the path below else leave it empty."
)

# Get the path to save the video
path = st.text_input("Enter the path to save the video")

if st.button("Download Video"):
    download_custom_resolution(link, selected_resolution, path)
