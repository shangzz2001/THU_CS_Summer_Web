from cgi import test
from email import header
import imp
from time import sleep
from unittest import result
from urllib import response
import requests
from bs4 import BeautifulSoup as bs
import json
import re
from collections import defaultdict, OrderedDict
import json
import os
import time
import sqlite3
import fake_useragent
class JS_crawler:
    def __init__(self):
        # user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"
        # user_agent = fake_useragent.UserAgent().random
        self.headers = {'User-Agent': fake_useragent.UserAgent().random}
        cookie = '_uab_collina=166002750457757950766442; web_login_version=MTY2MjM4ODk4NA==--1d65d71599c072230cf859ea0395607843632db4; _m7e_session_core=1b78529f65f906accd5519fd1692ac7d; read_mode=day; default_font=font2; locale=zh-CN; sensorsdata2015jssdkcross={"distinct_id":"17c63de9bf3a60-05e7d57d8cf78f-1d3b6650-1296000-17c63de9bf4d8f","first_id":"","props":{"$latest_traffic_source_type":"直接流量","$latest_search_keyword":"未取到值_直接打开","$latest_referrer":"","$latest_utm_source":"desktop","$latest_utm_medium":"not-signed-in-collection-follow-button"},"$device_id":"17c63de9bf3a60-05e7d57d8cf78f-1d3b6650-1296000-17c63de9bf4d8f"}; acw_tc=0bcd4ce216626467254343461e014d264f111b20ecd4a36b80eb4fb9f6f396; acw_sc__v2=6319f9c58e3aacacb3f50c0bb2376b674c9ead43; acw_sc__v3=6319fa021f25314a8c015a2e5ebd55556683d10b; signin_redirect=https://www.jianshu.com/u/96287c50380a?u_atoken=35d76945-6b42-491a-b086-d0fa484613c8&u_asession=01g7XFrKVIQR2cOigA7fnZLPg8Cniz_btyu9t44QssBJrKoE_-1m6VZMDp_tu4wp7oX0KNBwm7Lovlpxjd_P_q4JsKWYrT3W_NKPr8w6oU7K9Fhqtth7bG9hMxPCQWqNMHzdjoMV1y19BFQvaXcOyBfmBkFo3NEHBv0PZUm6pbxQU&u_asig=05psoSHU7Wv6_f8KE1VSR9R7G2gstA-rn_WwmILeAP9uaqQVj_RI-Xm8eUk7miq7C26kKd7q7-uTC151RxG1S3jhFSZlcMlQmO_6n1qlnj_KMvJd_4CJs12LUY2VMd4lu2wppjLUyi7NbWER4Eqd_ru-N8P80u8ZGyarJxdGGMXvD9JS7q8ZD7Xtz2Ly-b0kmuyAKRFSVJkkdwVUnyHAIJzSXO537UWu2YaDrVeKs9JRT14wbOO4bIekZKeElKu0AKqBR97QLsOYcZJeUxi-_JXu3h9VXwMyh6PgyDIVSG1W_n4a08Q9_Pk5Kev2DaUJhQPHCVMK-skk_JH_PvuEFgfn-rhQJzR-2GdbO7siWtZ5unh2ycaYsWKfyHHwWvX-jNmWspDxyAEEo4kbsryBKb9Q&u_aref=ciYiSRGFuEY5PmyeGHrSa0Gep8w%3D; ssxmod_itna=YqUxnD0DuDcQKhDlRD+rFx9m5OTIDD5+f3qoKGC0DBL+r4iNDnD8x7YDvmf=4rmQD2DKYK2fA4QKb03P4eUWY+PxNjY+QqKoD84i7DKqibDCqD1D3qDkb4oxiigDCeDIDWeDiDG+OcLuuj0D0PD7oin7kNDm4GW4eDgDY=DIkNDAfL5xDfcDAt3uktYV4DBIrR04PGv3=6RjdXM3qGumjjntjcHwcGxLArFIqGyKI9cbqr4guN9Wz0KpihAIF4GKB=Kmf+iboxPlYY06BEKDfmQbrqKfDkUtyS=O7dGWiD==; ssxmod_itna2=YqUxnD0DuDcQKhDlRD+rFx9m5OTIDD5+f3qoKGCD8k6EDGNYqGaQOAsoGrAM=GxAp3ZKbq70tnQUk7fpqjarBG+aA2i7P4/mfPHXQ8an=eXpHL+iYUGBQ5mk0QnboWtyINvTqzApCO5sxaqCanFoZEcalO7=xZvhQbvGobA+qaeOS6eO065O43vvyco==rHb7t81pzoCj45OQoWfmtB6Nzd+6Knjrod87/dIrOmGe5jf48CW+ES24rCT=ykcK4a2pra97yqCKsP9Kxzy8oCgftUBLD07Lx08DY98YQDq37FPhWhDD==='.encode("utf-8").decode("latin1")
        self.cookies ={'Cookie': cookie}
        
    def get_passage_url(self, i):
        """_summary_
        有关url中type_id的说明, 经过查证, 对应关系如下
        27:后端技术 570
        28:Andriod 612
        29:IOS  594
        30:人工智能 491
        31:前端 550
        32:数据库 488
        33:程序开发 610
        """
        # url = "https://www.jianshu.com/programmers?page={i}&type_id=27&count=10".format(i=i)
        url = 'https://www.jianshu.com/c/22f2ca261b85?order_by=added_at&page={i}'.format(i = i)
        # 读取了该页面上的所有文章的概述
        response = requests.get(url = url, headers= self.headers,cookies=self.cookies)
        response.encoding = 'utf-8'
        test_json = json.loads(response.text)
        
        url_passage_set = []
        url_passage_base = 'https://www.jianshu.com/p/'
        url_user_set = []
        url_user_base = 'https://www.jianshu.com/u/'
        
        for i in range(len(test_json)):
            url_passage_new = url_passage_base+test_json[i]['slug']
            url_user_new = url_user_base+test_json[i]['user']['slug']
            url_passage_set +=[url_passage_new]
            url_user_set += [url_user_new]
        
        return url_passage_set, url_user_set
    
    def get_python_url(self, i = 1):
        print("正在爬取第", i ," 页内容 : ")
        url = 'https://www.jianshu.com/c/22f2ca261b85?order_by=added_at&page={i}'.format(i = i)
        # 读取了该页面上的所有文章的概述
        requests.session().keep_alive = False
        response = requests.get(url = url, headers= self.headers,cookies= self.cookies)
        response.encoding = 'utf-8'
        soup = bs(response.text, features="lxml")
        soup = bs(str(soup.find_all(id="list-container")), features="lxml")
        contents = soup.find_all(class_="content")
        articles_list = []
        url_base = 'https://www.jianshu.com'
        for article in contents:
            # 获得评论数
            comments_re = r'<i class="iconfont ic-list-comments"></i>\s*([\d]*)\s*'
            comments_re = re.compile(comments_re)
            comments_num = re.findall(comments_re,str(article))
            # 获得获赞数
            likes_re = r'<span><i class="iconfont ic-list-like"></i>\s*([\d]*)\s*</span>'
            likes_re = re.compile(likes_re)
            likes_num = re.findall(likes_re,str(article))
            # 获得标题
            res = r'<a\s*class="title"\s*href="([^"]*)"\s*target="_blank">(.*)</a>'
            res = re.compile(res)
            result = re.findall(res,str(article.a))
            # print(result[0][0])
            # print(result[0][1])
            try:
                passage_url = url_base + result[0][0]
                passage_title = result[0][1]
            except:
                print(article.a)
            # 获得摘要
            res = r'<p class="abstract">\s*(.*)\s*</p>'
            res = re.compile(res)
            result = re.findall(res,str(article.p))
            try:
                passage_abs = str(result[0]).replace('\n','')
            except:
                print(article.p)
            user_info = article.find_all(class_ = "nickname")
            # print(user_info[0])
            res = r'<a class="nickname" href="([^"]*)" target="_blank">([^"]*)</a>'
            res = re.compile(res)
            result = re.findall(res,str(user_info[0]))
            # print(result[0][0])
            user_name = result[0][1]
            user_homepage = url_base + result[0][0]
            info_dict = {}
            info_dict['passage_url'] = passage_url
            info_dict['passage_title'] = passage_title
            info_dict['passage_abs'] = passage_abs
            info_dict['user_name'] = user_name
            info_dict['user_homepage'] = user_homepage
            info_dict['comments'] = int(comments_num[0])
            info_dict['likes'] = int(likes_num[0])
            # print(info_dict)
            articles_list += [info_dict]
            
        return articles_list
    # 713 python
    # 1567 java
    def get_java_url(self, i = 1):
        print("正在爬取第", i ," 页内容 : ")
        url = 'https://www.jianshu.com/c/86ff829f995f?order_by=added_at&page={i}'.format(i = i)
        # 读取了该页面上的所有文章的概述
        requests.session().keep_alive = False
        response = requests.get(url = url, headers= self.headers,cookies= self.cookies)
        response.encoding = 'utf-8'
        soup = bs(response.text, features="lxml")
        soup = bs(str(soup.find_all(id="list-container")), features="lxml")
        contents = soup.find_all(class_="content")
        articles_list = []
        url_base = 'https://www.jianshu.com'
        for article in contents:
            # 获得评论数
            comments_re = r'<i class="iconfont ic-list-comments"></i>\s*([\d]*)\s*'
            comments_re = re.compile(comments_re)
            comments_num = re.findall(comments_re,str(article))
            # 获得获赞数
            likes_re = r'<span><i class="iconfont ic-list-like"></i>\s*([\d]*)\s*</span>'
            likes_re = re.compile(likes_re)
            likes_num = re.findall(likes_re,str(article))
            # 获得标题
            res = r'<a\s*class="title"\s*href="([^"]*)"\s*target="_blank">(.*)</a>'
            res = re.compile(res)
            result = re.findall(res,str(article.a))
            # print(result[0][0])
            # print(result[0][1])
            try:
                passage_url = url_base + result[0][0]
                passage_title = result[0][1]
            except:
                print(article.a)
            # 获得摘要
            res = r'<p class="abstract">\s*(.*)\s*</p>'
            res = re.compile(res)
            result = re.findall(res,str(article.p))
            try:
                passage_abs = str(result[0]).replace('\n','')
            except:
                print(article.p)
            user_info = article.find_all(class_ = "nickname")
            # print(user_info[0])
            res = r'<a class="nickname" href="([^"]*)" target="_blank">([^"]*)</a>'
            res = re.compile(res)
            result = re.findall(res,str(user_info[0]))
            # print(result[0][0])
            user_name = result[0][1]
            user_homepage = url_base + result[0][0]
            info_dict = {}
            info_dict['passage_url'] = passage_url
            info_dict['passage_title'] = passage_title
            info_dict['passage_abs'] = passage_abs
            info_dict['user_name'] = user_name
            info_dict['user_homepage'] = user_homepage
            info_dict['comments'] = int(comments_num[0])
            info_dict['likes'] = int(likes_num[0])
            # print(info_dict)
            articles_list += [info_dict]
            
        return articles_list
    
    def get_user_info(self, user_url):
        """
        调用方法, 传入用户主页的url, 返回用户信息dict
        内有：用户姓名，用户关注数、用户粉丝数、用户文章总字数、用户收获喜欢个数、用户总资产
        """
        user_information = {}
        print(user_url)
        response = requests.get(url = user_url,cookies=self.cookies,headers=self.headers)
        soup = bs(response.text, features = "lxml")
        res = r'<title>\s*([^"]*)\s-\s*简书</title>'
        name_re = re.compile(res)
        name = re.findall(name_re, str(soup.title))
        # print(name[0])
        user_information['name'] = name[0]
        user_info = soup.find_all(class_ = "info")
        # print(user_info)
        infos = bs(str(user_info), features="lxml")
        # print(infos)
        infos = infos.find_all(class_ = "meta-block")
        data_list = [] # 关注、粉丝、文章、字数、收获喜欢、总资产
        for info in infos:
            re_num = r'<p>([/d]*)'
            res = r'<p>([\d]*)</p'
            ret = re.compile(res)
            num = re.findall(ret, str(info.p))
            data_list += [num[0]]
            # print(info.p)
        user_information['关注'] = int(data_list[0])
        user_information['粉丝'] = int(data_list[1])
        user_information['文章'] = int(data_list[2])
        user_information['字数'] = int(data_list[0])
        user_information['收获喜欢'] = int(data_list[0])
        user_information['总资产'] = int(data_list[0])
        
        return user_information
        
    def crawl_passage(self, passage_url):
        print("正在爬取文章：", passage_url)
        info_dict = {}
        response = requests.get(url = passage_url, headers = self.headers, cookies = self.cookies)
        soup = bs(response.text,features='lxml')
        # print(soup.prettify())
        temp = soup.find(id == '__NEXT_DATA__',type == 'Application/json')
        text = str(temp)
        # 获得创建时间
        res = r'"first_shared_at":([\d]*),'
        reg = re.compile(res)
        result = re.findall(reg,text)
        info_dict['create_time'] = str(timestamp_convert_localdate(int(result[0])))
        # 获得浏览量
        res = r'"first_shared_at":{time},"views_count":([\d]*)'.format(time = str(result[0]))
        reg = re.compile(res)
        result = re.findall(reg,text)[0]
        print(result)
        info_dict['views'] = int(str(result))
        print(info_dict['views'])
        article = str(temp.body.article)
        img_boxs = temp.find_all(class_ = 'image-package')
        result_dir = './result/'
        if os.path.exists(result_dir) == False:
            os.makedirs(result_dir)
        article_dir_list = os.listdir(result_dir)
        new_article_dir = result_dir+str(len(article_dir_list)+1)
        os.mkdir(new_article_dir)
        for i, tp in enumerate(img_boxs):
            img = tp.find('div').find('img').get('data-original-src')
            img_url = 'http:' + str(img)
            img_save_path = new_article_dir + '/'+str(i+1)+'.png'
            self.save_img(img_url, img_save_path)
            article = article.replace(str(tp),normalize(str(len(article_dir_list)+1),str(i+1)))
        info_dict['body'] = article
        with open(new_article_dir+'/body.html','w') as f:
            f.write(article)
            
        return info_dict, new_article_dir
    
    def save_img(self,img_url, file_path=''):
        img = requests.get(img_url,headers=self.headers,cookies=self.cookies)
        byte = img.content
        f = open(file_path, 'wb')
        f.write(byte)
        print(file_path, '文件保存成功！')
        f.close()

