import json
from gtts import gTTS


# we make audio from text in var text and add binary audio to output stream f
def make_mp3_from_text(text, lang, slow, f):
    audio = gTTS(text=text, lang=lang, slow=slow)
    audio.write_to_fp(f)

# we make audio from data and use make_mp3_from_text
# data can be - dictionary, list, string and integer
# for dictionary and list we make recursive
# for atomic types we make audio in ru lang
def make_mp3(data, f):

    if type(data) == dict:
        dictionary = data
        make_mp3_from_text(text="словарь", lang="ru", slow=False, f=f)
        for key in dictionary:
            str_to_mp3 = str(key)
            make_mp3_from_text(text=str_to_mp3, lang="en", slow=False, f=f)
            make_mp3(dictionary[key], f)
            make_mp3_from_text(text=str_to_mp3 + " значение закончено", lang="en", slow=False, f=f)
    elif type(data) == list:
        list_values = data
        make_mp3_from_text(text="список", lang="ru", slow=False, f=f)
        n = 0
        for element in list_values:
            make_mp3(element, f)
            n += 1
    else:
        str_to_mp3 = str(data)
        make_mp3_from_text(text=str_to_mp3, lang="ru", slow=False, f=f)

# read json in dictionary
# open audio binary stream for output
# use make_mp3
def make_mp3_from_json(json_path):
    with open(json_path, encoding='utf-8') as example_file:
        data = json.load(example_file)
    with open('source/result.mp3', 'wb') as f:
        make_mp3(data, f)



