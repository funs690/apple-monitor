from os import replace
import requests
import json
import time
import logging

# 请求信息
endponit = "https://www.apple.com.cn/shop/fulfillment-messages"
pl=True
location = "浙江 杭州 萧山区"

# 设备信号
black_256 = "MLT93CH/A"
white_256 = "MLTC3CH/A"
blue_256 = "MLT83CH/A"
golden_256 = "MLTD3CH/A"
mx_black_256 = "MLH83CH/A"
mx_white_256 = "MLH93CH/A"
mx_blue_256 = "MLHC3CH/A"
mx_golden_256 = "MLHA3CH/A"

# 封装参数
params = {
    "pl": pl,
    "location":location,
    "parts.0": black_256,
    "parts.1":white_256,
    "parts.2":blue_256,
    "parts.3":golden_256,
    "parts.4":mx_black_256,
    "parts.5":mx_white_256,
    "parts.6":mx_blue_256,
    "parts.7":mx_golden_256
}

hangzhou_wanxiang = "R532"
hangzhou_xihu = "R471"

split_symbol_line = "####################################################################################\n"
split_store_line = "#################################"
split_new_line = ""
split_blank_line = " \n"

log_path = "../logs/"

def get_goods_info():
    # 请求调用
    response = requests.get(url=endponit, params=params)
    # 注释日志数据打印
    # logging.info("response : " + response.text)
    # 加载json
    goods_info = json.loads(response.text)
    # 获取门店信息
    body = goods_info["body"]
    content = body["content"]
    pickupMessage = content["pickupMessage"]
    stores = pickupMessage["stores"]
    # 门店信息解析
    file_name = time.strftime("%Y-%m-%d-%H", time.localtime())
    file = open(log_path + file_name + '.log', 'a', encoding="utf-8")
    # 遍历门店信息
    file.write(split_symbol_line)
    file.write(split_store_line)
    file.write(split_new_line)
    file.write(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + "\n")
    file.write(split_store_line)
    file.write(split_blank_line)
    for store in stores :
        if store["storeNumber"] != hangzhou_wanxiang and store["storeNumber"] != hangzhou_xihu:
            continue
        file.write(split_store_line)
        file.write(store["storeName"] + split_blank_line)
        file.write(split_store_line)
        partsAvailability  = store["partsAvailability"]
        for item in partsAvailability:
            value = partsAvailability[item]
            message = value["storePickupProductTitle"] + " "
            if value["storeSelectionEnabled"] == True :
                message = message + "有货"
            else:
                message = message + "无货"
            file.write(message + split_blank_line)
        file.write(split_blank_line)
        file.write(split_store_line)
        file.write(split_blank_line)
    file.write(split_symbol_line)




