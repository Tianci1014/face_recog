import urllib.request
import urllib
warningtime = 0

# md5加密
def md5(str):
    import hashlib
    m = hashlib.md5()
    m.update(str.encode("utf8"))
    return m.hexdigest()
#
# 短信反馈
statusStr = {
    # 相当于一个数据字典，目的是把返回的代码翻译成相应的错误类型告诉你
    '0': '短信发送成功',
    '-1': '参数不全',
    '-2': '服务器空间不支持,请确认支持curl或者fsocket，联系您的空间商解决或更换空间',
    '30': '密码错误',
    '40': '账号不存在',
    '41': '余额不足',
    '42': '账户已过期',
    '43': 'IP地址限制',
    '50': '内容含有敏感词'
}


# 警报模块
def warning():
    smsapi = "http://api.smsbao.com/"
    # 短信平台账号
    user = 'wqeqeqwe'
    # 短信平台密码
    password = md5('Ctc031014')  # 密码需要用md5加密
    # 要发送短信的内容
    content = '欢迎您使用树莓派人工智能会议室管理系统'
    # 要发送短信的手机号码
    phone = '18828627350'

    data = urllib.parse.urlencode({'u': user, 'p': password, 'm': phone, 'c': content})
    send_url = smsapi + 'sms?' + data
    response = urllib.request.urlopen(send_url)
    the_page = response.read().decode('utf-8')
    print(statusStr[the_page])  # 输出短信反馈的具体信息

warning()