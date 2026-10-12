from __future__ import annotations

import calendar
from datetime import date

WEEKDAYS_RU = (
    "понедельник",
    "вторник",
    "среда",
    "четверг",
    "пятница",
    "суббота",
    "воскресенье",
)

DIGITS = {
    "0": [" *** ", "*   *", "*   *", "*   *", " *** "],
    "1": ["  *  ", " **  ", "  *  ", "  *  ", " *** "],
    "2": [" *** ", "*   *", "   * ", "  *  ", "*****"],
    "3": ["**** ", "    *", " *** ", "    *", "**** "],
    "4": ["*  * ", "*  * ", "*****", "   * ", "   * "],
    "5": ["*****", "*    ", "**** ", "    *", "**** "],
    "6": [" *** ", "*    ", "**** ", "*   *", " *** "],
    "7": ["*****", "    *", "   * ", "  *  ", "  *  "],
    "8": [" *** ", "*   *", " *** ", "*   *", " *** "],
    "9": [" *** ", "*   *", " ****", "    *", " *** "],
    " ": ["   ", "   ", "   ", "   ", "   "],
}


def get_weekday(birth_date: date) -> str:
    """Возвращает русское название дня недели для даты."""
    return WEEKDAYS_RU[birth_date.weekday()]


def is_leap_year(year: int) -> bool:
    """Определяет, является ли год високосным."""
    return calendar.isleap(year)


def calculate_age(birth_date: date, today: date | None = None) -> int:
    """Возвращает полный возраст пользователя на текущую дату."""
    today = today or date.today()
    years = today.year - birth_date.year
    birthday_not_reached = (today.month, today.day) < (birth_date.month, birth_date.day)
    return years - int(birthday_not_reached)


def render_star_date(birth_date: date) -> str:
    """Рисует дату в формате дд мм гггг символами '*'."""
    text = birth_date.strftime("%d %m %Y")
    rows: list[str] = []
    for row in range(5):
        rows.append(" ".join(DIGITS[ch][row] for ch in text))
    return "\n".join(rows)


def read_int(prompt: str) -> int:
    while True:
        value = input(prompt).strip()
        try:
            return int(value)
        except ValueError:
            print("Ошибка: введите целое число.")


def main() -> None:
    print("Стилистическое преобразование даты рождения")
    print("-" * 46)

    day = read_int("Введите день рождения: ")
    month = read_int("Введите месяц рождения: ")
    year = read_int("Введите год рождения: ")

    try:
        birth_date = date(year, month, day)
    except ValueError as exc:
        print(f"Ошибка: такой даты не существует ({exc}).")
        return

    today = date.today()
    if birth_date > today:
        print("Ошибка: дата рождения не может быть в будущем.")
        return

    print(f"\nДень недели: {get_weekday(birth_date)}")
    print(f"Високосный год: {'да' if is_leap_year(year) else 'нет'}")
    print(f"Возраст: {calculate_age(birth_date, today)}")
    print("\nДата рождения в формате электронного табло:\n")
    print(render_star_date(birth_date))


if __name__ == "__main__":
    main()