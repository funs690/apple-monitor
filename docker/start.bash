cp ../requirements.txt ./requirements.txt;
docker build -t apple/goods . ;
docker run -d --name apple \
    -v /home/apple/bin:/home/apple/bin \
    -v /home/apple/logs:/home/apple/logs \
    apple/goods;