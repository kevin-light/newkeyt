from EmQuantAPI import *
from datetime import timedelta, datetime


def startCallback(message):
    print("[EmQuantAPI Python]", message)
    return 1

def csqQuoteCallback(quantdata):
    """
    DemoCallback 是EM_CSQ订阅时提供的回调函数模板。该函数只有一个为c.EmQuantData类型的参数quantdata
    :param quantdata:c.EmQuantData
    :return:
    """
    print ("csqQuoteCallback111,", str(quantdata))
    quant = quantdata.Data
    print('222',type(quant))
    for key,val in quant.items():
        code = key
        print(code,val)
        for index in val:
            indicator = index
            # print(code,indicator)


# def demoQuoteCallback(quantdata):
#     """
#     DemoCallback 是EM_CSQ订阅时提供的回调函数模板。该函数只有一个为c.EmQuantData类型的参数quantdata
#     :param quantdata:c.EmQuantData
#     :return:
#     """
#     for i in range(0, len(quantdata.Codes)):
#         length = len(quantdata.Dates)
#         for it in quantdata.Data.keys():
#             print(it.decode(c_encodeType))
#             for k in range(0, length):
#                 for j in range(0, len(quantdata.Indicators)):
#                     print(quantdata.Data[it][j * length + k], " ",end = "")
#                 print()

# 调用登录函数（激活后使用，不需要用户名密码）
loginResult = c.start("ForceLogin=1")

if (loginResult.ErrorCode != 0):
    print("login in fail")
    exit()


# #实时行情订阅使用范例
# data = c.csq('000850.SH', 'TIME,Now,Volume','Pushtype=1')
# if data.ErrorCode != 0:
#     print("request csq Error, ", data.ErrorMsg)
# else:
#     print("csq输出结果======分隔线======")
#     text = input("press any key to cancel csq \r\n")
#     #取消订阅
#     data = c.csqcancel(data.SerialID)

# data=c.csq("600000.SH,600090.SH,600083.SH,600086.SH,600091.SH,600099.SH","Time,Now,High,Low,Open,PreClose,","Pushtype=1",fncallback=csqQuoteCallback,)

def csquantData():

    data=c.csq("00001.HK,00002.HK,00003.HK","Time,Now,High,Low,Open,PreClose,","Pushtype=1",fncallback=csqQuoteCallback)

    if data.ErrorCode != 0:
        print("request csq Error, ", data.ErrorMsg)
    else:
        print("csq输出结果======分隔线======")
        text = input("press any key to cancel csq \r\n")
        #取消订阅
        #data = c.csqcancel(data.SerialID)

    # 退出
    data = logoutResult = c.stop()
    print('ok',data)


if __name__ == '__main__':

    csquantData()
