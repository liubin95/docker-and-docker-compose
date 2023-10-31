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
from loguru import logger
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
    res = [{"href": f'{root_domain}{item.xpath("./@href").get()}', "title": item.xpath("./@title").get()} for item
           in
           titles]
    logger.debug("daily_news {}", res)
    return res


def daily_image():
    # 获取图片
    res_bing = requests.get("https://cn.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1&mkt=zh-cn")
    res_bing = res_bing.json()
    img_url = "https://cn.bing.com" + res_bing['images'][0]['url']
    img_title = res_bing['images'][0]['title']
    img_copyright = res_bing['images'][0]['copyright']
    res = {"url": img_url, "title": img_title, "copyright": img_copyright}
    logger.debug("daily_image {}", res)
    return res


def daily_clause():
    date = time.strftime("%Y-%m-%d", time.localtime())
    url = f'https://web.shanbay.com/opp/quotes/{date}'
    res = requests.get(url)
    html = res.content.decode('utf-8')
    selector = Selector(text=html)
    content = selector.xpath('//p[@class="content"]/text()').get()
    translation = selector.xpath('//p[@class="translation"]/text()').get()
    res = {"content": content, "translation": translation}
    logger.debug("daily_clause {}", res)
    return res


def daily_weather():
    # beijing dalian
    city_list = [{'id': '101010100', 'name': '北京市', 'content': []},
                 {'id': '101070201', 'name': '大连市', 'content': []}]
    _key = os.getenv('QWEATHER_KEY')
    for item in city_list:
        _res = requests.get(f"https://devapi.qweather.com/v7/weather/now?key={_key}&location={item['id']}")
        _json = _res.json()
        fx_link = _json['fxLink']
        feels_like = _json['now']['feelsLike']
        res = requests.get(fx_link)
        html = res.content.decode('utf-8')
        selector = Selector(text=html)
        abstract = selector.xpath('//div[@class="current-abstract"]//text()').get()
        _url = f"https://devapi.qweather.com/v7/indices/1d?key={_key}&location={item['id']}&type=3,8"
        _res = requests.get(_url)
        item['name'] = f"{item['name']}天气"
        item['content'].append(abstract)
        item['content'].append(f'体感温度{feels_like}摄氏度。')
        item['content'].append(f"{_res.json()['daily'][1]['text']}")
        item['content'].append(f"{_res.json()['daily'][0]['text']}")

    logger.debug("daily_weather {}", city_list)
    return city_list


def dail_alcohol():
    url = "https://www.thecocktaildb.com/api/json/v1/1/random.php"
    res = requests.get(url)
    json = res.json()
    drink = json['drinks'][0]
    raw = []
    for i in range(1, 15):
        if drink[f'strIngredient{i}']:
            raw.append({'name': drink[f'strIngredient{i}'], 'measure': drink[f'strMeasure{i}']})
        else:
            break
    res = {
        'name': drink['strDrink'],
        'description': drink['strInstructionsZH-HANS'] if drink['strInstructionsZH-HANS'] else drink['strInstructions'],
        'image': drink['strDrinkThumb'],
        'raw': raw
    }
    logger.debug("dail_alcohol {}", res)
    return res


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


def build_message(_type, msg, title):
    if _type == 'text':
        return {"msgtype": "text", "text": {"content": msg}}
    elif _type == 'markdown':
        return {
            "msgtype": "markdown",
            "markdown": {
                "title": title,
                "text": msg
            },
            "at": {
                "isAtAll": True
            }
        }


@app.get("/daily")
def api_daily():
    return dingding_robot(build_message('markdown', build_markdown(), '每日早报'))


@app.get("/alcohol")
def api_alcohol():
    return dingding_robot(build_message('markdown', build_markdown_alcohol(), '喝一杯'))


def build_markdown_alcohol():
    env = Environment(
        loader=FileSystemLoader("templates"),
        autoescape=select_autoescape()
    )
    date = time.strftime("%Y年%m月%d日", time.localtime())
    template = env.get_template("alcohol.jinja")
    res = template.render(drink=dail_alcohol(), date=date)

    return res


def build_markdown():
    env = Environment(
        loader=FileSystemLoader("templates"),
        autoescape=select_autoescape()
    )
    date = time.strftime("%Y年%m月%d日", time.localtime())
    template = env.get_template("daily.jinja")
    res = template.render(news_list=daily_news(),
                          image=daily_image(),
                          date=date,
                          clause=daily_clause(),
                          weather_list=daily_weather())
    return res


def dingding_robot(msg):
    timestamp, sign = get_sign()
    url = f"https://oapi.dingtalk.com/robot/send?access_token={os.getenv('DINGDING_TOKEN')}&timestamp={timestamp}&sign={sign}"
    res = requests.post(url,
                        headers={"Content-Type": "application/json; charset=utf-8"},
                        json=msg)
    return res.content.decode('utf-8')


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
    print(build_markdown())
    # print(dingding_robot(build_message('markdown', build_markdown())))
    # print(dingding_robot(build_message('markdown', build_markdown_alcohol())))
