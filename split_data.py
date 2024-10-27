import os, shutil, random
random.seed(0)
import numpy as np
from sklearn.model_selection import train_test_split

val_size = 0.1
test_size = 0.2
postfixes = ['jpg', 'JPG']  # 后缀为 'jpg' 和 'JPG'
imgpath = '/home/lenovo/data/liujiaji/Oildata/allimage1'
txtpath = '/home/lenovo/data/liujiaji/Oildata/alllabel1'

# 创建目标目录
os.makedirs('/home/lenovo/data/liujiaji/Oildata/images/train', exist_ok=True)
os.makedirs('/home/lenovo/data/liujiaji/Oildata/images/val', exist_ok=True)
os.makedirs('/home/lenovo/data/liujiaji/Oildata/images/test', exist_ok=True)
os.makedirs('/home/lenovo/data/liujiaji/Oildata/labels/train', exist_ok=True)
os.makedirs('/home/lenovo/data/liujiaji/Oildata/labels/val', exist_ok=True)
os.makedirs('/home/lenovo/data/liujiaji/Oildata/labels/test', exist_ok=True)

# 获取所有的标签文件
listdir = np.array([i for i in os.listdir(txtpath) if 'txt' in i])
random.shuffle(listdir)

# 分割训练集、验证集和测试集
train, val, test = listdir[:int(len(listdir) * (1 - val_size - test_size))], listdir[int(len(listdir) * (1 - val_size - test_size)):int(len(listdir) * (1 - test_size))], listdir[int(len(listdir) * (1 - test_size)):]

print(f'train set size: {len(train)} val set size: {len(val)} test set size: {len(test)}')

# 定义一个函数，处理图片文件的复制逻辑，处理不同的后缀
def copy_image_and_label(src_image_name, src_txt_name, dst_image_folder, dst_label_folder):
    # 检查两种后缀 'jpg' 和 'JPG'
    for postfix in postfixes:
        src_image_path = os.path.join(imgpath, f"{src_image_name}.{postfix}")
        if os.path.exists(src_image_path):
            # 如果图片存在，进行复制
            shutil.copy(src_image_path, os.path.join(dst_image_folder, f"{src_image_name}.{postfix}"))
            break  # 找到匹配后立即退出循环

    # 复制标签文件
    src_txt_path = os.path.join(txtpath, src_txt_name)
    dst_txt_path = os.path.join(dst_label_folder, src_txt_name)
    shutil.copy(src_txt_path, dst_txt_path)

# 复制训练集图片和标签
for i in train:
    copy_image_and_label(i[:-4], i, '/home/lenovo/data/liujiaji/Oildata/images/train', '/home/lenovo/data/liujiaji/Oildata/labels/train')

# 复制验证集图片和标签
for i in val:
    copy_image_and_label(i[:-4], i, '/home/lenovo/data/liujiaji/Oildata/images/val', '/home/lenovo/data/liujiaji/Oildata/labels/val')

# 复制测试集图片和标签
for i in test:
    copy_image_and_label(i[:-4], i, '/home/lenovo/data/liujiaji/Oildata/images/test', '/home/lenovo/data/liujiaji/Oildata/labels/test')