def normalize(article_idx, img_idx):
    result = """
    <figure class="figure">
        <img src=/media/{article_idx}/{img_idx}.png class="figure-img img-fluid rounded" alt="...">
        <figcaption class="figure-caption">A caption for the above image.</figcaption>
    </figure>
    """.format(article_idx = article_idx, img_idx = img_idx)
    return result

def write_list_to_json(infos_list,file_dir):
    for info in infos_list:
        info_dict = {
        'version': "1.0",
        'results': infos_list,
        'explain': {
            'used': True,
            'details': "this is for josn test",
            }
        }
        file_name = file_dir + '/result.json'
        json_str = json.dumps(info_dict, indent=3, ensure_ascii=False)
        with open(file_name, 'w', encoding='utf-8') as f:
            f.write(json_str)
    
def timestamp_convert_localdate(timestamp,time_format="%Y/%m/%d %H:%M:%S"):
    # 按照当前设备时区来进行转换，比如当前北京时间UTC+8
    timeArray = time.localtime(timestamp)
    styleTime = time.strftime(str(time_format), timeArray)
    return styleTime

def get_tag(title):
    if title.upper().find('PYTHON')>=0:
        return 'python'
    elif title.upper().find('JAVASCRIPT')>=0:
        return 'js'
    elif title.upper().find('JAVA')>=0:
        return 'java'
    elif title.upper().find('C++')>=0:
        return 'cplus'
    elif title.upper().find('SQL')>=0:
        return 'sql'
    elif title.upper().find('PHP')>=0:
        return 'php'
    elif title.upper().find('C#')>=0:
        return 'csharp'
    else:
        return 'else'

