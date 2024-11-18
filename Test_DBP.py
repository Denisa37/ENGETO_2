# Denisa F. (Discord)

import pytest

from playwright.sync_api import sync_playwright


def test_dbp_title(page):
     page.goto("https://divadlobolkapolivky.cz/")
     title = page.locator("title")

     assert title.inner_text() == "Divadlo Bolka Polívky"
   

def test_dbp_cookies(page):
    page.goto("https://divadlobolkapolivky.cz/")

    button = page.locator(".goout-cookie-essentials")
    button.click()
   
    
def test_dbp_buyticket(page):
    page.goto("https://divadlobolkapolivky.cz/program/?month_filter=2025-01")
    
    button = page.get_by_text("Přijmout vše")
    button.click()

    button = page.locator("div:nth-child(25) > .events-tickets > a:nth-child(2)")
    button.click()
    
    
def test_dbp_ShowProgram(page):
    page.goto("https://divadlobolkapolivky.cz/")
    
    button = page.locator(".goout-cookie-close")
    button.click()
    
    button = page.get_by_role("link", name="Kompletní program zde")
    button.click()
   

def test_dbp_search(page):
    page.goto("https://divadlobolkapolivky.cz/")
    
    button = page.locator(".goout-cookie-close")
    button.click() 
    
    search = page.locator("input[name=\"q\"]")
    search.fill("DNA")
    
    search.press("Enter")
    
    
  