# 🎧🐍

## STEPS TO RECREAT VIRTUAL ENVIRONMENT

- install ffmpeg
    brew install ffmpeg

- is recomended install python 3.12 or higher
        
    brew install python@3.12

- create the virtual environment

    python3 -m venv myenv

- go to the virtual environment

    source myenv/bin/activate

- recreate virtual environment

    pip install -r requirements.txt

    NOTE: if happen an error that display something like

    path-that-error-especify -m pip install --upgrade pip

    replace "path-that-error-especify" with your path

- in the root project create the folders outputWhisper and files

    ```
    mkdir outputWhisper
    mkdir files
    ```

in the root create a .env file and add the following variables

    #IF USE_MAIN_FILE = 1
    USE_MAIN_FILE=1
    MAIN_FILE_NAME=FILE_NAME
    MAIN_EXTENSION=mov

    #IF USE_MAIN_FILE != 0
    #WP = whisperTranscription file
    #VC = videoConverter file
    FILE_NAME_WP=FILE_NAME
    EXTENSION_WP=mov
    FILE_NAME_VC=FILE_NAME
    EXTENSION_VC=mov

- in the "files" folder add the videos to convert and transcript and modify the FILE_NAME env variable with respective name

- run
    ```
    python3 whisperTranscription.py
    python3 videoConverter.py
    ```

- 🟨 list dependences to recreate virtual environment, run in the case that you install or uninstall dependences

    pip freeze > requirements.txt

## NOTES:

close pyenv 

    deactivate

## STEPS TO RUN THE PROJECT FIRS TIME

these are the steps documenting how was created the project with extra info, is not necessary do them at least you want to do all manually

python3 -m venv myenv 

source myenv/bin/activate

pip3 install moviepy openai-whisper googletrans==4.0.0-rc1 rich python-dotenv

use for openai-whisper and vosk
    brew install ffmpeg

### **OPENAI-WHISPER**
pip3 install openai-whisper

### **for video converter**
pip3 install rich

### **VOSK - NO USED**
pip3 install vosk

