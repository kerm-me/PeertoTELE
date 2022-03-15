from threading import activeCount
from playwright.sync_api import Playwright, sync_playwright
import time  # 引入time模块
import requests

baseuri = 'https://api.telegram.org/bot'
method = '/sendMessage?chat_id='
chat_id = ""  # Userid
token = ""  # 机器人 TOKEN


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=True)
    # context = browser.new_context(storage_state="./peer2profit")
    context = browser.new_context(storage_state="./peer2profit")

    # Open new page
    page = context.new_page()

    page.goto("https://peer2profit.com/dashboard")

    # el = 

    # totalearn = el.text_content()

    # print(totalearn)
    els = page.query_selector_all("//div[@class='earnings-amount']")
    el = page.query_selector("//div[@class='earnings-amount earnings-total']").text_content()

    massage = 'Peer2Profit每日报告\n'+time.strftime("%Y-%m-%d", time.localtime())+'\n流量收益：'+els[0].text_content()+'\n代理收益：'+(els[1]).text_content()+'\n总收益：'+el

    print(massage)
    uri = baseuri+token+method+chat_id+'&text='+massage
    requests.get(uri)

    context.close()
    browser.close()


with sync_playwright() as playwright:
    # print(os.getcwd())
    run(playwright)
