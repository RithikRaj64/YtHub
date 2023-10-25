import streamlit as st
from pytube import YouTube
import os

st.set_page_config(
    page_title="YtHub | Audio Downloader",
    layout="centered",
    page_icon="🎥",
    initial_sidebar_state="auto",
)


def convert_video_to_audio(link: str, path: str) -> None:
    yt = YouTube(link)

    # Choose the audio stream with the highest quality
    audio_stream = (
        yt.streams.filter(only_audio=True, file_extension="webm")  # type: ignore
        .order_by("abr")
        .desc()
        .first()
    )

    if not path:
        path = os.path.join(os.path.expanduser("~"), "Downloads")

    if audio_stream:
        audio_stream.download(output_path=path)
        st.success("Video converted to audio and downloaded successfully.")
    else:
        st.error("Sorry, couldn't convert the video to audio.")


# Get the link from the user
link = st.text_input("Enter the link of the video")

st.write(  # type: ignore
    "Audio will be converted and downloaded in the downloads folder. If you want to change the path, please enter the path below or leave it empty."
)

# Get the path to save the audio
path = st.text_input("Enter the path to save the audio")

if st.button("Convert to Audio"):
    convert_video_to_audio(link, path)
