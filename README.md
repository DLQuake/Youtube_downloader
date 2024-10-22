# YouTube Downloader

## Table of Contents
* [Brief Description of the Repository](#brief-description-of-the-repository)
* [Requirements](#requirements)
* [Instructions](#instructions)
* [Usage Examples](#usage-examples)
* [Downloads](#downloads)
* [Contributing](#contributing)
* [License](#license)

## Brief Description of the Repository
This repository contains a Python script that allows you to download videos from the [YouTube](https://www.youtube.com/) platform. The script utilizes the [yt-dlp](https://github.com/yt-dlp/yt-dlp) library, enabling users to easily download videos, audio, or both in various formats.

## Requirements

To run this program, you need to have Python installed on your computer (version 3.10 or higher). You also need to install the `yt-dlp` library, which can be done via pip:

```bash
pip install yt-dlp
```

Additionally, ensure you have [FFmpeg](https://ffmpeg.org/download.html) installed for optimal performance when merging audio and video files.

## Instructions

1. Clone or download the repository to your local machine.
2. Navigate to the project directory in your terminal or command prompt.
3. Run the program using Python:
    ```bash
    py main.py
    ```
4. When the program starts, you will see a menu with options to download from YouTube.
5. Enter the URL of the YouTube video you wish to download.
6. Choose the type of file you want to download (video, audio, video without audio, or all).
7. Wait for the download to complete. The files will be saved in their respective folders (`Videos`, `Audios`, or `Videos_without_audio`) in the current directory.
8. To exit the program, select option 2 from the main menu.

## Usage Examples

### Downloading a Video
1. Start the program.
2. Enter the video URL.
3. Choose to download the video.
4. Find the downloaded video in the `Videos` folder.

### Downloading Audio
1. Start the program.
2. Enter the video URL.
3. Choose to download audio only.
4. Find the audio file in the `Audios` folder.

## Downloads
You can download the repository using one of the following methods:
* Clone the repository using Git:
    ```bash
    git clone https://github.com/DLQuake/Youtube_downloader.git
    ```
* Download the repository as a ZIP file:
[Download ZIP](https://github.com/DLQuake/Youtube_downloader/archive/refs/heads/main.zip).