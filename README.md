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
- in the "files" folder add the videos to convert and transcript and modify the names in each case replacing the text of MY_FYLE_NAME wiht the your file's name, the transciption and video convertion work with .mov and mp4 formats

    ```
    #videoConverter.py 
    input_file = 'files/MY_FYLE_NAME.mov'
    ```

    ```
    #whisperTranscription.py
    file_name = 'MY_FYLE_NAME'
    ```


- 🟨 list dependences to recreate virtual environment, run in the case that you install or uninstall dependences

    pip freeze > requirements.txt

## STEPS TO RUN THE PROJECT FIRS TIME

these are the steps documenting how was created the project with extra info, is not necessary do them at least you want to do all manually

python3 -m venv myenv 

source myenv/bin/activate

pip3 install moviepy SpeechRecognition googletrans==4.0.0-rc1 pydub httpcore==0.9.1 translate
pip install moviepy openai-whisper googletrans==4.0.0-rc1 rich

use for openai-whisper and vosk
    brew install ffmpeg

### **OPENAI-WHISPER**
pip3 install openai-whisper

### **for video converter**
pip3 install rich

### **VOSK - NO USED**
pip3 install vosk

