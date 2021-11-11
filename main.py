import goods
import schedule
import logging

LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
logging.basicConfig(filename='system.log', level=logging.DEBUG, format=LOG_FORMAT)

# 定义函数
def get_goods_info_job() :
    logging.info("=================task start ...============")
    goods.get_goods_info()
    logging.info("=================task end ...============")

# 程序主入口
def main():
    
    # 1分钟进行一次
    schedule.every(1).minutes.do(get_goods_info_job)
    while True:
        schedule.run_pending()

if __name__ == '__main__':
    main()