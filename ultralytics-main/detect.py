import warnings
warnings.filterwarnings('ignore')
from ultralytics import YOLO

# 推理参数官方详解链接：https://docs.ultralytics.com/modes/predict/#inference-sources:~:text=of%20Results%20objects-,Inference%20Arguments,-model.predict()

if __name__ == '__main__':
    # model = YOLO('runs/train/oilexp/weights/best.pt') # select your model.pt path
    model = YOLO('runs/train/oilexp6/weights/best.pt') # select your model.pt path
    
    model.predict(
                # source='/home/lenovo/data/liujiaji/Oildata/images/test',
        
                # source='/home/lenovo/data/liujiaji/Oildata/DJI_20240926150333_0001_S.MP4', # 5594,
                source='/home/lenovo/data/liujiaji/Oildata/DJI_20240926150333_0001_Z.MP4', #3057,,2696
                # source='/home/lenovo/data/liujiaji/Oildata/DJI_20240926153243_0001_S.MP4',
                # source='/home/lenovo/data/liujiaji/Oildata/DJI_20240927094110_0001_S.MP4', # 3374
                # source='/home/lenovo/data/liujiaji/Oildata/DJI_20240927095133_0001_S.MP4',# 
                # source='/home/lenovo/data/liujiaji/Oildata/DJI_20240927095908_0001_S.MP4', #
                # source='/home/lenovo/data/liujiaji/Oildata/DJI_20240927100240_0019_Z.MP4', # 5022,,3803
                
                  imgsz=800,
                  project='runs/detect',
                  name='multi/conf-0.85/oilexp',
                  save=True,
                  conf=0.94,
                  # iou=0.7,
                  # agnostic_nms=True,
                  # visualize=True, # visualize model features maps
                  line_width=10, # line width of the bounding boxes
                  show_conf=True, # do not show prediction confidence
                  show_labels=True, # do not show prediction labels
                  save_txt=True, # save results as .txt file
                  # save_crop=True, # save cropped images with results
                )