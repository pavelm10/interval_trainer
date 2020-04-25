"""
Script for sound generation,
it generates mp3 files based on the provided yml sound database file
"""
from gtts import gTTS
from ruamel.yaml import safe_load
import argparse
import pathlib

FDIR = pathlib.Path(__file__).parent.resolve()


def read_sound_database(file):
    with open(file, 'r') as f:
        return safe_load(f)


def generate_sound(text):
    text = str(text)
    myobj = gTTS(text=text, lang='en', slow=False)
    fname = text.replace(" ", "_")
    myobj.save(f"sounds/{fname}.mp3")


def main():
    argp = argparse.ArgumentParser()
    argp.add_argument('-i',
                      help='path to the sound database file',
                      default=(FDIR / 'sound_database.yml').as_posix())

    args = argp.parse_args()

    exercises = read_sound_database(args.i)
    for ex in exercises['exercises']:
        generate_sound(ex)


if __name__ == "__main__":
    main()
