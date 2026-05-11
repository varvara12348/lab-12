from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

YOUR_LOGIN = "varvara12348"      
YOUR_PASSWORD = "password135427"    

def test_successful_login():
    print("\n" + "="*50)
    print("ТЕСТ №1: Успешная авторизация")
    print("="*50)
    
    driver = webdriver.Chrome()
    driver.maximize_window()
    
    try:
        # Шаг 1: Открыть страницу авторизации
        driver.get("https://github.com/login")
        print("✓ Открыта страница авторизации")
        
        # Шаг 2: Ввести логин (с ожиданием загрузки поля)
        username_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "login_field"))
        )
        username_field.send_keys(YOUR_LOGIN)
        print("✓ Логин введен")
        
        # Шаг 3: Ввести пароль
        password_field = driver.find_element(By.ID, "password")
        password_field.send_keys(YOUR_PASSWORD)
        print("✓ Пароль введен")
        
        # Шаг 4: Нажать кнопку Sign in
        sign_in_button = driver.find_element(By.NAME, "commit")
        sign_in_button.click()
        print("✓ Нажата кнопка Sign in")
        
        # Ожидание загрузки страницы после входа
        time.sleep(5)
        
        # Проверка успешного входа - проверяем URL
        current_url = driver.current_url
        print(f"✓ Текущий URL: {current_url}")
        
        # Если URL не содержит "login" - значит вход выполнен
        if "login" not in current_url:
            print("✓ URL изменился - вход выполнен")
            print("\n✅ ТЕСТ №1 ПРОЙДЕН - Успешная авторизация")
        else:
            print("\n❌ ТЕСТ №1 НЕ ПРОЙДЕН - Вход не выполнен")
            
    except Exception as e:
        print(f"\n❌ ТЕСТ №1 НЕ ПРОЙДЕН - Ошибка: {e}")
        
    finally:
        time.sleep(3)
        driver.quit()

# Запуск теста
if __name__ == "__main__":
    test_successful_login()
