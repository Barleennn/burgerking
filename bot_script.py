from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time
from aiogram import Bot, Dispatcher, types
from aiogram.types import ParseMode
from aiogram.utils import executor
import asyncio

# Учетные данные по умолчанию
LOGIN = "БАЛОРА001"
PASSWORD = "SpA123456$"

API_TOKEN = '5754695804:AAHiIp1BY2skLVnVUlNZhWDoaTRTBlaApyY'
CHAT_ID = '1419048544'

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

def send_message(message: str):
    asyncio.run(bot.send_message(CHAT_ID, message, parse_mode=ParseMode.MARKDOWN))

def login(driver):
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "okta-signin-username")))
    username = driver.find_element(By.ID, "okta-signin-username")
    password = driver.find_element(By.ID, "okta-signin-password")
    username.send_keys(LOGIN)
    password.send_keys(PASSWORD)
    login_button = driver.find_element(By.ID, "okta-signin-submit")
    login_button.click()
    send_message("Вход выполнен.")
    time.sleep(15)

def navigate_to_page(driver, url):
    driver.get(url)

def wait_for_video(driver):
    try:
        video = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "video"))
        )
        duration = driver.execute_script("return arguments[0].duration", video)
        
        if duration:
            wait_time = duration + 5  # Добавляем 5 секунд к длительности видео
            send_message(f"Видео найдено. Длительность: {duration} секунд. Ожидание: {wait_time} секунд.")
            time.sleep(wait_time)
        else:
            send_message("Не удалось определить длительность видео. Ожидание 30 секунд.")
            time.sleep(30)
    except:
        send_message("Видео не найдено на странице. Продолжаем без ожидания.")

def click_start_learning_button(driver):
    try:
        start_learning_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'button-rectangular') and contains(@class, 'bg-positive-green-filled')]"))
        )
        actions = ActionChains(driver)
        actions.move_to_element(start_learning_button).click().perform()
        send_message("Кнопка 'Начните обучение прямо сейчас' нажата.")
    except Exception as e:
        send_message(f"Не удалось найти или нажать кнопку 'Начните обучение прямо сейчас': {e}")

def click_next_button(driver):
    try:
        time.sleep(5)
        next_button = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, "//rectangular-button[contains(@class, 'navigate next')]/button"))
        )
        driver.execute_script("arguments[0].click();", next_button)
        send_message("Кнопка 'След.' нажата с помощью JavaScript.")
        time.sleep(5)
        return True
    except Exception as e:
        send_message(f"Не удалось найти или нажать кнопку 'След.': {e}")
        return False

@dp.message_handler(commands=['set_credentials'])
async def set_credentials(message: types.Message):
    global LOGIN, PASSWORD
    try:
        _, new_login, new_password = message.text.split(maxsplit=2)
        LOGIN = new_login
        PASSWORD = new_password
        await send_message(f"Логин и пароль обновлены: {LOGIN} / {PASSWORD}")
    except ValueError:
        await send_message("Неверный формат команды. Используйте: /set_credentials <логин> <пароль>")

