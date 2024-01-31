import json
from pydub import AudioSegment
from gtts import gTTS
from time import sleep, perf_counter
from threading import Thread
import os
with open('C:\\Users\\a_zhuck\Documents\GitHub\sound_JSON\example_json.json', encoding = 'utf-8') as example_file:
    data = json.load(example_file)

def make_mp3(data):
    def make_mp3_from_text(text, lang, slow, mp3):
        audio = gTTS(text=text, lang=lang, slow=slow)
        audio.save(mp3)

    if type(data) == dict:
        dictionary = data

        t1 = Thread(target=make_mp3_from_text(text="словарь", lang="ru", slow=False, mp3="example_dict.mp3"))
        # audio = gTTS(text="словарь", lang="ru", slow=False)
        # audio.save("example_dict.mp3")
        t1.start()
        flag_is_alive = t1.is_alive()
        while flag_is_alive:
            sleep(1)
            flag_is_alive = t1.is_alive()
        t1.join()
        sound_dict = AudioSegment.from_mp3("example_dict.mp3")
        sound_dict.export("example.mp3", format="mp3")
        for key in dictionary:
            str_to_mp3 = str(key)
            t1 = Thread(target=make_mp3_from_text(text=str_to_mp3, lang="en", slow=False, mp3="example_key.mp3"))
            # audio = gTTS(text="словарь", lang="ru", slow=False)
            # audio.save("example_dict.mp3")
            t1.start()
            flag_is_alive = t1.is_alive()
            while flag_is_alive:
                sleep(1)
                flag_is_alive = t1.is_alive()
            t1.join()
            # audio = gTTS(text=str_to_mp3, lang="en", slow=False)
            # audio.save("example_key.mp3")
            make_mp3(dictionary[key])
            #соединить звук key + value
            sound_key = AudioSegment.from_mp3("example_key.mp3")
            sound_value = AudioSegment.from_mp3("example.mp3")
            sound_key_value = sound_key + sound_value

            # соединить звук словарь + элемент словаря
            sound_dict = AudioSegment.from_mp3("example_dict.mp3")
            sound_dict_new = sound_dict + sound_key_value
            sound_dict_new.export("example_dict.mp3", format="mp3")
        sound_dict = AudioSegment.from_mp3("example_dict.mp3")
        sound_dict.export("example.mp3", format="mp3")
    elif type(data) == list:
        list_values = data
        t1 = Thread(target=make_mp3_from_text(text="список", lang="ru", slow=False, mp3="example_list.mp3"))
        # audio = gTTS(text="словарь", lang="ru", slow=False)
        # audio.save("example_dict.mp3")
        t1.start()
        flag_is_alive = t1.is_alive()
        while flag_is_alive:
            sleep(1)
            flag_is_alive = t1.is_alive()
        t1.join()
        # audio = gTTS(text="список", lang="ru", slow=False)
        # audio.save("example_list.mp3")
        for element in list_values:
            make_mp3(element)
            # соединить звук словарь + элемент словаря
            sound_list = AudioSegment.from_mp3("example_list.mp3")
            sound_el = AudioSegment.from_mp3("example.mp3")
            sound_list_new = sound_list + sound_el
            sound_list_new.export("example_list.mp3", format="mp3")
        sound_list = AudioSegment.from_mp3("example_list.mp3")
        sound_list.export("example.mp3", format="mp3")
    else:
        str_to_mp3 = str(data)
        # re.search(r'[^a-zA-Z а-яА-ЯёЁ]',a )
        t1 = Thread(target=make_mp3_from_text(text=str_to_mp3, lang="ru", slow=False, mp3="example.mp3"))
        # audio = gTTS(text="словарь", lang="ru", slow=False)
        # audio.save("example_dict.mp3")
        t1.start()
        flag_is_alive = t1.is_alive()
        while flag_is_alive:
            sleep(1)
            flag_is_alive = t1.is_alive()
        t1.join()
        # audio = gTTS(text=mytext, lang="ru", slow=False)
        # audio.save("example.mp3")


def make_mp3_from_json(json_path):
    with open(json_path, encoding='utf-8') as example_file:
        data = json.load(example_file)
    make_mp3(data)

#'C:\\Users\\a_zhuck\Documents\GitHub\sound_JSON\example_json.json'




