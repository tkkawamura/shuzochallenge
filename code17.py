# -- coding: utf-8 --
#!/usr/bin/env python3

import time
import boto3
import pandas as pd
import datetime
import RPi.GPIO as GPIO             #GPIO用のモジュールをインポート
import sys                          #sysモジュールをインポート
import itertools
import collections
import numpy as np
import csv
from pydub import AudioSegment
from pydub.playback import play
# バイナリデータを読み込む場合の一時ファイル用
from tempfile import NamedTemporaryFile
import simpleaudio

class SoundPlayer:
    """SoundPlayer module."""

    @classmethod
    def play(cls, filename, audio_format="mp3", wait=False, stop=False):
        """Play audio file."""

        if stop:
            simpleaudio.stop_all()

        seg = AudioSegment.from_file(filename, audio_format)
        playback = simpleaudio.play_buffer(
            seg.raw_data,
            num_channels=seg.channels,
            bytes_per_sample=seg.sample_width,
            sample_rate=seg.frame_rate
        )

        if wait:
            playback.wait_done()

    @classmethod
    def play_from_buffer(cls, audio_content, audio_format="mp3", wait=False, stop=False):
        """Play from buffer."""
        with NamedTemporaryFile() as fd:
            fd.write(audio_content)
            # Revert head of file. It is neccesary to play audio.
            fd.seek(0)
            cls.play(fd.name, audio_format=audio_format, wait=wait, stop=stop)

Sw_pin = 11                         #変数"Sw_pin"に17を格納
BtnPin = 12    # pin12 --- button

