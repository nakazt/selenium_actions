"""
このモジュールはSeleniumを使用してWebページのテストを実行します。
"""

import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


URL = "https://den2k6.github.io/actions_aws_deploy/"
EXPECTED_TITLE = "AWS deploy test using Actions"


def selenium_test(url, expected_title):
    """テストの実行"""

    #  Chromeのオプションを設定
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # ヘッドレスモード

    if os.name == "nt":
        # Windows の場合　ここから 4行
        # ソースコードと同じディレクトリにある chromedriver のパスを取得
        current_dir = os.path.dirname(os.path.abspath(__file__))
        chrome_driver_path = os.path.join(current_dir, "chromedriver.exe")
        service = Service(executable_path=chrome_driver_path)
        driver = webdriver.Chrome(service=service, options=chrome_options)
    elif os.name == "posix":
        # Ubuntu の場合　ここから 2行
        service = Service("/usr/bin/chromedriver")
        driver = webdriver.Chrome(service=service, options=chrome_options)

    # テスト対象のWebページにアクセス
    driver.get(url)

    # ページのタイトルと要素を取得
    title = driver.title
    h1_text = driver.find_element(By.TAG_NAME, "h1").text

    # タイトルが期待通りかチェック
    assert (
        title == expected_title
    ), f"タイトルが一致しません。取得されたタイトル: {title}"

    # 要素を表示
    print(f"page title: {title}")
    print(f"h1 text:    {h1_text}")

    time.sleep(1)

    # WebDriverを終了
    driver.quit()


if __name__ == "__main__":
    selenium_test(URL, EXPECTED_TITLE)
