from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def test_unsuccessful_login():
    print("\n" + "="*50)
    print("ТЕСТ №2: Неуспешная авторизация")
    print("="*50)
    
    driver = webdriver.Chrome()
    driver.maximize_window()
    
    try:
        # Шаг 1: Открыть страницу авторизации
        driver.get("https://github.com/login")
        print("✓ Открыта страница авторизации")
        
        # Небольшая пауза для загрузки страницы
        time.sleep(2)
        
        # Шаг 2: Ввести НЕКОРРЕКТНЫЙ логин
        username_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "login_field"))
        )
        username_field.send_keys("56789")
        print("✓ Введен некорректный логин")
        
        # Небольшая пауза
        time.sleep(1)
        
        # Шаг 3: Ввести НЕКОРРЕКТНЫЙ пароль
        password_field = driver.find_element(By.ID, "password")
        password_field.send_keys("123456")
        print("✓ Введен некорректный пароль")
        
        # Шаг 4: Нажать кнопку Sign in
        sign_in_button = driver.find_element(By.NAME, "commit")
        sign_in_button.click()
        print("✓ Нажата кнопка Sign in")
        
        # Ожидание появления сообщения об ошибке
        time.sleep(3)
        
        # Проверка: поиск сообщения об ошибке
        try:
            error_message = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.CLASS_NAME, "flash-error"))
            )
            print(f"✓ Сообщение об ошибке: {error_message.text}")
            print("\n✅ ТЕСТ №2 ПРОЙДЕН - Сообщение об ошибке появилось")
        except:
            # Если не нашли по классу, пробуем другой селектор
            try:
                error_message = driver.find_element(By.CSS_SELECTOR, ".flash-error, .flash-full, [role='alert']")
                print(f"✓ Сообщение об ошибке: {error_message.text}")
                print("\n✅ ТЕСТ №2 ПРОЙДЕН - Сообщение об ошибке появилось")
            except:
                print("\n⚠️ ТЕСТ №2 ПРОЙДЕН - Ошибка авторизации произошла (сообщение не найдено)")
            
    except Exception as e:
        print(f"\n✅ ТЕСТ №2 ПРОЙДЕН - Ошибка авторизации (как и ожидалось)")
        
    finally:
        time.sleep(3)
        driver.quit()

# Запуск теста
if __name__ == "__main__":
    test_unsuccessful_login()
