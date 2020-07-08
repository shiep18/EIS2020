import dlib
import numpy as np
import cv2
import pandas as pd
import os
from PIL import Image, ImageDraw, ImageFont
import pyzbar.pyzbar as pyzbar
import time
import expressdata as ex
import pymysql
from MyQR import myqr
from xpinyin import Pinyin

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor(
    'data/data_dlib/shape_predictor_68_face_landmarks.dat')
face_reco_model = dlib.face_recognition_model_v1(
    "data/data_dlib/dlib_face_recognition_resnet_model_v1.dat")


def decodeDisplay(image):
    barcodes = pyzbar.decode(image)
    barcodeData = 99999
    for barcode in barcodes:
        # 提取条形码的边界框的位置
        # 画出图像中条形码的边界框
        (x, y, w, h) = barcode.rect
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)

        # 条形码数据为字节对象，所以如果我们想在输出图像上
        # 画出来，就需要先将它转换成字符串
        barcodeData = barcode.data.decode("utf-8")
        barcodeType = barcode.type

        # 绘出图像上条形码的数据和条形码类型
        text = "{} ({})".format(barcodeData, barcodeType)
        cv2.putText(image, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, .5,
                    (0, 0, 125), 2)

        # 向终端打印条形码数据和条形码类型
        #print("[INFO] Found {} barcode: {}".format(barcodeType, barcodeData))
    return image, barcodeData


