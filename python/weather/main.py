# coding=utf-8
import re
import time
from typing import Union

import requests
from fastapi import FastAPI, Header, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from fastapi.responses import HTMLResponse


def get_city(_latitude, _longitude, key):
    _url = f"https://geoapi.qweather.com/v2/city/lookup?key={key}&location={_longitude},{_latitude}"
    _res = requests.get(_url)
    _json = _res.json()
    _city = _json['location'][0]['adm2']
    _city_id = _json['location'][0]['id']
    return _city, _city_id


def get_weather(_city_id, key):
    _url = f"https://devapi.qweather.com/v7/weather/now?key={key}&location={_city_id}"
    _res = requests.get(_url)
    _json = _res.json()
    _weather_text = _json['now']['text']
    _weather_temp = _json['now']['temp']
    _weather_feelsLike = _json['now']['feelsLike']
    _weather_windDir = _json['now']['windDir']
    _weather_windScale = _json['now']['windScale']
    return _weather_text, _weather_temp, _weather_feelsLike, _weather_windDir, _weather_windScale


def get_daily(_city_id, key):
    _url = f"https://devapi.qweather.com/v7/indices/1d?key={key}&location={_city_id}&type=1,3,8,10,11"
    _res = requests.get(_url)
    _json = _res.json()
    return _json['daily'][1]['text']


def get_warning(_city_id, key):
    _url = f"https://devapi.qweather.com/v7/warning/now?key={key}&location={_city_id}"
    _res = requests.get(_url)
    _json = _res.json()
    return _json['warning']


def get_weather_main(latitude, longitude, key):
    city, city_id = get_city(latitude, longitude, key)
    weather_text, weather_temp, weather_feelsLike, weather_windDir, weather_windScale = get_weather(city_id, key)
    daily = get_daily(city_id, key)
    warning = get_warning(city_id, key)
    warning = list(warning)

    def deal_warning(it):
        _str = re.sub(r'\[.*/', '，', it['title'])
        _str = re.sub(r']', '', _str)
        return _str

    warning_str = '。'.join(map(deal_warning, warning))

    final_text = f"你当前在{city}市，天气{weather_text}，体感温度{weather_feelsLike}摄氏度。{weather_windDir}{weather_windScale}级。{daily}{warning_str}"
    return final_text


app = FastAPI(docs_url=None, redoc_url=None)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


# 为app增加接口处理耗时的响应头信息
@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    authority = request.headers.get("authority")
    # 没有 authority 请求头 并且 不是 OPTIONS 则返回 403
    if not authority and request.method != "OPTIONS" and request.url.path != "/daily":
        return JSONResponse(status_code=403, content={"msg": "请提供authority"})
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time

    # X- 作为前缀代表专有自定义请求头
    response.headers["X-Process-Time"] = str(process_time)
    return response

i
@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/daily",response_class=HTMLResponse)
def daily():
    # 获取图片
    res_bing = requests.get("https://cn.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1&mkt=zh-cn")
    res_bing = res_bing.json()
    img_url = "https://cn.bing.com" + res_bing['images'][0]['url']
    img_title = res_bing['images'][0]['title']
    img_copyright = res_bing['images'][0]['copyright'] 
    return JSONResponse(status_code=403, content={"url": img_url,"title":img_title,"copyright":img_copyright})

@app.get("/weather/{latitude}/{longitude}")
def weather(latitude: str,
            longitude: str,
            authority: Union[str, None] = Header(default=None)):
    return get_weather_main(latitude, longitude, authority)
