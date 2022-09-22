# -*- coding:utf-8 -*-
import requests, json
from time import time
from datetime import date 

print(datetime.datetime.now())
#登錄URL
login_url = 'https://app.culr.edu.cn/uc/wap/login?redirect=https%3A%2F%2Fapp.culr.edu.cn%2Fncov%2Fwap%2Fdefault%2Findex'
#身份驗證URL
check_url = 'http://app.culr.edu.cn/uc/wap/login/check'
#身份驗證通過，重定向URL
redirect_url = 'https://app.culr.edu.cn/ncov/wap/default/index'
#表單提交URL
save_url = 'https://app.culr.edu.cn/ncov/wap/default/save'
#僞裝瀏覽器類型
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'}

info = {
    #所在地信息（省+市+区（县） 或 直辖市+区，其间需要插入一个空格）
    #例如 '江苏省 苏州市 姑苏区'
    'area': "江苏省 苏州市 姑苏区",          # 打卡位置（省市區以空格分隔）
    'bztcyy': "",                          # 不和前一天同城原因
    'province': "江苏省",                   # 所在省份
    'city': "苏州市",                       # 所在城市     
    'created': '',                         # 时间戳
    'csmjry': "0",                         # 近14日内本人/共同居住者是否去过疫情发生场所
    'date': "",                            # 打卡日期
    'zgfxdq': "0",                         # 今日是否在中高风险地区？
    'jcjgqr': "0",                         # 正常（0）疑似感染（1）确诊感染（2）其他（3）
    'tw': "2",                             # 今日体温范围（2表示第二個選項）
    'szsqsfybl': 0,                        # 所在社区是否有确诊病例
    'sfzx': "0",                           # 是否在校
    'sfjcbh': "0",                         # 今日是否接触无症状感染/疑似/确诊人群？
    'mjry': "0",                           # 今日是否接触密接人员？
    'sfcxtz': "0",                         # 今日是否出现发热、乏力、干咳、呼吸困难等症状？
    'sfcxzysx': "0",                       # 是否有任何与疫情相关的， 值得注意的情况？
    'sfcyglq': "0",                        # 是否处于观察期？
    #以上爲關鍵信息，
    'glksrq': "",                            
    'gllx': "",
    'address': "",
    'gtjzzfjsj': "",                         
    'gwszdd': "",
    'id': 2511960,
    'ismoved': 0,
    'jcbhlx': "",
    'jcbhrq': "",
    'jchbryfs': "",
    'jcjg': "",
    'jcqzrq': "",
    'jcwhryfs': "",
    'jhfjhbcc': "",
    'jhfjjtgj': "",
    'jhfjrq': "",
    'jrsfqzfy': "",
    'jrsfqzys': "",
    'qksm': "",
    'remark': "",
    'sfjchbry': "0",
    'sfjcqz': "",
    'sfjcwhry': "0",
    'sfsfbh': 0,
    'sfsqhzjkk': 0,
    'sftjhb': "0",
    'sftjwh': "0",
    'sfxk': 0,
    'sfygtjzzfj': 0,
    'sfyqjzgc': "",
    'sfyyjc': "0",
    'sqhzjkkys': "",
    'szgj': "",
    'uid': "46144",
    'xjzd': "",
    'xkqq': ""
}
    
#打卡时间信息更新
info['date'] = str(date.today()).replace('-', '')
info['created'] = str(round(time()))

#學號和密碼
username = ''
password = ''

login_data = {'username': username, 'password': password}
#創建會話
session = requests.Session()
#登錄驗證
chk_res = session.post(url=check_url, data=login_data, headers=headers)

chk_result_dict = json.loads(chk_res.text)
if chk_result_dict['e']==0:
    
    print('[身份信息验证:]',chk_result_dict['m'])
    
    session.get(url=redirect_url, headers=headers)

    resp = session.post(url=save_url, data=info, headers=headers)

    print('[學號:]', username)

    print('[打卡位置]:{0}\n[是否在校]:{1}'.format(info['area'], '是' if info['sfzx'] != '0' else '否'))

    print('[時間:]', date.today())
    
    punch_result_dict = json.loads(resp.text)
    
    print('[結果:]',punch_result_dict['m'])
    
else:
    print('[学号，密码]验证失败!')

