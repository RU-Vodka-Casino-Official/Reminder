import time
import argparse
try:
    from plyer import notification
    USE_SYSTEM_NOTIFICATION = True
except ImportError:
    USE_SYSTEM_NOTIFICATION = False

def remind(message: str, delay_seconds: int):
    print(f"⏳ Напоминание установлено на {delay_seconds} секунд.")
    time.sleep(delay_seconds)
    print(f"🔔 Напоминание: {message}")
    
    if USE_SYSTEM_NOTIFICATION:
        notification.notify(
            title='Напоминание',
            message=message,
            timeout=10
        )

def parse_time(time_str: str) -> int:
    if time_str.endswith('m'):
        return int(time_str[:-1]) * 60
    elif time_str.endswith('s'):
        return int(time_str[:-1])
    else:
        raise ValueError("Укажите время в формате '10s' или '5m'")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Простой скрипт-напоминалка")
    parser.add_argument("time", help="Время до напоминания (например: 10s, 5m)")
    parser.add_argument("message", help="Сообщение напоминания в кавычках")
    args = parser.parse_args()

    try:
        delay = parse_time(args.time)
        remind(args.message, delay)
    except ValueError as e:
        print(f"Ошибка: {e}")
