# 加载基础镜像
FROM python:3.9-alpine

# 文件复制(使用挂在方式加载数据)
# COPY mian.py /home/apple
# COPY goods.py /home/apple
COPY requirements.txt /home/apple/

WORKDIR /home/apple/bin/

# 安装依赖
RUN pip install -r /home/apple/requirements.txt

#定义时区参数
ENV TZ=Asia/Shanghai
#设置时区
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime \
    && echo '$TZ' > /etc/timezone

#运行日志应用
ENTRYPOINT ["python3", "/home/apple/bin/main.py"]