def check_vowels():
    # Código a implementar utilizando input.


# Para verificar este ejercicio ejecutar el comando
# `pytest tp3_in_string_test.py` o `python tp3_in_string_test.py`
    nombre = input()
    nombre = nombre.lower()
    print(f"Contiene a: {"a" in nombre}")
    print(f"Contiene e: {"e" in nombre}")
    print(f"Contiene i: {"i" in nombre}")
    print(f"Contiene o: {"o" in nombre}")
    print(f"Contiene u: {"u" in nombre}")