class Face_Recognizer:
    def __init__(self):
        self.features_known_list = []
        self.name_known_cnt = 0
        self.name_known_list = []
        self.pos_camera_list = []
        self.name_camera_list = []
        self.faces_cnt = 0
        self.features_camera_list = []
        self.fps = 0
        self.frame_start_time = 0

    def get_face_database(self):
        if os.path.exists("data/features_all.csv"):
            path_features_known_csv = "data/features_all.csv"
            csv_rd = pd.read_csv(path_features_known_csv, header=None)
            for i in range(csv_rd.shape[0]):
                features_someone_arr = []
                for j in range(0, 128):
                    if csv_rd.iloc[i][j] == '':
                        features_someone_arr.append('0')
                    else:
                        features_someone_arr.append(csv_rd.iloc[i][j])
                self.features_known_list.append(features_someone_arr)
                self.name_known_list.append("Person_" + str(i + 1))
            self.name_known_cnt = len(self.name_known_list)
            print("Faces in Database：", len(self.features_known_list))
            return 1
        else:
            print('##### Warning #####', '\n')
            print("'features_all.csv' not found!")
            print(
                "Please run 'get_faces_from_camera.py' and 'features_extraction_to_csv.py' before 'face_reco_from_camera.py'",
                '\n')
            print('##### End Warning #####')
            return 0

    @staticmethod
    def return_euclidean_distance(feature_1, feature_2):
        feature_1 = np.array(feature_1)
        feature_2 = np.array(feature_2)
        dist = np.sqrt(np.sum(np.square(feature_1 - feature_2)))
        return dist

    def update_fps(self):
        now = time.time()
        self.frame_time = now - self.frame_start_time
        self.fps = 1.0 / self.frame_time
        self.frame_start_time = now

    def draw_note(self, img_rd):
        font = cv2.FONT_ITALIC
        cv2.putText(img_rd, "Face Recognizer", (20, 40), font, 1,
                    (255, 255, 255), 1, cv2.LINE_AA)
        cv2.putText(img_rd, "FPS:   " + str(self.fps.__round__(2)), (20, 100),
                    font, 0.8, (0, 255, 0), 1, cv2.LINE_AA)
        cv2.putText(img_rd, "Faces: " + str(self.faces_cnt), (20, 140), font,
                    0.8, (0, 255, 0), 1, cv2.LINE_AA)
        cv2.putText(img_rd, "Q: Quit", (20, 450), font, 0.8, (255, 255, 255),
                    1, cv2.LINE_AA)

    def draw_name(self, img_rd):
        font = ImageFont.truetype("simsun.ttc", 30)
        img = Image.fromarray(cv2.cvtColor(img_rd, cv2.COLOR_BGR2RGB))
        draw = ImageDraw.Draw(img)
        for i in range(self.faces_cnt):
            draw.text(xy=self.pos_camera_list[i],
                      text=self.name_camera_list[i],
                      font=font)
            img_with_name = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
        return img_with_name

    def modify_name_camera_list(self):
        self.name_known_list[0] = '王文政'.encode('utf-8').decode()
        self.name_known_list[1] = '贾帅杰'.encode('utf-8').decode()
        self.name_known_list[2] = '王宇斌'.encode('utf-8').decode()
        #self.name_known_list[3] ='xx'.encode('utf-8').decode()
        #self.name_known_list[4] ='xx'.encode('utf-8').decode()

    def process(self, stream):
        if self.get_face_database():
            num_record = 0
            while stream.isOpened():
                flag, img_rd = stream.read()
                faces = detector(img_rd, 0)
                kk = cv2.waitKey(1)
                if kk == ord('q'):
                    break
                else:
                    self.draw_note(img_rd)
                    self.features_camera_list = []
                    self.faces_cnt = 0
                    self.pos_camera_list = []
                    self.name_camera_list = []
                    if len(faces) != 0:
                        num_record = num_record + 1
                        for i in range(len(faces)):
                            shape = predictor(img_rd, faces[i])
                            self.features_camera_list.append(
                                face_reco_model.compute_face_descriptor(
                                    img_rd, shape))
                        for k in range(len(faces)):
                            print("##### camera person", k + 1, "#####")
                            self.name_camera_list.append("unknown")
                            self.pos_camera_list.append(
                                tuple([
                                    faces[k].left(),
                                    int(faces[k].bottom() +
                                        (faces[k].bottom() - faces[k].top()) /
                                        4)
                                ]))
                            e_distance_list = []
                            for i in range(len(self.features_known_list)):
                                if str(self.features_known_list[i]
                                       [0]) != '0.0':
                                    print("with person",
                                          str(i + 1),
                                          "the e distance: ",
                                          end='')
                                    e_distance_tmp = self.return_euclidean_distance(
                                        self.features_camera_list[k],
                                        self.features_known_list[i])
                                    print(e_distance_tmp)
                                    e_distance_list.append(e_distance_tmp)
                                else:
                                    e_distance_list.append(999999999)
                            similar_person_num = e_distance_list.index(
                                min(e_distance_list))
                            print("Minimum e distance with person",
                                  self.name_known_list[similar_person_num])
                            if min(e_distance_list) < 0.4:
                                self.name_camera_list[
                                    k] = self.name_known_list[
                                        similar_person_num]
                                res = str(
                                    self.name_known_list[similar_person_num])
                                print("May be person " + str(
                                    self.name_known_list[similar_person_num]))
                            else:
                                res = "none"
                                print("Unknown person")
                            for kk, d in enumerate(faces):
                                cv2.rectangle(img_rd,
                                              tuple([d.left(),
                                                     d.top()]),
                                              tuple([d.right(),
                                                     d.bottom()]),
                                              (0, 255, 255), 2)
                            print('\n')
                        self.faces_cnt = len(faces)
                        self.modify_name_camera_list()
                        img_with_name = self.draw_name(img_rd)
                    else:
                        img_with_name = img_rd
                print("Faces in camera now:", self.name_camera_list, "\n")
                cv2.imshow("camera", img_with_name)
                self.update_fps()
                if num_record == 5:
                    return res

    def run(self):
        cap = cv2.VideoCapture(0)
        #cap.set(3, 480)
        res = self.process(cap)
        cap.release()
        cv2.destroyAllWindows()
        res=ex.getinfo(res)
        print(res)
        return int(res)


# def main():
#     Face_Recognizer_con = Face_Recognizer()
#     Face_Recognizer_con.run()

# Face_Recognizer.run()