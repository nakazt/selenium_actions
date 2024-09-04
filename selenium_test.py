"""
このモジュールはSeleniumを使用してWebページのテストを実行します。
"""

import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


TARGET_URL = "https://nakazt.github.io/actions_test/"
EXPECTED_H1 = "GitHub Actions + Pages Samples"


def selenium_test(url, expected_h1):
    """テストの実行"""

    chrome_options = Options()
    chrome_options.add_argument("--headless")  # ヘッドレスモード

    if os.name == "nt":
        current_dir = os.path.dirname(os.path.abspath(__file__))
        chrome_driver_path = os.path.join(current_dir, "chromedriver.exe")
        service = Service(executable_path=chrome_driver_path)
    elif os.name == "posix":
        service = Service("/usr/bin/chromedriver")

    driver = webdriver.Chrome(service=service, options=chrome_options)

    # テスト開始
    driver.get(url)
    title = driver.title
    h1_text = driver.find_element(By.TAG_NAME, "h1").text

    assert (
        h1_text == expected_h1
    ), f"H1 が一致しません。取得値: {h1_text}、期待値: {EXPECTED_H1}"

    print(f"page title: {title}")
    print(f"h1 text:    {h1_text}")

    time.sleep(0)
    driver.quit()


if __name__ == "__main__":
    selenium_test(TARGET_URL, EXPECTED_H1)
