# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['owoi_audio_to_clip']

package_data = \
{'': ['*']}

install_requires = \
['Google-Images-Search>=1.4.6,<2.0.0',
 'black>=22.10.0,<23.0.0',
 'google-cloud-speech>=2.16.2,<3.0.0',
 'google-cloud-storage>=2.5.0,<3.0.0',
 'imageio[opencv]>=2.25.1,<3.0.0',
 'moviepy>=1.0.3,<2.0.0',
 'pytube>=12.1.2,<13.0.0']

setup_kwargs = {
    'name': 'owoi-audiotoclip',
    'version': '1.2.0',
    'description': 'Package to convert audio to video with google speech to text and google image search',
    'long_description': '# OWOI_AudioToClip\nPython module used for the school project OWOI (One Word One Image)\n\n## Installation\n\nAfter git cloning the repository, you can install the dependencies with the following command:\n\n```bash\npoetry install\n```\n\n## Credentials\n\nPlease provide your credentials in the following environment variables:\n\n```bash\nexport GOOGLE_APPLICATION_CREDENTIALS="path/to/credentials.json"\nexport GOOGLE_IMAGES_SEARCH_TOKEN="token"\nexport GOOGLE_SEARCH_ID="id"\n```\n\n## Classes\n\n### TranscriptFactory\n\nThis class is used to create a transcript from a text file. It will create a list of words and a list of timestamps.\n\n```python\t\nfrom owoi_audio_to_clip.TranscriptFactory import TranscriptFactory\n\ntranscript_factory = TranscriptFactory(gcs_uri="gs://bucket/file.mp3")\n```\n\nMethods:\n- ***transcribe_audio_to_text() -> list[dict]***: transcribe audio to text from the gcs_uri and returns a list of dict with the following keys: "word", "start_time" and "end_time"\n- ***get_word_timestamps() -> list[dict]***: returns a list of dict with the following keys: "word", "start_time" and "end_time"\n\nThis Class should be used to create a transcript from a text file before creating a clip with the ClipMakerFactory.\n\n### ClipMakerFactory\n\nThis class is used to create a clip from a transcript.\n\n```python\nfrom owoi_audio_to_clip.ClipMakerFactory import ClipMakerFactory\n\nclip_maker_factory = ClipMakerFactory(video_name, username, transcript, gcs_bucket_name, local_storage_path, gcs_audio_name, with_subtitles=True)\n```\n\nParams:\n- ***video_name***:str -> name of the video\n- ***username***:str -> name of the user\n- ***transcript***:list[WordTimestamp] -> list of WordTimestamp\n- ***gcs_bucket_dest***:str -> name of the gcs bucket destination\n- ***local_storage***:str -> path to the local storage destination\n- ***gcs_audio_path***:str -> path to the audio file in the gcs bucket\n- ***with_subtitles***:bool -> if True, subtitles will be added to the video\n\nMethods:\n- ***clip_maker(word_timestamps: list[WordTimestamp]) -> VideoFileClip***: creates a clip from the transcript and returns a VideoFileClip\n\n## Functions\n\n### Utils\n\n```python\nfrom owoi_audio_to_clip.utils import upload_audio_to_gcs, upload_video_to_gcs, purge_local_storage_images\n\nupload_audio_to_gcs(bucket_name, username, audio_name, local_storage_path)\nupload_video_to_gcs(bucket_name, username, video_name, local_storage_path)\npurge_local_storage_images(local_storage_path)\ndownload_audio_from_youtube(youtube_url, local_dest, username, audio_name, start_time, end_time, gcs_bucket_name)\n```\n\n#### download_audio_from_youtube\n\nThis function is used to download an audio file from a youtube video, and upload it to the gcs bucket.\n\nParams:\n- ***youtube_url***:str -> url of the youtube video\n- ***local_dest***:str -> path to the local storage destination (where the audio file will be downloaded, the program will create a folder with the username, and put the audio in an \'audios\' folder)\n- ***username***:str -> name of the user\n- ***audio_name***:str -> name of the audio file\n- ***start_time***:str -> start time of the audio file extracted from the youtube video\n- ***end_time***:str -> end time of the audio file extracted from the youtube video\n- ***gcs_bucket_name***:str -> name of the gcs bucket destination',
    'author': 'Pierre-Louis Sergent',
    'author_email': 'papa.louis59@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
