def test1(age: int) -> bool:
    return age > 18

def converter(cm: float) -> float:
    if cm == str:
        raise TypeError("ееее куди")
    result = cm/2.54
    return result.__round__(2)