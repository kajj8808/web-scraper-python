from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

options = Options()
# 웹 브라우저가 실제 사용자가 접근한 것처럼 설정 (모바일 에이전트 사용)
user_agent = "Mozilla/5.0 (Linux; Android 9; SM-G975F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.83 Mobile Safari/537.36"
options.add_argument('user-agent=' + user_agent)
options.add_argument("headless")  # 브라우저를 띄우지 않고 실행 (헤드리스 모드)
options.add_argument('--start-maximized')

# Selenium 웹 드라이버 실행
browser = webdriver.Chrome(options=options)

# 웹 페이지 로드
browser.get('https://nyaa.si/')

# 스크린샷을 PNG 형식으로 얻기
screenshot = browser.get_screenshot_as_png()

# 로컬 파일에 스크린샷 저장
with open('screenshot.png', 'wb') as file:
    file.write(screenshot)

# 페이지 소스를 가져오기
html_content = browser.page_source

# BeautifulSoup을 사용하여 HTML 파싱
soup = BeautifulSoup(html_content, 'html.parser')

# 예시: 페이지 제목 추출
title = soup.title.string
print(f"Page Title: {title}")

# 예시: 특정 요소 찾기 (예: 페이지의 모든 링크)
links = soup.find_all('a')
for link in links:
    print(link.get('href'))

# 웹 드라이버 종료
browser.quit()

