import warnings
warnings.filterwarnings('ignore')
from ultralytics import YOLO

# 验证参数官方详解链接：https://docs.ultralytics.com/modes/val/#usage-examples:~:text=of%20each%20category-,Arguments%20for%20YOLO%20Model%20Validation,-When%20validating%20YOLO

if __name__ == '__main__':
    model = YOLO('runs/train/oilexp6/weights/best.pt')
    # model = YOLO('runs/distill/yolov8n-l2-exp1/weights/best.pt')
    model.val(data='/home/lenovo/data/liujiaji/powerGit/OilGit/Oildata.yaml',
              split='test',
              imgsz=800,
              batch=16,
              # iou=0.7,
              # rect=False,
              save_json=True, # if you need to cal coco metrice
              project='runs/test',
              name='oilexp',
              )