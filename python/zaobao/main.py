import base64
import hashlib
import hmac
import os
import time
import urllib
import urllib.parse

import requests
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from jinja2 import Environment, select_autoescape, FileSystemLoader
from parsel import Selector


def daily_news():
    root_domain = 'https://www.zaobao.com'
    res = requests.get(root_domain, headers={
        'Connection': 'Keep - Alive',
        'User-Agent': 'Apache - HttpClient / 4.5.14(Java / 17.0.8)',
        'Accept-Encoding': 'br, deflate, gzip, x - gzip'
    })
    html = res.content.decode('utf-8')
    selector = Selector(text=html)
    titles = selector.xpath('//div[@class="rank-item"]//a')
    titles = titles[:5]
    return [{"href": f'{root_domain}{item.xpath("./@href").get()}', "title": item.xpath("./@title").get()} for item
            in
            titles]


def daily_image():
    # 获取图片
    res_bing = requests.get("https://cn.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1&mkt=zh-cn")
    res_bing = res_bing.json()
    img_url = "https://cn.bing.com" + res_bing['images'][0]['url']
    img_title = res_bing['images'][0]['title']
    img_copyright = res_bing['images'][0]['copyright']
    return {"url": img_url, "title": img_title, "copyright": img_copyright}


app = FastAPI(docs_url=None, redoc_url=None)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    authority = request.headers.get("authority")
    # 没有 authority 请求头 并且 不是 OPTIONS 则返回 403
    if not authority and request.method != "OPTIONS":
        return JSONResponse(status_code=403, content={"msg": "请提供authority"})
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time

    # X- 作为前缀代表专有自定义请求头
    response.headers["X-Process-Time"] = str(process_time)
    return response


def build_message(_type, msg):
    if _type == 'text':
        return {"msgtype": "text", "text": {"content": msg}}
    elif _type == 'markdown':
        return {
            "msgtype": "markdown",
            "markdown": {
                "title": "早报",
                "text": msg
            },
            "at": {
                "isAtAll": True
            }
        }


def build_markdown():
    env = Environment(
        loader=FileSystemLoader("templates"),
        autoescape=select_autoescape()
    )
    date = time.strftime("%Y年%m月%d日", time.localtime())
    template = env.get_template("daily.jinja")
    res = template.render(news_list=daily_news(), image=daily_image(), date=date)
    return res


def dingding_robot(msg):
    timestamp, sign = get_sign()
    url = f"https://oapi.dingtalk.com/robot/send?access_token={os.getenv('DINGDING_TOKEN')}&timestamp={timestamp}&sign={sign}"
    res = requests.post(url,
                        headers={"Content-Type": "application/json; charset=utf-8"},
                        json=msg)
    print(res.content.decode('utf-8'))


def get_sign():
    timestamp = str(round(time.time() * 1000))
    secret = os.getenv('DINGDING_SECRET')
    secret_enc = secret.encode('utf-8')
    string_to_sign = '{}\n{}'.format(timestamp, secret)
    string_to_sign_enc = string_to_sign.encode('utf-8')
    hmac_code = hmac.new(secret_enc, string_to_sign_enc, digestmod=hashlib.sha256).digest()
    sign = urllib.parse.quote_plus(base64.b64encode(hmac_code))
    return timestamp, sign


if __name__ == '__main__':
    print('Hello World!')
    dingding_robot(build_message('markdown', build_markdown()))
