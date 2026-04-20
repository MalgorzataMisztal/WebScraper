import os
import json
import requests
from bs4 import BeautifulSoup

product_code = input("Provide product code: ")
page = 1
next = True
headers = {
    "Host": "www.ceneo.pl",
    "Cookie": "sv3=1.0_80884de2-3cbb-11f1-b9f4-2ba308a43880; urdsc=1; userCeneo=ID=53dc9c67-50ab-462e-a92d-5a4ae3ea521f; __RequestVerificationToken=dGr72PcFQmiQVgrAldxkQdBrEjHY6t0nEiDmHAKHJsGdUrM2Ng0LpjCtz1BlQJrA6VZcCBIcDqiRXZvPlia7WdxED_CN0QYx248U2V6BKQE1; ai_user=ZstTS|2026-04-20T13:19:04.186Z; __utmf=364726cdbe2e8437518b57e7b5f0d525_Dsgqi6QMc9CtX7buqOpcIw%3D%3D; appType=%7B%22Value%22%3A1%7D; cProdCompare_v2=; browserBlStatus=0; ga4_ga=GA1.2.80884de2-3cbb-11f1-b9f4-2ba308a43880; _gcl_au=1.1.2107283923.1776691147; consentcookie=eyJBZ3JlZUFsbCI6dHJ1ZSwiQ29uc2VudHMiOlsxLDMsNCwyXSwiVENTdHJpbmciOiJDUWk5ajBBUWk5ajBBR3lBQkJQTENiRXNBUF9nQUFBQUFCNVlJekpEN0JiRkxVRkF3RmhqWUtzUU1JRVRVTUNBQW9RQUFBYUJBQ0FCUUFLUUlBUUNra0FRQkFTZ0JBQUNBQUFBSUNSQklRQU1BQUFBQ0VBQVFBQUFJQUFFQUFDUUFRQUlBQUFBZ0FBUUFBQVlBQUFpQUlBQUFBQUlnQUlBRUFBQW1RaEFBQUlBRUVBQWhBQUVJQUFBQUFBQUFBQUFBZ0FBQUFBQ0FBSUFBQUFBQUNBQUFJQUFBQUFBQUFBQUFCQkdZQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFCWUtBREFBRUVaZ2tBR0FBSUl6Qm9BTUFBUVJtRVFBWUFBZ2pNS2dBd0FCQkdZWkFCZ0FDQ013NkFEQUFFRVppRUFHQUFJSXpFb0FNQUFRUm1LUUFZQUFnak1XZ0F3QUJCR1kuSUl6SkQ3QmJGTFVGQXdGaGpZS3NRTUlFVFVNQ0FBb1FBQUFhQkFDQUJRQUtRSUFRQ2trQVFCQVNnQkFBQ0FBQUFJQ1JCSVFBTUFBQUFDRUFBUUFBQUlBQUVBQUNRQVFBSUFBQUFnQUFRQUFBWUFBQWlBSUFBQUFBSWdBSUFFQUFBbVFoQUFBSUFFRUFBaEFBRUlBQUFBQUFBQUFBQUFnQUFBQUFDQUFJQUFBQUFBQ0FBQUlBQUFBQUFBQUFBQUJBIiwiVmVyc2lvbiI6InYzIn0=; FPID=FPID2.2.lZMGih%2FwwqD0C3y2bM11hRIatBDZMbvH0MV%2FSXMyLTc%3D; FPLC=H0Q45%2BocxQ6K5AEFQaH%2FQoXY3tvF2Wu8qegBEU850mxjAWUs6aj4JL2oIgXEgyYJsIuoT8ZJg%2Bf0uSM2TQzC2d5C4E0fLXXaTYeJan%2FWsNubxNo%3D; nps3=SessionStartTime=1776691158,SurveyId=68; _fbp=fb.1.1776691159171.933698697798143435; ai_session=y0yLg|1776691144883|1776691159352; ga4_ga_K2N2M0CBQ6=GS2.2.s1776691145$o1$g1$t1776691159$j60$l0$h1094332990; __rtbh.uid=%7B%22eventType%22%3A%22uid%22%2C%22id%22%3A%22unknown%22%2C%22expiryDate%22%3A%222027-04-20T13%3A19%3A19.834Z%22%7D; __rtbh.aid=%7B%22eventType%22%3A%22aid%22%2C%22id%22%3A%2280884de2-3cbb-11f1-b9f4-2ba308a43880%22%2C%22expiryDate%22%3A%222027-04-20T13%3A19%3A19.834Z%22%7D; __rtbh.lid=%7B%22eventType%22%3A%22lid%22%2C%22id%22%3A%22qUS1NgKF7v2b4R9Ru5qn%22%2C%22expiryDate%22%3A%222027-04-20T13%3A19%3A19.834Z%22%7D; _tt_enable_cookie=1; _ttp=01KPNGQ8WRFKRMW09JMB0WHFH9_.tt.1; ttcsid_CNK74OBC77U1PP7E4UR0=1776691159963::nn1xKb4tvJi4u5bHqbTz.1.1776691159971.0; ttcsid=1776691159964::qJ7WPMotWKTKpTM5T9rU.1.1776691159972.0::1.-2002.0::0.0.0.0::0.0.0",
    "User-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36 Edg/147.0.0.0"
}

all_opinions = []
while next:
    url = f"https://www.ceneo.pl/{product_code}/opinie-{page}"
    response = requests.get(url, headers = headers)
    if response.status_code == 200:
        page_dom = BeautifulSoup(response.text, 'html.parser')
        product_name = page_dom.select_one('h1').get_text() if page == 1 else product_name
        opinions = page_dom.select("div.js_product-review:not(.user-post--highlight)")
        print(len(opinions))
    
        for opinion in opinions:
            single_opinion = {
                'opinion_id': opinion.get("data-entry-id"),
                'author': opinion.select_one("span.user-post__author-name").get_text().strip(),
                'recommendation': opinion.select_one("span.user-post__author-recomendation > em").get_text().strip() if opinion.select_one("span.user-post__author-recomendation > em") else None,
                'score': opinion.select_one("span.user-post__score-count").get_text().strip(),
                'content': opinion.select_one("div.user-post__text").get_text().strip(),
                'pros': [p.get_text().strip() for p in opinion.select("div.review-feature__item--positive")],
                'cons': [c.get_text().strip() for c in opinion.select("div.review-feature__item--negative")],
                'helpful': opinion.select_one("button.vote-yes > span").get_text().strip(),
                'unhelpful': opinion.select_one("button.vote-no > span").get_text().strip(),
                'publish_date': opinion.select_one("span.user-post__published > time:nth-child(1)[datetime]").get('datetime').strip(),
                'purchase_date': opinion.select_one("span.user-post__published > time:nth-child(2)[datetime]").get('datetime').strip() if opinion.select_one("span.user-post__published > time:nth-child(2)[datetime]")  else None
            }
        all_opinions.append(single_opinion)
next = True if page_dom.select_one('button.pagination_next') else False
if next: page += 1 

if not os.path.exists("./opinions"):
    os.mkdir("./opinions")

with open(f"./opinions/{product_code}.json", "w", encoding="UTF-8") as jf:
    json.dump(all_opinions, jf, indent=4, ensure_ascii= False)