@dp.message_handler(commands=['start'])
async def start_tasks(message: types.Message):
    await send_message("Запуск задач...")
    user_queue = [
        {"login": "user1", "password": "pass1"},
        {"login": "user2", "password": "pass2"},
        # Добавьте других пользователей
    ]

    for user in user_queue:
        LOGIN = user["login"]
        PASSWORD = user["password"]

        driver = webdriver.Chrome()

        urls = [
                "https://rbi.okta.com/app/restaurantbrandsinternational_burgerkingacademy_1/exk1he4dgr4B86Exq1d8/sso/saml",
    "https://www.burgerkinguniversity.com/learn/course/6069/dobro-pozalovat-v-burger-king-a001ruskz;lp=2195",
    "https://www.burgerkinguniversity.com/learn/course/6075/bezopasnost-pisevyh-produktov-a003ruskz;lp=2195",
    "https://www.burgerkinguniversity.com/learn/course/9505/allergens-a0035ruskz;lp=2195",
    "https://www.burgerkinguniversity.com/learn/course/6077/uborka-obzor-a004ruskz;lp=2195",
    "https://www.burgerkinguniversity.com/learn/course/6080/ocistka-s-glubokim-pogruzeniem-a005ruskz;lp=2195",
    "https://www.burgerkinguniversity.com/learn/course/6084/bezopasnost-i-zasita-a006ruskz;lp=2195",
    "https://www.burgerkinguniversity.com/learn/course/6090/ocenocnyj-list-osnovy-basicsruskz;lp=2195",
    "https://www.burgerkinguniversity.com/learn/course/6090/ocenocnyj-list-osnovy-basicsruskz;lp=873",
    "https://www.burgerkinguniversity.com/learn/course/6096/uborka-restorana-bk009ruskz;lp=873",
    "https://www.burgerkinguniversity.com/learn/course/6096/uborka-restorana-bk009ruskz;lp=873",
    "https://www.burgerkinguniversity.com/learn/course/6096/uborka-restorana-bk009ruskz;lp=873",
    "https://www.burgerkinguniversity.com/learn/course/6102/prigotovlenie-zagotovok-sendvici-bk011ruskz;lp=873",
    "https://www.burgerkinguniversity.com/learn/course/6114/sendvici-bk016ruskz",
    "https://www.burgerkinguniversity.com/learn/course/6179/zavtrak-bk038ruskz",
    "https://www.burgerkinguniversity.com/learn/course/6272/deserty-bk018ruskz",
    "https://www.burgerkinguniversity.com/learn/course/6273/vedusij-specialist-po-prodazam-i-obsluzivaniu-bk023ruskz",
    "https://www.burgerkinguniversity.com/learn/course/6064/upakovka-markirovka-i-obertka-bk015ruskz",
    "https://www.burgerkinguniversity.com/learn/course/6069/dobro-pozalovat-v-burger-king-a001ruskz",
    "https://www.burgerkinguniversity.com/learn/course/6072/myte-ruk-a002ruskz",
    "https://www.burgerkinguniversity.com/learn/course/6075/bezopasnost-pisevyh-produktov-a003ruskz",
    "https://www.burkerkinguniversity.com/learn/course/6080/ocistka-s-glubokim-pogruzeniem-a005ruskz",
    "https://www.burkerkinguniversity.com/learn/course/6084/bezopasnost-i-zasita-a006ruskz",
    "https://www.burkerkinguniversity.com/learn/course/6090/ocenocnyj-list-osnovy-basicsruskz",
    "https://www.burkerkinguniversity.com/learn/course/6093/osnovnye-principy-podgotovki-bk008ruskz",
    "https://www.burkerkinguniversity.com/learn/course/6096/uborka-restorana-bk009ruskz",
    "https://www.burkerkinguniversity.com/learn/course/6099/vyderzka-goracih-produktov-bk010ruskz",
    "https://www.burkerkinguniversity.com/learn/course/6105/ispolzovanie-zarocnogo-skafa-bk012ruskz",
    "https://www.burkerkinguniversity.com/learn/course/6108/ispolzovanie-friturnicy-bk014ruskz",
    "https://www.burkerkinguniversity.com/learn/course/6118/napitki-bk017ruskz"
    "https://www.burgerkinguniversity.com/learn/course/6090/ocenocnyj-list-osnovy-basicsruskz;lp=872",
    "https://www.burgerkinguniversity.com/learn/course/6093/osnovnye-principy-podgotovki-bk008ruskz;lp=872",
    "https://www.burgerkinguniversity.com/learn/course/6096/uborka-restorana-bk009ruskz;lp=872",
    "https://www.burgerkinguniversity.com/learn/course/6099/vyderzka-goracih-produktov-bk010ruskz;lp=872",
    "https://www.burgerkinguniversity.com/learn/course/6108/ispolzovanie-friturnicy-bk014ruskz;lp=872",
    "https://www.burgerkinguniversity.com/learn/course/6090/ocenocnyj-list-osnovy-basicsruskz;lp=874",
    "https://www.burgerkinguniversity.com/learn/course/6118/napitki-bk017ruskz;lp=874",
    "https://www.burgerkinguniversity.com/learn/course/6272/deserty-bk018ruskz;lp=874",
    "https://www.burgerkinguniversity.com/learn/course/6096/uborka-restorana-bk009ruskz;lp=874",
    "https://www.burgerkinguniversity.com/learn/course/6099/vyderzka-goracih-produktov-bk010ruskz;lp=874",
    "https://www.burgerkinguniversity.com/learn/course/6064/upakovka-markirovka-i-obertka-bk015ruskz;lp=874",
        ]

        navigate_to_page(driver, urls[0])
        login(driver)

        for url in urls[1:]:
            navigate_to_page(driver, url)
            click_start_learning_button(driver)
            
            while True:
                wait_for_video(driver)
                if not click_next_button(driver):
                    send_message("Переходим к следующей ссылке.")
                    break
                
                if "rbi.okta.com" in driver.current_url:
                    send_message("Перенаправление на страницу авторизации. Повторная попытка входа.")
                    login(driver)
                    break

        driver.quit()

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
