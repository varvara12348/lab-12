from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

YOUR_LOGIN = "varvara12348"           
YOUR_PASSWORD = "password135427"          
YOUR_PROFILE_URL = "https://github.com/varvara12348"
REPO_NAME = "china"                   
REPO_URL = "https://github.com/varvara12348/china"

def test_navigate_to_repository():
    print("\n" + "="*50)
    print("ТЕСТ №3: Переход к репозиторию")
    print("="*50)
    
    driver = webdriver.Chrome()
    driver.maximize_window()
    
    try:
        # Шаг 1: Авторизация
        driver.get("https://github.com/login")
        print("✓ Открыта страница авторизации")
        
        username_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "login_field"))
        )
        username_field.send_keys(YOUR_LOGIN)
        print("✓ Логин введен")
        
        password_field = driver.find_element(By.ID, "password")
        password_field.send_keys(YOUR_PASSWORD)
        print("✓ Пароль введен")
        
        sign_in_button = driver.find_element(By.NAME, "commit")
        sign_in_button.click()
        print("✓ Нажата кнопка Sign in")
        time.sleep(3)
        print("✓ Авторизация выполнена")
        
        # Шаг 2: Переход на страницу профиля
        driver.get(YOUR_PROFILE_URL)
        time.sleep(2)
        print(f"✓ Открыта страница профиля: {YOUR_PROFILE_URL}")
        
        # Шаг 3: Поиск и клик по репозиторию
        repo_link = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, REPO_NAME))
        )
        repo_link.click()
        time.sleep(2)
        print(f"✓ Клик по репозиторию '{REPO_NAME}'")
        
        # Проверка: соответствует ли URL ожидаемому
        if REPO_URL in driver.current_url:
            print(f"✓ Текущий URL: {driver.current_url}")
            print("\n✅ ТЕСТ №3 ПРОЙДЕН - Переход к репозиторию выполнен")
        else:
            print(f"⚠️ Ожидалось: {REPO_URL}")
            print(f"⚠️ Фактически: {driver.current_url}")
            print("\n❌ ТЕСТ №3 НЕ ПРОЙДЕН - URL не совпадает")
            
    except Exception as e:
        print(f"\n❌ ТЕСТ №3 НЕ ПРОЙДЕН - Ошибка: {e}")
        
    finally:
        time.sleep(3)
        driver.quit()

# Запуск теста
if __name__ == "__main__":
    test_navigate_to_repository()
