import os
import cv2


def get_frame_from_video(self, interval):
    """
    Args:
        video_name:输入视频名字
        interval: 保存图片的帧率间隔
    Returns:
    """
    # 开始读视频
    print('Start spliting video!')
    framePath = self.root + str(self.video_id)
    if not os.path.exists(framePath):
        os.makedirs(framePath)

    video_capture = cv2.VideoCapture(self.root + self.video_id + '.mp4')

    fps = video_capture.get(cv2.CAP_PROP_FPS)
    frame_all = video_capture.get(cv2.CAP_PROP_FRAME_COUNT)
    time_all = frame_all / fps

    i = 1
    j = 0

    while True:
        success, frame = video_capture.read()
        if (i / fps - j / fps) >= interval:
            j = i
            cv2.imwrite(framePath + '/' + str(int(i / fps)) + '.jpg', frame)
            print(framePath + '/' + str(int(i / fps)) + '.jpg')
        i += 1
        if not success:
            print('video is all read')
            break
    print('Split Over!')