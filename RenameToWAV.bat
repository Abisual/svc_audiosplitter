@echo off
for %%F in (*.ogg *.mp3) do (
    echo Renaming file: %%F
    ren "%%F" "%%~nF.wav"
)
echo Complete!
pause