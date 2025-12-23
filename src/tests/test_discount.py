import pytest
from src.discount import calculate_discount


def test_regular_discount():
    """Тест для обычной скидки"""
    # Act
    result = calculate_discount(100.0, 20.0)
    
    # Assert
    assert result == 80.0


def test_zero_discount():
    """Тест для нулевой скидки"""
    # Act
    result = calculate_discount(100.0, 0.0)
    
    # Assert
    assert result == 100.0


def test_full_discount():
    """Тест для 100% скидки"""
    # Act
    result = calculate_discount(100.0, 100.0)
    
    # Assert
    assert result == 0.0


def test_fractional_discount():
    """Тест для дробного процента скидки"""
    # Act
    result = calculate_discount(100.0, 25.5)
    
    # Assert
    # 100 - (100 * 25.5/100) = 100 - 25.5 = 74.5
    assert result == 74.5


def test_negative_discount_raises_error():
    """Тест на отрицательную скидку (должен вызвать ошибку)"""
    # Act & Assert
    with pytest.raises(ValueError, match="Скидка должна быть в диапазоне от 0 до 100%"):
        calculate_discount(100.0, -10.0)


def test_discount_above_100_raises_error():
    """Тест на скидку больше 100% (должен вызвать ошибку)"""
    # Act & Assert
    with pytest.raises(ValueError, match="Скидка должна быть в диапазоне от 0 до 100%"):
        calculate_discount(100.0, 150.0)


def test_rounding():
    """Тест на округление результата"""
    # Act
    result = calculate_discount(99.99, 33.33)
    
    # Assert
    # 99.99 - (99.99 * 33.33/100) = 99.99 - 33.326667 = 66.663333 ≈ 66.66
    assert result == 66.66


def test_with_different_prices():
    """Тест с разными ценами"""
    test_cases = [
        (50.0, 10.0, 45.0),   # 50 - 5 = 45
        (200.0, 25.0, 150.0), # 200 - 50 = 150
        (0.0, 50.0, 0.0),     # 0 - 0 = 0
    ]
    
    for price, discount, expected in test_cases:
        result = calculate_discount(price, discount)
        assert result == expected, f"Failed for price={price}, discount={discount}%"
