import os
import json

def convert_voc_to_yolo(json_dir, output_dir):
    # 检查并创建输出目录
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # 遍历JSON目录中的所有文件
    for json_file in os.listdir(json_dir):
        if json_file.endswith('.json'):
            json_path = os.path.join(json_dir, json_file)
            
            # 打开并读取JSON文件
            with open(json_path, 'r', encoding='utf-8') as f:
                voc_data = json.load(f)
            
            # 获取图像的宽高信息
            img_width = voc_data['asset']['size']['width']
            img_height = voc_data['asset']['size']['height']

            # 生成YOLO标签文件名，与图片名一致
            file_name = voc_data['asset']['name']
            prefix = os.path.splitext(file_name)[0]
            yolo_file = os.path.join(output_dir, prefix + '.txt')

            # 打开 YOLO 标签文件进行写入
            with open(yolo_file, 'w') as yf:
                # 遍历JSON中的每个对象（假设这些对象包含边界框信息）
                for obj in voc_data['regions']:
         
                    label = obj['tags']
                    print(label)
                    height = obj['boundingBox']['height']
                    width = obj['boundingBox']['width']
                    xmin = obj['boundingBox']['left']
                    ymin = obj['boundingBox']['top']


                    # 计算 YOLO 格式所需的中心坐标、宽度和高度
                    x_center = (xmin + xmin + width) / 2.0
                    y_center = (ymin + ymin + height) / 2.0

                    # 归一化坐标
                    x_center /= img_width
                    y_center /= img_height
                    width /= img_width
                    height /= img_height
                    
                    # 这里假设 label 是从一个类名映射到一个类别ID的过程，你可以根据你的需求修改它
                    class_id = label_to_id(label)
                    # print(class_id)
                    
                    
                    # 写入YOLO格式: <class_id> <center_x> <center_y> <width> <height>
                    yf.write(f"{class_id} {x_center} {y_center} {width} {height}\n")

            print(f"转换完成：{json_file} -> {yolo_file}")


# 将类别名称映射到YOLO标签的class_id (根据你的具体类别修改)
def label_to_id( label_list):
    label_dict = {
        # 正常、异常
        # "Well normal": 0,
        # "Well lost": 1,
        # "Well with man": 1,
        # "Well with car": 1, 

        # "Warning-Stacks normal":0,
        # "Warning-Stacks damaged":1,
        # "Warning-Stacks with man":1,
        # "Warning-Stacks with car":1,

        # "Pointer normal": 0,
        # "Pointer abnormal": 1,

        # 缺陷类别
        "Well normal": 7,
        "Well lost": 0,
        "Well with man": 1,
        "Well with car": 2, 

        "Warning-Stacks normal":7,
        "Warning-Stacks damaged":3,
        "Warning-Stacks with man":4,
        "Warning-Stacks with car":5,

        "Pointer normal": 7,
        "Pointer abnormal": 6,




    }

    # 遍历列表中的每个键
    for key in label_list:
        # 如果字典中不存在该键，则将其值设为 -1
        if key not in label_dict:
            label_dict[key] = -1
    return label_dict[key]

# 示例用法
json_dir = '/home/lenovo/data/liujiaji/Oildata/Pointer/Pointer normal/json'  # JSON文件所在目录
output_dir = '/home/lenovo/data/liujiaji/Oildata/Pointer/Pointer normal/label1'  # YOLO标签保存目录

convert_voc_to_yolo(json_dir, output_dir)
