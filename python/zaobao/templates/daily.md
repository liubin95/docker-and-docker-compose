# {{ date }} 早 报

## 今日新闻

{% for item in news_list %}
- [{{ item.title }}]({{ item.href }})
{% endfor %}

## 每日一图

{{ image.title }}
{{ image.copyright }}

![{{ image.title }}]({{ image.url }})

## 每日一句

- {{ clause.content }}
- {{ clause.translation }}