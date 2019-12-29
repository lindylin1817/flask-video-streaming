import time
from base_camera import BaseCamera
import cv2


class Camera(BaseCamera):
    """An emulated camera implementation that streams a repeated sequence of
    files 1.jpg, 2.jpg and 3.jpg at a rate of one frame per second."""
    imgs = [open(f + '.jpg', 'rb').read() for f in ['1', '2', '3']]

    @staticmethod
    def frames():
        tmp_image_name = "../detectron/my_inference/tmp_out.jpg"
        while True:
            image = []
            time.sleep(0.3)
#            img = open(tmp_image_name, 'rb')
            try:
                print("1")
                image = cv2.imread(tmp_image_name)
                image1 = cv2.resize(image, (400, 240), interpolation=cv2.INTER_AREA)
                yield cv2.imencode('.jpg', image1)[1].tobytes()
            except:
                print("error image")

'''            
            try:
                print("1")
                image = cv2.imread(tmp_image_name)
                image1 = cv2.resize(image, (640, 400), interpolation=cv2.INTER_AREA)
                yield cv2.imencode('.jpg', image1)[1].tobytes()
            except:
                print("3")
                try:
                    print("2")
                    image = cv2.imread(tmp_image_name)
                    image1 = cv2.resize(image, (640, 400), interpolation=cv2.INTER_AREA)
                    yield cv2.imencode('.jpg', image1)[1].tobytes()
                except:
                    print("error image")
'''

'''
    @staticmethod
    def frames():
        vid_cap = cv2.VideoCapture("./warehouse_small.mp4")
#        tmp_image_name = "./tmp_img.jpg"
        frame_id = 0
        while True:
            time.sleep(0.1)
            success, image = vid_cap.read()
#            cv2.imwrite(tmp_image_name, image)
            yield cv2.imencode('.jpg', image)[1].tobytes()

    @staticmethod
    def frames():
        while True:
            time.sleep(1)
            yield Camera.imgs[int(time.time()) % 3]
'''