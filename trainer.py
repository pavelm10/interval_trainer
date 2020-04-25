from subprocess import run
import time
import pathlib
from ruamel.yaml import safe_load

FDIR = pathlib.Path(__file__).parent.resolve()
VLC = 'C:/Program Files/VideoLAN/VLC/vlc.exe'


class Trainer:

    DATABASE = FDIR / 'sounds'

    def __init__(self, cfg, break_sec=15):
        self.train_seq = cfg
        self.break_sec = max(0, break_sec - 3)

    def train(self):
        self.play_sound('get ready for kick ass training')
        for exc in self.train_seq:
            ex = list(exc.keys())[0]
            dur = exc[ex]
            print(ex, dur)
            self.play_sound(ex)
            self.play_sound(str(dur))
            time.sleep(self.break_sec)

            self.play_sound('ready and go')
            time.sleep(dur)

            self.play_sound('stop')

        self.play_sound('you kick ass you rock high five')

    def play_sound(self, exercise):
        exercise = exercise.replace(" ", "_")
        file = self.DATABASE / (exercise + '.mp3')
        cmd = f'"{VLC}" -I null --play-and-exit {file}'
        run(cmd)


if __name__ == "__main__":
    import argparse

    argp = argparse.ArgumentParser()
    argp.add_argument('--cfg',
                      help='path to the training sequence yml file',
                      default='training.yml')
    argp.add_argument('--break',
                      help='length of the break between training repetitions',
                      dest='break_sec',
                      default=15,
                      type=int)

    args = argp.parse_args()

    with open(args.cfg, 'r') as f:
        seq = safe_load(f)

        trainer = Trainer(seq, args.break_sec)
        trainer.train()
