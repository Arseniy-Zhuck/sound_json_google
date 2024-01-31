# This is a sample Python script.
import json

from gtts import gTTS
from pydub import AudioSegment

from exp_gTTs import make_mp3, make_mp3s_from_json, make_mp3_from_text


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    make_mp3s_from_json('example_json.json')
    # make_mp3_from_text('start', 'en', False, 'result.mp3')
    # audio = AudioSegment.from_mp3('C:\\Users\\a_zhuck\Documents\GitHub\sound_JSON\\result.mp3')
    # audio.export("res_name.mp3", format="mp3")
    # collect_single_mp3_from_json('example_json.json')
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
