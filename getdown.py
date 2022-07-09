from glob import glob
from pathlib import Path
from shutil import rmtree
import cv2
import os


def img_resize(image, size=(640, 480), load=False, save=False, save_path="./resize.png"):
    if load:
        image = cv2.imread(image)
    image = cv2.resize(image, dsize=size)
    if save:
        cv2.imwrite(save_path, image)
    return image


def video_gen(width=640, height=480, path="./", chaos="./chaos/", eternallove="./eternallove/",
              getdown="./getdown/", lookatme="./lookatme/", nothing="./nothing/", swing="./swing/",
              outputname="getdown.mp4", output_path="./"):
    print("gen start")
    fps = 25
    folder = [nothing, getdown, chaos, lookatme, swing, eternallove]
    frame = []
    if not os.path.exists("./temp"):
        os.mkdir("./temp")

    counter = 0
    for i in folder:
        paths = glob(str(path) + str(i) + "*.png")
        for j, p in enumerate(paths):
            image = img_resize(cv2.imread(p), size=(width, height))
            s = str(counter).zfill(2)
            cv2.imwrite("./temp/" + s + ".png", image)
            counter += 1

    temp = "./temp/"
    folder = [temp]
    for i in folder:
        p = Path(str(i) + "%02d.png")
        cap = cv2.VideoCapture(str(p))
        while True:
            # 1フレームずつ取得する。
            ret, f = cap.read()

            if not ret:
                break  # 取得に失敗した場合
            else:
                frame.append(f)

        cap.release()

    format = cv2.VideoWriter_fourcc(*"mp4v")
    writer = cv2.VideoWriter(output_path + outputname,
                             format, fps, (width, height))

    for i in range(51):
        # 無
        writer.write(frame[0])

    for i in range(12):
        # ゲッ
        writer.write(frame[1])
    for i in range(12):
        # ダン
        writer.write(frame[2])
    for i in range(216):
        # ユーレルマーワルフーレルセツナーイキモチー
        writer.write(frame[3 + (i % 16)])
    for i in range(2):
        # ミツメテ
        for j in range(10):
            writer.write(frame[19 + j])
    for i in range(26):
        # ワタシーダケ
        writer.write(frame[3 + (i % 16)])
    for i in range(2):
        # ミツメテ
        for j in range(10):
            writer.write(frame[19 + j])
    for i in range(9):
        # アスヲー
        for j in range(3):
            writer.write(frame[29])
        for j in range(3):
            writer.write(frame[30])
    for i in range(13):
        # ピタッ
        writer.write(frame[31])
    for i in range(12):
        # ち
        writer.write(frame[32])
    for i in range(12):
        # か
        writer.write(frame[33])
    for i in range(12):
        # う
        writer.write(frame[32])

    for i in range(216):
        # ギュッッットダーカレモーエルコイゴーコロー
        writer.write(frame[3 + (i % 16)])
    for i in range(2):
        # アイシテル
        for j in range(10):
            writer.write(frame[19 + j])
    for i in range(26):
        # キョウヨーリ
        writer.write(frame[3 + (i % 16)])
    for i in range(2):
        # アイシテル
        for j in range(10):
            writer.write(frame[19 + j])
    for i in range(9):
        # ズットー
        for j in range(3):
            writer.write(frame[29])
        for j in range(3):
            writer.write(frame[30])
    for i in range(13):
        # ピタッ
        writer.write(frame[31])
    for i in range(12):
        # エ
        writer.write(frame[32])
    for i in range(12):
        # ター
        writer.write(frame[33])
    for i in range(12):
        # ナル
        writer.write(frame[32])
    for i in range(101):
        # looooooooooooveeeeeeeeeeee
        writer.write(frame[3 + (i % 16)])

    for i in range(89):
        # 無
        writer.write(frame[0])

    writer.release()
    rmtree("./temp/")

    print("complete")


if __name__ == "__main__":
    video_gen(path="./yukari/", width=640, height=480)

# video_gen()
#   width : 動画の横幅
#   height : 動画の縦幅
#   path : 以下のフォルダが存在するフォルダのパス
#   chaos, eternallove, getdown, lookatme, nothing, swing : pathからそれぞれのフォルダへの相対パス
#   outputname : 出力する動画のファイル名
#   outputpath : 出力するフォルダへのパス

#   初期値
#   def video_gen(width=640, height=480, path="./", chaos="./chaos/", eternallove="./eternallove/",
#                 getdown="./getdown/", lookatme="./lookatme/", nothing="./nothing/", swing="./swing/",
#                 outputname="getdown.mp4", output_path="./"):
