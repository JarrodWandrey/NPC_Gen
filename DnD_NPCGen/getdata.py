from gettext import npgettext
from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
import settings

def get_data(num):
    with sync_playwright() as p: #to avoid memory issues
        browser = p.firefox.launch(headless=True, slow_mo=50) #browser object we can use
        page = browser.new_page()
        page.goto('https://donjon.bin.sh/fantasy/random/#type=npc;npc-order=common')
        settings.NPCs = []

        while(len(settings.NPCs) < num): #function to gather the information from the website
            html = page.inner_html('#out')
            soup = BeautifulSoup(html, 'html.parser')
            npc_list = soup.find_all('li')
            for item in npc_list:
                settings.NPCs.append(item.text)

            page.click("text=Generate")
