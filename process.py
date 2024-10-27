# ###### 判断不同类别下 是否有重复图片
# # import os
# # from collections import defaultdict

# # def find_duplicate_filenames(directories):
# #     # 用于存储文件名及其出现的路径
# #     file_map = defaultdict(list)

# #     # 遍历每个目录
# #     for directory in directories:
# #         if os.path.exists(directory):
# #             for root, _, files in os.walk(directory):
# #                 for file in files:
# #                     file_map[file].append(os.path.join(root, file))
# #         else:
# #             print(f"目录 {directory} 不存在。")

# #     # 找出重复的文件名
# #     duplicates = {file: paths for file, paths in file_map.items() if len(paths) > 1}

# #     return duplicates

# # # 示例用法
# # directories = [
# #     '/home/lenovo/data/liujiaji/Oildata/Warning-Stacks/label',  # 第一个目录
# #     '/home/lenovo/data/liujiaji/Oildata/Warning-Stacks/image',  # 第二个目录
# #     # '/home/lenovo/data/liujiaji/Oildata/Well/Well with man:car/label'   # 第三个目录
# # ]

# # duplicates = find_duplicate_filenames(directories)

# # # 输出重复的文件名及其路径
# # if duplicates:
# #     print("找到重复的文件名:")
# #     for file, paths in duplicates.items():
# #         print(f"{file}:")
# #         for path in paths:
# #             print(f"  - {path}")
# # else:
# #     print("没有找到重复的文件名。")

# ############# 按标签拆分数据集
# import os
# import json
# import shutil

# imgpath = '/home/lenovo/data/liujiaji/Oildata/Warning-Stacks/image'
# txtpath = '/home/lenovo/data/liujiaji/Oildata/Warning-Stacks/label'
# jsonpath = '/home/lenovo/data/liujiaji/Oildata/Warning-Stacks/json'

# dst_base_img_dir = '/home/lenovo/data/liujiaji/Oildata/Warning-Stacks/split_images'
# dst_base_label_dir = '/home/lenovo/data/liujiaji/Oildata/Warning-Stacks/split_labels'

# # 创建目标基目录
# os.makedirs(dst_base_img_dir, exist_ok=True)
# os.makedirs(dst_base_label_dir, exist_ok=True)

# # 获取所有JSON文件
# json_files = [f for f in os.listdir(jsonpath) if f.endswith('.json')]

# # 遍历每个JSON文件
# for json_file in json_files:
#     json_file_path = os.path.join(jsonpath, json_file)

#     # 打开并解析JSON文件
#     with open(json_file_path, 'r') as f:
#         data = json.load(f)
    
#     # 假设JSON文件中有一个字段 "label" 对应标签
#     for obj in data['regions']:
#         label_list = obj['tags']  # 获取标签
#         for label in label_list:
#             # print(label)

#             # 为该标签创建目录
#             dst_img_dir = os.path.join(dst_base_img_dir, label)
#             dst_label_dir = os.path.join(dst_base_label_dir, label)
#             os.makedirs(dst_img_dir, exist_ok=True)
#             os.makedirs(dst_label_dir, exist_ok=True)

#             file_name = data['asset']['name']
#             prefix = os.path.splitext(file_name)[0]

#             # 构建源文件路径
#             img_file_jpg = f"{prefix}.jpg"
#             img_file_JPG = f"{prefix}.JPG"
#             label_file = f"{prefix}.txt"

#             src_img_path_jpg = os.path.join(imgpath, img_file_jpg)
#             src_img_path_JPG = os.path.join(imgpath, img_file_JPG)
#             src_label_path = os.path.join(txtpath, label_file)

#             # 复制图片文件到对应标签目录
#             if os.path.exists(src_img_path_jpg):
#                 shutil.copy(src_img_path_jpg, os.path.join(dst_img_dir, img_file_jpg))
#             elif os.path.exists(src_img_path_JPG):
#                 shutil.copy(src_img_path_JPG, os.path.join(dst_img_dir, img_file_JPG))
#             else:
#                 print(f"图片文件 {img_file_jpg} 或 {img_file_JPG} 不存在，跳过。")

#             # 复制标签文件到对应标签目录
#             if os.path.exists(src_label_path):
#                 shutil.copy(src_label_path, os.path.join(dst_label_dir, label_file))
#             else:
#                 print(f"标签文件 {label_file} 不存在，跳过。")

import os

# 文件路径
img_dir = '/home/lenovo/data/liujiaji/Oildata/Pointer/Pointer-normal/sourceimage'
label_dir = '/home/lenovo/data/liujiaji/Oildata/Pointer/Pointer-normal/label1'

# 定义新文件的前缀
new_prefix = 'new_image_pointernor'

# 获取所有的图片文件和标签文件
img_files = [f for f in os.listdir(img_dir) if f.endswith(('.jpg', '.JPG'))]
label_files = [f for f in os.listdir(label_dir) if f.endswith('.txt')]

# 确保图片和标签文件的数量匹配
if len(img_files) != len(label_files):
    print("图片文件和标签文件数量不匹配，请检查！")
else:
    # 按照相同的顺序对文件进行重命名
    for idx, img_file in enumerate(img_files):
        # 获取文件名的前缀（不带扩展名）
        base_name = os.path.splitext(img_file)[0]

        # 新的文件名
        new_img_name = f"{new_prefix}{idx + 1}.jpg"  # 你可以选择 .jpg 或 .JPG
        new_label_name = f"{new_prefix}{idx + 1}.txt"

        # 定义源文件路径和目标文件路径
        src_img_path = os.path.join(img_dir, img_file)
        src_label_path = os.path.join(label_dir, f"{base_name}.txt")

        dst_img_path = os.path.join(img_dir, new_img_name)
        dst_label_path = os.path.join(label_dir, new_label_name)

        # 重命名图片和标签文件
        os.rename(src_img_path, dst_img_path)
        os.rename(src_label_path, dst_label_path)

        print(f"图片文件 '{img_file}' 重命名为 '{new_img_name}'")
        print(f"标签文件 '{base_name}.txt' 重命名为 '{new_label_name}'")

print("重命名完成！")