def read_and_write(pagenum=1):
    l = a.get_java_url(pagenum)
    for i in range(len(l)):
        user_info = a.get_user_info(l[i]['user_homepage'])
        info_dict,file_dir = a.crawl_passage(l[i]['passage_url'])
        info_dict.update(l[i])
        info_dict['user_info'] = user_info
        info_dict['tag'] = get_tag(info_dict['passage_title'])
        write_list_to_json(info_dict,file_dir=file_dir)
        # write_to_sqlite(info_dict)
        sleep(2)
    
def write_to_sqlite(info):
    sql = ''' insert into article_articlepost
            (title, body, comments, create_time, favors, likes,passage_url, pre_id, tag, abs, author_id)
        values
              (:title, :body, :comments, :create_time, :favors, :likes, :passage_url, :pre_id, :tag, :abs, :author_id)'''
    cursor.execute(sql,{'title':info['passage_title'], 'body':info['body'], 'comments':info['comments'], 'create_time':info['create_time'], 'favors':0, 'likes':info['likes'], 'passage_url':info['passage_url'], 'pre_id':info['user_name'], 'tag': info['tag'], 'abs':info['passage_abs'], 'author_id':1})
    conn.commit()

if __name__ == "__main__":
    a = JS_crawler()
    conn = sqlite3.connect("db.sqlite3")
    cursor = conn.cursor()
    cursor.close()
    for i in range(131,140):
        read_and_write(i)
    # l = a.get_python_url()
    # for i in range(len(l)):
    #     info_dict,file_dir = a.crawl_passage(l[i]['passage_url'])
    #     info_dict.update(l[i])
    #     user_info = a.get_user_info(info_dict['user_homepage'])
    #     info_dict['user_info'] = user_info
    #     info_dict['tag'] = get_tag(info_dict['passage_title'])
    #     write_list_to_json(info_dict,file_dir=file_dir)
    #     sleep(1)
        
    
    