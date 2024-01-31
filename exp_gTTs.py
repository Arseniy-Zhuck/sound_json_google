import json
from pydub import AudioSegment
from gtts import gTTS
from time import sleep, perf_counter
from threading import Thread
import os
def make_mp3_from_text(text, lang, slow, mp3, f):
    audio = gTTS(text=text, lang=lang, slow=slow)
    audio.save(mp3)
    audio.write_to_fp(f)

def make_mp3(data, file_name, f):

    if type(data) == dict:
        dictionary = data
        res_name = file_name
        make_mp3_from_text(text="словарь", lang="ru", slow=False, mp3=res_name + '.mp3', f=f)
        # audio = gTTS(text="словарь", lang="ru", slow=False)
        # audio.save("example_dict.mp3")
        for key in dictionary:
            str_to_mp3 = str(key)
            make_mp3_from_text(text=str_to_mp3, lang="en", slow=False, mp3=res_name + str_to_mp3 + '.mp3',f=f)
            make_mp3(dictionary[key], res_name + '[' + str_to_mp3 + ']', f)
    elif type(data) == list:
        list_values = data
        make_mp3_from_text(text="список", lang="ru", slow=False, mp3=file_name + '.mp3', f=f)
        n = 0
        for element in list_values:
            make_mp3(element, file_name + '[' + str(n) + ']',f)
            n += 1
            # соединить звук словарь + элемент словаря
    else:
        str_to_mp3 = str(data)
        make_mp3_from_text(text=str_to_mp3, lang="ru", slow=False, mp3=file_name + '.mp3', f=f)


def make_mp3s_from_json(json_path):
    with open(json_path, encoding='utf-8') as example_file:
        data = json.load(example_file)
    with open('result.mp3', 'wb') as f:
        make_mp3(data, 'res\\JSON', f)

#'C:\\Users\\a_zhuck\Documents\GitHub\sound_JSON\example_json.json'




