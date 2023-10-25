import streamlit as st
import moviepy.editor as mp
import os

st.set_page_config(
    page_title="YtHub | Webm to MP3",
    layout="centered",
    page_icon="🎥",
    initial_sidebar_state="auto",
)


def convert_to_mp3_and_delete_webm(path: str | None) -> None:
    if not path:
        st.error("Please enter a valid file path.")
        return

    # If there is  " in start and end of the path, remove them
    path = path.strip('"')  # type: ignore

    # Check if the file exists at the given path
    if not os.path.exists(path):
        st.error("The file does not exist at the specified path.")
        return

    # Get the base filename (without extension) and the folder
    base_filename, _ = os.path.splitext(os.path.basename(path))
    folder = os.path.dirname(path)

    # Generate the path for the MP3 file in the same folder
    mp3_path = os.path.join(folder, f"{base_filename}.mp3")

    try:
        clip = mp.AudioFileClip(path)
        clip.write_audiofile(mp3_path)

        # Delete the original WebM file
        os.remove(path)

        st.success(
            f"Video converted to audio (MP3) and saved as {base_filename}.mp3 in the same folder. The WebM file has been deleted."
        )
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")


# Get the path from the user
path = st.text_input("Enter the path of the webm file")

if st.button("Convert to MP3 and Delete WebM"):
    convert_to_mp3_and_delete_webm(path)
