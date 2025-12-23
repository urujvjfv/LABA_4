def calculate_discount(price: float, discount_percent: float) -> float:
    """
    Рассчитывает итоговую цену после применения скидки.
    
    Args:
        price: Исходная цена
        discount_percent: Процент скидки (от 0 до 100)
    
    Returns:
        Итоговая цена после скидки
    
    Raises:
        ValueError: Если скидка отрицательная или больше 100%
    """
    if discount_percent < 0 or discount_percent > 100:
        raise ValueError("Скидка должна быть в диапазоне от 0 до 100%")
    
    discount_amount = price * (discount_percent / 100)
    final_price = price - discount_amount
    
    # Округляем до 2 знаков после запятой для денежных значений
    return round(final_price, 2)
