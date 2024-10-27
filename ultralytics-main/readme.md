# ultralytics版本版本8.2.50
# 我的实验环境:
    python: 3.8.18
    torch:  1.12.0+cu113
    torchvision: 0.13.0+cu113
    timm: 0.9.8                 
    mmcv: 2.1.0                
    mmengine: 0.9.0 
    numpy : 1.22.3

# 在上述环境下，脚本均可直接运行
1. train.py：训练模型的脚本
2. main_profile.py：输出模型和模型每一层的参数,计算量的脚本
3. val.py：使用训练好的模型计算指标
4. detect.py：模型推理
5. get_COCO_metrice.py：计算COCO指标的脚本
6. get_FPS.py：计算模型储存大小、模型推理时间、FPS的脚本