def setup():
    GPIO.setmode(GPIO.BOARD)       # Numbers GPIOs by physical location
    GPIO.setup(Sw_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(BtnPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)    # Set BtnPin's mode is input, and pull up to high level(3.3V)

def shuzoloop():
    BUCKET = "20210622cycle"
    now = datetime.datetime.now()
    filename = now.strftime('%Y%m%d_%H%M%S') + '.csv'
    KEY = filename

    d_today = datetime.date.today()
    d_now = datetime.datetime.now()

    d2 = d_now + datetime.timedelta(minutes=1)
    d2 = d2.strftime('%Y-%m-%d %H:%M')
    d3 = d_now + datetime.timedelta(minutes=2)
    d3 = d3.strftime('%Y-%m-%d %H:%M')
    d4 = d_now + datetime.timedelta(minutes=3)
    d4 = d4.strftime('%Y-%m-%d %H:%M')
    d5 = d_now + datetime.timedelta(minutes=4)
    d5 = d5.strftime('%Y-%m-%d %H:%M')
    d6 = d_now + datetime.timedelta(minutes=5)
    d6 = d6.strftime('%Y-%m-%d %H:%M')
    d7 = d_now + datetime.timedelta(minutes=6)
    d7 = d7.strftime('%Y-%m-%d %H:%M')
    d8 = d_now + datetime.timedelta(minutes=7)
    d8 = d8.strftime('%Y-%m-%d %H:%M')
    d9 = d_now + datetime.timedelta(minutes=8)
    d9 = d9.strftime('%Y-%m-%d %H:%M')
    d10 = d_now + datetime.timedelta(minutes=9)
    d10 = d10.strftime('%Y-%m-%d %H:%M')
    d11 = d_now + datetime.timedelta(minutes=10)
    d11 = d11.strftime('%Y-%m-%d %H:%M')
    d12 = d_now + datetime.timedelta(minutes=11)
    d12 = d12.strftime('%Y-%m-%d %H:%M')
    d13 = d_now + datetime.timedelta(minutes=12)
    d13 = d13.strftime('%Y-%m-%d %H:%M')
    d14 = d_now + datetime.timedelta(minutes=13)
    d14 = d14.strftime('%Y-%m-%d %H:%M')
    d15 = d_now + datetime.timedelta(minutes=14)
    d15 = d15.strftime('%Y-%m-%d %H:%M')
    d16 = d_now + datetime.timedelta(minutes=15)
    d16 = d16.strftime('%Y-%m-%d %H:%M')
    d17 = d_now + datetime.timedelta(minutes=16)
    d17 = d17.strftime('%Y-%m-%d %H:%M')
    d18 = d_now + datetime.timedelta(minutes=17)
    d18 = d18.strftime('%Y-%m-%d %H:%M')
    d19 = d_now + datetime.timedelta(minutes=18)
    d19 = d19.strftime('%Y-%m-%d %H:%M')
    d20 = d_now + datetime.timedelta(minutes=19)
    d20 = d20.strftime('%Y-%m-%d %H:%M')
    d21 = d_now + datetime.timedelta(minutes=20)
    d21 = d21.strftime('%Y-%m-%d %H:%M')
    d22 = d_now + datetime.timedelta(minutes=21)
    d22 = d22.strftime('%Y-%m-%d %H:%M')
    d23 = d_now + datetime.timedelta(minutes=22)
    d23 = d23.strftime('%Y-%m-%d %H:%M')
    d24 = d_now + datetime.timedelta(minutes=23)
    d24 = d24.strftime('%Y-%m-%d %H:%M')
    d25 = d_now + datetime.timedelta(minutes=24)
    d25 = d25.strftime('%Y-%m-%d %H:%M')
    d26 = d_now + datetime.timedelta(minutes=25)
    d26 = d26.strftime('%Y-%m-%d %H:%M')
    d27 = d_now + datetime.timedelta(minutes=26)
    d27 = d27.strftime('%Y-%m-%d %H:%M')
    d28 = d_now + datetime.timedelta(minutes=27)
    d28 = d28.strftime('%Y-%m-%d %H:%M')
    d29 = d_now + datetime.timedelta(minutes=28)
    d29 = d29.strftime('%Y-%m-%d %H:%M')
    d30 = d_now + datetime.timedelta(minutes=29)
    d30 = d30.strftime('%Y-%m-%d %H:%M')
    d_now = d_now.strftime('%Y-%m-%d %H:%M')
    counts = collections.Counter()
#   sound = AudioSegment.from_mp3("/usr/share/sounds/alsa/shuzo.mp3")

    for i in itertools.count():
        for _ in range(int(60/0.018)):
            if (GPIO.input(Sw_pin)):
                counts[i] += 1
            time.sleep(0.018)
            print(counts[i])
        if i == 31:
            break
        elif 1 < counts[i] < 79:
            SoundPlayer.play("/usr/share/sounds/alsa/shuzo.mp3")
    print("明日はもっと頑張ろうな！")
 
    list1=[[d_today,d_now,counts[0]],[d_today,d2,counts[1]],[d_today,d3,counts[2]],[d_today,d4,counts[3]],[d_today,d5,counts[4]],[d_today,d6,counts[5]],[d_today,d7,counts[6]],[d_today,d8,counts[7]],[d_today,d9,counts[8]],[d_today,d10,counts[9]],[d_today,d11,counts[10]],[d_today,d12,counts[11]],[d_today,d13,counts[12]],[d_today,d14,counts[13]],[d_today,d15,counts[14]],[d_today,d16,counts[15]],[d_today,d17,counts[16]],[d_today,d18,counts[17]],[d_today,d19,counts[18]],[d_today,d20,counts[19]],[d_today,d21,counts[20]],[d_today,d22,counts[21]],[d_today,d23,counts[22]],[d_today,d24,counts[23]],[d_today,d25,counts[24]],[d_today,d26,counts[25]],[d_today,d27,counts[26]],[d_today,d28,counts[27]],[d_today,d29,counts[28]],[d_today,d30,counts[29]]]
    #columns1 = [1]
    #dataframe作成
    #df = pd.DataFrame(data=list1,columns=columns1)
    df = pd.DataFrame(data=list1)
    df.index = np.arange(1, len(df)+1)
    df.to_csv(filename)
    s3 = boto3.resource('s3')
    s3.Bucket(BUCKET).upload_file(Filename=KEY, Key=KEY)

def loop():
    while True:
        if GPIO.input(BtnPin) == GPIO.LOW: # Check whether the button is pressed.
            sound = AudioSegment.from_mp3("/usr/share/sounds/alsa/3seconds.mp3")
            play(sound)
            shuzoloop()
        else:
            print ('修造待機中...')
        time.sleep(0.2)

def destroy():
    GPIO.cleanup()                     # Release resource
    print('-- お疲れ様、またがんばろうな！ --')

if __name__ == '__main__':     # Program start from here
    setup()
    try:
        loop()
    except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
        destroy()
