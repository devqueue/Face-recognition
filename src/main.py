#!~/.virtualenvs/facerec/bin/python3.8
import sys
from datacollect import datacollect
import photocam
import facetrainer
import facedetect



def main():
  game = Game()
  game.run()
  sys.exit()


if __name__ == '__main__':
    main()
