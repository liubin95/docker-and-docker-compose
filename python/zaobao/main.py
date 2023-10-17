import time

import requests
from fastapi import FastAPI
from parsel import Selector
from starlette.middleware.cors import CORSMiddleware
from fastapi import FastAPI, Header, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from fastapi.responses import HTMLResponse


def _zaobao():
    root_domain = 'https://www.zaobao.com'
    try:
        res = requests.get(root_domain, headers={
            'Connection': 'Keep - Alive',
            'User-Agent': 'Apache - HttpClient / 4.5.14(Java / 17.0.8)',
            'Accept-Encoding': 'br, deflate, gzip, x - gzip'
        })
        html = res.content.decode('utf-8')
        selector = Selector(text=html)
        titles = selector.xpath('//div[@class="rank-item"]//a')
        titles = titles[:5]
        return [f'{root_domain}{item.xpath("./@href").get()}' for item in titles]
    except Exception as e:
        print(e)


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


@app.get("/zaobao")
def zaobao():
    return _zaobao()


if __name__ == '__main__':
    print('Hello World!')
    for it in zaobao():
        print(it)
