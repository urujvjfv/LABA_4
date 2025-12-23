"""
Главный файл для демонстрации работы функции calculate_discount
"""
from discount import calculate_discount


def main():
    print("=" * 60)
    print("ДЕМОНСТРАЦИЯ РАБОТЫ ФУНКЦИИ РАСЧЕТА СКИДКИ")
    print("=" * 60)
    
    # Примеры использования
    examples = [
        ("Обычная скидка", 100.0, 20.0, 80.0),
        ("Нулевая скидка", 100.0, 0.0, 100.0),
        ("Скидка 100%", 100.0, 100.0, 0.0),
        ("Дробный процент скидки", 99.99, 33.33, 66.66),
        ("Цена 0", 0.0, 50.0, 0.0),
        ("Большая сумма", 10000.0, 15.0, 8500.0),
    ]
    
    print("\nПримеры корректных расчетов:")
    print("-" * 60)
    
    for description, price, discount, expected in examples:
        try:
            result = calculate_discount(price, discount)
            status = "✓" if abs(result - expected) < 0.01 else "✗"
            print(f"{status} {description}")
            print(f"  Цена: {price:.2f} руб., Скидка: {discount}%")
            print(f"  Итог: {result:.2f} руб. (ожидалось: {expected:.2f} руб.)")
            print()
        except ValueError as e:
            print(f"✗ {description}: Ошибка - {e}")
            print()
    
    print("\nПримеры ошибочных входных данных:")
    print("-" * 60)
    
    error_cases = [
        ("Отрицательная скидка", 100.0, -10.0),
        ("Скидка больше 100%", 100.0, 150.0),
    ]
    
    for description, price, discount in error_cases:
        try:
            result = calculate_discount(price, discount)
            print(f"✗ {description}: ОШИБКА! Функция не вызвала исключение")
            print(f"  Получен результат: {result}")
        except ValueError as e:
            print(f"✓ {description}: Правильно вызвано исключение")
            print(f"  Сообщение: {e}")
        print()
    
    print("\nИнтерактивный режим:")
    print("-" * 60)
    
    # Интерактивная часть
    while True:
        try:
            price_input = input("Введите цену (или 'q' для выхода): ")
            if price_input.lower() == 'q':
                break
                
            discount_input = input("Введите процент скидки (0-100): ")
            if discount_input.lower() == 'q':
                break
            
            price = float(price_input)
            discount = float(discount_input)
            
            result = calculate_discount(price, discount)
            print(f"Результат: {price:.2f} руб. - {discount}% = {result:.2f} руб.")
            print()
            
        except ValueError as e:
            print(f"Ошибка: {e}")
            print("Пожалуйста, введите корректные числа.")
            print()
        except KeyboardInterrupt:
            print("\nПрограмма завершена.")
            break
    
    print("\n" + "=" * 60)
    print("ПРОГРАММА ЗАВЕРШЕНА")
    print("=" * 60)


if __name__ == "__main__":
    main()
