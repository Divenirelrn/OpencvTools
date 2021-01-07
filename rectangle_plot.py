import pickle as pkl
import cv2
import random, os
import json

colors = pkl.load(open("pallete", "rb"))
def write(img, left, top, right, bottom, label):
    c1 = (left, top)
    c2 = (right, bottom)
    color = random.choice(colors)
    cv2.rectangle(img, c1, c2, color, 1)
    t_size = cv2.getTextSize(label, cv2.FONT_HERSHEY_PLAIN, 1 , 1)[0]
    c2 = c1[0] + t_size[0] + 3, c1[1] + t_size[1] + 4
    cv2.rectangle(img, c1, c2, color, -1)
    cv2.putText(img, label, (c1[0], c1[1] + t_size[1] + 4), cv2.FONT_HERSHEY_PLAIN, 1, [225,255,255], 1);
    return img


def main():
    img_dir = r"F:\object_detection\data\baidu_images_labeld\img_all"
    label_dir = r"F:\object_detection\data\baidu_images_labeld\labels"
    save_dir = r"F:\object_detection\data\baidu_images_labeld\img_all_plot"

    if not os.path.exists(save_dir):
        os.makedirs(save_dir)

    img_list = os.listdir(img_dir)
    for img in img_list:
        name, suffix = os.path.splitext(img)
        #读取图片
        img_path = os.path.join(img_dir, img)
        imge = cv2.imread(img_path)
        # imge = cv2.cvtColor(imge, cv2.COLOR_BGR2RGB)
        label = name + ".json"
        json_path = os.path.join(label_dir, label)
        with open(json_path, "r") as fp:
            data = json.load(fp)
        shapes = data["shapes"]
        for shape in shapes:
            label = shape["label"]
            points = shape["points"]
            left = int(points[0][0])
            top = int(points[0][1])
            right = int(points[1][0])
            bottom = int(points[1][1])
            write(imge, left, top, right, bottom, label)

        save_path = os.path.join(save_dir, img)
        cv2.imwrite(save_path, imge)

if __name__ == "__main__":
    main()