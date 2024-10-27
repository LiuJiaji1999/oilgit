#### oilgit

##### 记录华北油田的训练进度
```text 
2024.10.27：移植到github下的public，随时更新下载；

```


##### 常见问题解决
- 查看运行进行

        nvidia-smi
        ps aux | grep python 
        kill -9 进程号

- 提示：设备上没有空间

        df -h
        # lsof | grep delete 最好不要用
        # kill -9 进程号  最好不要用
        du -h -x --max-depth=1  #查看文件夹大小
        cd /home #逐级查看
