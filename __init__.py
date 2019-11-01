from pydub import AudioSegment
import os
import glob
import shutil


def get_filelist():
    return glob.glob('audio/mp3/*.mp3')


def convert(filename):
    song = AudioSegment.from_mp3(filename)
    # 120 seconds
    s120 = 120 * 1000
    first_30_seconds = song[:s120]
    l = filename.split('/')
    song[:s120].export("{filename}.wav".format(filename=filename), format="wav",
                       parameters=["-t 30", "-vn", "-ac 2", "-ar 44100", "-acodec pcm_s16le"])
    shutil.move("{filename}.wav".format(filename=filename),
                '/Users/taka/Documents/X-audio/mp3towav/audio/wav/{filename}.wav'.format(
                    filename=filename.split('/')[-1].replace('.mp3', '')))


def main():
    fl = get_filelist()
    for file in fl:
        print(os.path.abspath(file))
        convert(os.path.abspath(file))


if __name__ == '__main__':
    main()
