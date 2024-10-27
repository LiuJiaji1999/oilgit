import warnings
warnings.filterwarnings('ignore')
from ultralytics import YOLO

# 训练参数官方详解链接：https://docs.ultralytics.com/modes/train/#resuming-interrupted-trainings:~:text=a%20training%20run.-,Train%20Settings,-The%20training%20settings

if __name__ == '__main__':
    model = YOLO('ultralytics/cfg/models/v8/yolov8m.yaml')
    # model = YOLO('/home/lenovo/data/liujiaji/yolov8/ultralytics-main/runs/train/exp2/weights/last.pt')
    model.load('yolov8m.pt') # loading pretrain weights
    
    model.train(data='/home/lenovo/data/liujiaji/powerGit/OilGit/Oildata.yaml',
                cache=False,
                imgsz=640,
                epochs=300,
                batch=16, # 32
                close_mosaic=10,
                workers=8,# 4
                # device='0',
                optimizer='SGD', # using SGD
                patience=0, # close earlystop
                resume=True, # 断点续训,YOLO初始化时选择last.pt
                # amp=False, # close amp
                # fraction=0.2,
                cos_lr = True,
                project='runs/train',
                name='oilexp',
                )
