import os
import requests
import json
import fake_useragent
import re
from bs4 import BeautifulSoup as bs
import time
from time import sleep
headers = {'User-Agent': fake_useragent.UserAgent().random}
cookie = '_uab_collina=166002750457757950766442; web_login_version=MTY2MjM4ODk4NA==--1d65d71599c072230cf859ea0395607843632db4; _m7e_session_core=1b78529f65f906accd5519fd1692ac7d; read_mode=day; default_font=font2; locale=zh-CN; sensorsdata2015jssdkcross={"distinct_id":"17c63de9bf3a60-05e7d57d8cf78f-1d3b6650-1296000-17c63de9bf4d8f","first_id":"","props":{"$latest_traffic_source_type":"直接流量","$latest_search_keyword":"未取到值_直接打开","$latest_referrer":"","$latest_utm_source":"desktop","$latest_utm_medium":"not-signed-in-collection-follow-button"},"$device_id":"17c63de9bf3a60-05e7d57d8cf78f-1d3b6650-1296000-17c63de9bf4d8f"}; acw_sc__v2=631a29eac8961375abb1d5a5d111fc2d7017949b; acw_tc=0bcd4ce216626610218941629e0145e66046abaec1f3778c95c8c72a508e69; acw_sc__v3=631a31a1ab3ddad873642212fdc74578ede846ea; signin_redirect=https://www.jianshu.com/u/96287c50380a?u_atoken=fe86ac3a-7c88-4d26-81cb-545bd4e427c6&u_asession=0169jGHQKhLaoGH8IU7PqFJ7SuaSIuu3fXLDrT8vQh-iAagoAyBhzBhg6Q6Jqa1BH4X0KNBwm7Lovlpxjd_P_q4JsKWYrT3W_NKPr8w6oU7K-oFiHHO1YChTwN5C6ydLz4zdjoMV1y19BFQvaXcOyBfmBkFo3NEHBv0PZUm6pbxQU&u_asig=05oMTEtiyDfGac8z8D-HX9RyUWmj_psBgS7bLDdp2Vmr9olWVz-Zq6_IlHJ96FqrwcvulrSTAc48Jex4wIE-0Oej4dDiHGhE5pLGoxcywQXvOPzEoA3fb51z6yZrQXVgMOLZy4XYbu_OPGgNp2hb3UK61LKdHfAy4ec6Ez5HBy0cn9JS7q8ZD7Xtz2Ly-b0kmuyAKRFSVJkkdwVUnyHAIJzZa56_PyoTF195Q0lNPVwRHvf9hx90iuLKf2lTgCm1N9qBR97QLsOYcZJeUxi-_JXu3h9VXwMyh6PgyDIVSG1W9IwlPYKu2GOXY33-NFbJhxSCSeVzKmqAxYi4JZf_7kSOGhbkepW0ElgdbHzohe9npTA_hfBW0-KVuiPMypjvekmWspDxyAEEo4kbsryBKb9Q&u_aref=GAqDKEV0CvsaGSuUJeCXqAH%2FYfc%3D; ssxmod_itna=Qq0xyD9QiQdYu0xl4iubUiYvzxG2xAK4mio+LPD/FQxnqD=GFDK40ooO34No50iztA3BDQWABrPGClAC2DqeWpG+3re=1xiTD4q07Db4GkDAqiOD7MmeDxOq0rD74irDDxD3mrv9tgXDB4DjBvOfh5Dbxi3/xGCDmKDuh5DW6PwDDa8DWHm9xHw1xDC0lBHz40T+z97uO51wx0ONt9Oef3LUbxGdAA30x0kD5k8va7Gg6v85qA+bQGbidrNtiGeh04qejWbqGDP/B6P==ii7m2bOeRqFsrNUwEWTVjDD; ssxmod_itna2=Qq0xyD9QiQdYu0xl4iubUiYvzxG2xAK4mio+PG9bu4xBkODhD7PrNSFHGFCjAyxYvPgQ0dmxGOj=Gy4qWDboWtNlYBDYmCx1Sh7XjdACPlRPeBO0Q2vlAm1H6QXwvm/UPxpIqhTfMeP8XEWrlQihdl4tBBKrBQiTYiTwKZh=KUnzqSG74SvQ9Qo1qiP5KtiWqWEdWmnWOtfjUmD=YCvrhGYPugytL+7G=fydMGGOW=KN14nm/UpCnmF7DpnnMPAnt=gtocazDFwrgPp2nl1q=L1z7XO2Ek/qzxeamcwOqMW=4rT2tGVS0FWi5yf2nDe+UKibYNeBS35quFzFH0RRn4KrIFCRYhS2S9BqH7tF0hnbVFIoX73dgX4E5VKyKPokge6HQ1gDM7exWWtYZRhZDWZB2=5viE2BfBYX+bYRM3ny35anYsWOnK57j73D07FxDLxD2jRHCG5YTqYGDD=='
cookie = cookie.encode("utf-8").decode("latin1")
cookies ={'Cookie': cookie}

def save_user_img(user_url, user_name, file_path='/Users/shangzizhi/CodeManager/MyPython/Django/helloworld/media/user_img/'):
    response = requests.get(url = user_url,cookies=cookies,headers=headers)
    # print(response.text)
    soup = bs(response.text, features = "lxml")
    # r'<i class="iconfont ic-list-comments"></i>\s*([\d]*)\s*'
    res = r'src="(https://upload.jianshu.io/users/([^"]*))'
    res =re.compile(res)
    # print(res)
    # print(str(soup))
    img_url = re.findall(res,str(soup))
    try:
        a = img_url[0][0]
    except:
        print('using default pic')
        return "/media/user_img/"+'default'+'.png'
    # print(img_url[0][0])
    save_img(img_url[0][0],file_path+user_name+'.png')
    return "/media/user_img/"+user_name+'.png'
    
def save_img(img_url, file_path=''):
    img = requests.get(img_url,headers=headers,cookies=cookies)
    byte = img.content
    f = open(file_path, 'wb')
    f.write(byte)
    print(file_path, '文件保存成功！')
    f.close()
    
pre_dataset = os.listdir('./result')

url_list = []
for i in range(4733,len(pre_dataset)):
    current_data_dir = './result/'+pre_dataset[i]
    current_html_dir = current_data_dir+'/body.html'
    result_json_dir = current_data_dir + '/result.json'
    target_json_dir = './result/' +pre_dataset[i] + '/result.json'
    if os.path.exists(result_json_dir) :
        with open(result_json_dir, 'r') as f:
            result_json = json.load(f)
            # print(result)
            result = result_json.get('results')
            url = result['passage_url']
            if url in url_list :
                # print("重复")
                continue
            else:
                url_list += [result['passage_url']]
                if result['body'] == 'None':
                    print(result_json)
                    print(None)
                    pass
                else:
                        print(i," : ",pre_dataset[i])
                        result_json['results']['user_img']= save_user_img(result_json['results']['user_homepage'],result_json['results']['user_name'])
                        result_json = json.dumps(result_json, indent=3, ensure_ascii=False)
                        with open(target_json_dir, 'w', encoding='utf-8') as f:
                            f.write(result_json)
                        sleep(0.5)
    