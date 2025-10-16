def reverse_string(s):
    """Повертає рядок у зворотному порядку"""
    if not isinstance(s, str):
        raise TypeError("Очікується рядок")
    return s[::-1]

def count_words(sentence):
    """Підрахунок кількості слів у реченні"""
    if not isinstance(sentence, str):
        raise TypeError("Очікується рядок")
    return len(sentence.split())

def unique_values(seq):
    """Повертає унікальні значення зі списку"""
    if not isinstance(seq, list):
        raise TypeError("Очікується список")
    return list(set(seq))
