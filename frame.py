import cv2
import os

def extract_frames(video_path, output_folder, frame_interval):
    # 打开视频文件
    video_capture = cv2.VideoCapture(video_path)

    # 检查视频是否成功打开
    if not video_capture.isOpened():
        print(f"无法打开视频文件: {video_path}")
        return

    # 获取视频的帧率
    fps = int(video_capture.get(cv2.CAP_PROP_FPS))
    print(f"视频帧率: {fps}帧/秒")

    # 确保输出目录存在
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    frame_count = 0
    saved_frame_count = 0

    while True:
        # 读取下一帧
        ret, frame = video_capture.read()

        if not ret:
            break  # 如果没有更多帧，退出循环

        # 判断是否保存该帧（根据设定的抽帧间隔）
        if frame_count % frame_interval == 0:
            frame_filename = os.path.join(output_folder, f"frame_{saved_frame_count:04d}.jpg")
            # cv2.imwrite(frame_filename, frame)  # 保存帧为图片
            # print(f"保存帧: {frame_filename}")
            saved_frame_count += 1

        frame_count += 1

    # 释放视频资源
    video_capture.release()
    print(f"视频处理完成，共保存了{saved_frame_count}帧")

# 使用示例
video_path = "/home/lenovo/data/liujiaji/Oildata/DJI_20240926150333_0001_S.MP4"  # 输入视频文件路径
output_folder = "output_frames"  # 保存抽取帧的输出文件夹
frame_interval = 1  # 每隔多少帧保存一张

extract_frames(video_path, output_folder, frame_interval)
