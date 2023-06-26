# SVC AudioSplitter
SVS Audio splitter is a program for splitting audio files into chunks of 10 (this can be changed) seconds. 10 seconds is the recommended time to train [so-vits-svc-fork AI](https://github.com/voicepaw/so-vits-svc-fork). Unfortunately, to avoid complications in its installation, it can only work with wav files, but if your folder contains files of other extensions, you can use a bat file that will change all your extensions to .wav. 
Please note that the bat file does not convert files to another format, but simply renames them, which can cause problems. If you have such problems, use any third-party converter.

## How it works

First clone the repository and run the script. You can also use a ready-made release for more convenient work: https://github.com/Abisual/svc_audiosplitter/releases/tag/Python

The default field is 10 seconds. You can change this value at your discretion.
The check mark is responsible for whether the source files will remain in place after processing or will be deleted. (before using, make sure that your sources are saved somewhere else).
After clicking on the button, you need to select all the source files that will be processed, then you need to select the folder where all the processed files will be uploaded.
