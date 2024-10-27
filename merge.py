import os
import shutil

def copy_images_and_labels(src_image_folder, src_label_folder, dst_image_folder, dst_label_folder):
    # 确保目标目录存在
    os.makedirs(dst_image_folder, exist_ok=True)
    os.makedirs(dst_label_folder, exist_ok=True)

    # 获取源目录中的所有图片文件
    image_files = os.listdir(src_image_folder)

    # 遍历图片文件
    for image_file in image_files:
        src_image_path = os.path.join(src_image_folder, image_file)
        dst_image_path = os.path.join(dst_image_folder, image_file)

        # 检查目标目录中是否已存在同名图片文件
        if os.path.exists(dst_image_path):
            print(f"图片文件 {image_file} 已存在，跳过复制。")
        else:
            # 复制图片文件到目标目录
            shutil.copy(src_image_path, dst_image_path)
            # print(f"复制图片文件 {image_file} 到 {dst_image_folder}")

    # 获取源目录中的所有标签文件
    label_files = os.listdir(src_label_folder)

    # 遍历标签文件
    for label_file in label_files:
        src_label_path = os.path.join(src_label_folder, label_file)
        dst_label_path = os.path.join(dst_label_folder, label_file)

        # 检查目标目录中是否已存在同名标签文件
        if os.path.exists(dst_label_path):
            print(f"标签文件 {label_file} 已存在，追加内容。")
            # 追加标签文件内容
            with open(src_label_path, 'r') as src_label:
                src_content = src_label.read()
            with open(dst_label_path, 'a') as dst_label:
                # dst_label.write("\n")  # 添加换行符以分隔内容
                dst_label.write(src_content)
            print(f"已将 {label_file} 内容追加到目标文件。")
        else:
            # 复制标签文件到目标目录
            shutil.copy(src_label_path, dst_label_path)
            # print(f"复制标签文件 {label_file} 到 {dst_label_folder}")


src_image_folder_1 = '/home/lenovo/data/liujiaji/Oildata/Well/Well lost/image'  # 第一个图片文件夹
src_label_folder_1 = '/home/lenovo/data/liujiaji/Oildata/Well/Well lost/label1'  # 第一个标签文件夹

src_image_folder_2 = '/home/lenovo/data/liujiaji/Oildata/Well/Well normal/image'  # 第二个图片文件夹
src_label_folder_2 = '/home/lenovo/data/liujiaji/Oildata/Well/Well normal/label1'  # 第二个标签文件夹

src_image_folder_3 = '/home/lenovo/data/liujiaji/Oildata/Well/Well with man:car/image'  # 第二个图片文件夹
src_label_folder_3 = '/home/lenovo/data/liujiaji/Oildata/Well/Well with man:car/label1'  # 第二个标签文件夹

src_image_folder_4 = '/home/lenovo/data/liujiaji/Oildata/Warning-Stacks/image'  # 第二个图片文件夹
src_label_folder_4 = '/home/lenovo/data/liujiaji/Oildata/Warning-Stacks/label1'  # 第二个标签文件夹

src_image_folder_5 = '/home/lenovo/data/liujiaji/Oildata/Pointer/Pointer-abnormal/sourceimage'  # 第二个图片文件夹
src_label_folder_5 = '/home/lenovo/data/liujiaji/Oildata/Pointer/Pointer-abnormal/label1'  # 第二个标签文件夹

src_image_folder_6 = '/home/lenovo/data/liujiaji/Oildata/Pointer/Pointer-normal/sourceimage'  # 第二个图片文件夹
src_label_folder_6 = '/home/lenovo/data/liujiaji/Oildata/Pointer/Pointer-normal/label1'  # 第二个标签文件夹


dst_image_folder = '/home/lenovo/data/liujiaji/Oildata/allimage1'  # 目标图片文件夹
dst_label_folder = '/home/lenovo/data/liujiaji/Oildata/alllabel1'  # 目标标签文件夹

# 复制文件夹中的图片和标签
# copy_images_and_labels(src_image_folder_1, src_label_folder_1, dst_image_folder, dst_label_folder)
# copy_images_and_labels(src_image_folder_2, src_label_folder_2, dst_image_folder, dst_label_folder)
# copy_images_and_labels(src_image_folder_3, src_label_folder_3, dst_image_folder, dst_label_folder)
# copy_images_and_labels(src_image_folder_4, src_label_folder_4, dst_image_folder, dst_label_folder)
copy_images_and_labels(src_image_folder_5, src_label_folder_5, dst_image_folder, dst_label_folder)
copy_images_and_labels(src_image_folder_6, src_label_folder_6, dst_image_folder, dst_label_folder)


# 使用isfile函数过滤出文件，并获取文件数量
src_img_1 = len([f for f in os.listdir(src_image_folder_1) if os.path.isfile(os.path.join(src_image_folder_1, f))])
src_lab_1 = len([f for f in os.listdir(src_label_folder_1) if os.path.isfile(os.path.join(src_label_folder_1, f))])

src_img_2 = len([f for f in os.listdir(src_image_folder_2) if os.path.isfile(os.path.join(src_image_folder_2, f))])
src_lab_2 = len([f for f in os.listdir(src_label_folder_2) if os.path.isfile(os.path.join(src_label_folder_2, f))])

src_img_3 = len([f for f in os.listdir(src_image_folder_3) if os.path.isfile(os.path.join(src_image_folder_3, f))])
src_lab_3 = len([f for f in os.listdir(src_label_folder_3) if os.path.isfile(os.path.join(src_label_folder_3, f))])

src_img_4 = len([f for f in os.listdir(src_image_folder_4) if os.path.isfile(os.path.join(src_image_folder_4, f))])
src_lab_4 = len([f for f in os.listdir(src_label_folder_4) if os.path.isfile(os.path.join(src_label_folder_4, f))])

src_img_5 = len([f for f in os.listdir(src_image_folder_5) if os.path.isfile(os.path.join(src_image_folder_5, f))])
src_lab_5 = len([f for f in os.listdir(src_label_folder_5) if os.path.isfile(os.path.join(src_label_folder_5, f))])

src_img_6 = len([f for f in os.listdir(src_image_folder_6) if os.path.isfile(os.path.join(src_image_folder_6, f))])
src_lab_6 = len([f for f in os.listdir(src_label_folder_6) if os.path.isfile(os.path.join(src_label_folder_6, f))])


all_img = len([f for f in os.listdir(dst_image_folder) if os.path.isfile(os.path.join(dst_image_folder, f))])
all_lab = len([f for f in os.listdir(dst_label_folder) if os.path.isfile(os.path.join(dst_label_folder, f))])

 
print(
    "well normal 数量为:", src_img_2,src_lab_2,
    "well lost 数量为:", src_img_1,src_lab_1,
    "well with man:car 数量为:", src_img_3,src_lab_3,

    "warning-stacks 数量为:", src_img_4,src_lab_4,

    "Pointer abnormal 数量为:", src_img_5,src_lab_5,
    "Pointer normal 数量为:", src_img_6,src_lab_6,

    "所有文件数量为:", all_img,all_lab,

)
