import requests

def massge_to_xf():
    url = 'http://eip.hnx.ctc.com/ims/portalapp/sms_send.app'
    mydatas = 'businessId=1102&idCard=13342573355'
    # mydatas = 'businessId=1102&idCard=13342570991'
    headers = {
        'x-requested-with': 'XMLHttpRequest',
        'Accept-Language': 'zh-CN',
        'Referer': 'http://eip.hnx.ctc.com/###',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Accept-Encoding': 'gzip, deflate',
        'User-Agent': 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET4.0C; .NET4.0E; InfoPath.2)',
        'Host': 'eip.hnx.ctc.com',
        'Content-Length': '34',
        'Pragma': 'no-cache',
        'Cookie': 'PD-H-SESSION-ID=1_4_0_t00F6aF0NrWYzWS5bEvYE9aogxFZdSUNtLFw9LvARQGcgswn; ,JSESSIONID=0000HL2gbSLhHLSU69yRZMHSpBd:1ar0dcrji',
        'Connection': 'close',
    }
    response = requests.post(url, data=mydatas, headers=headers)
    if '"success":true' in response.text:
        print('短信发送成功!')
    else:
        print('短信发送失败!!!!!!')

massge_to_xf()


