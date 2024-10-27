#!/bin/bash

# 定义训练命令列表
commands=(
    # "python val.py"
    "python heatmap.py"
    "python heatmap.py"
)

# 日志文件
logfile="error_log.txt"

# 清空日志文件
> $logfile

# 遍历并执行每个训练命令
for cmd in "${commands[@]}"
do
    echo "执行命令: $cmd"
    
    # 执行命令并捕获错误输出
    $cmd 2>> $logfile
    
    # 检查命令是否成功执行
    if [ $? -ne 0 ]; then
        echo "命令失败，错误已记录到 $logfile"
    else
        echo "命令成功执行"
    fi
    
    # 停止 20 s
    echo "暂停 20 s ..."
    sleep 20
done

echo "所有命令已执行完毕"