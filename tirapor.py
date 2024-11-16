# String representando a porcentagem
percent_str = "10.10%"

# Remover o símbolo de porcentagem
percent_without_symbol = percent_str.strip('%')

# Converter para float
percent_float = float(percent_without_symbol)
print(percent_without_symbol)
# Converter para inteiro
integer_value = int(percent_float)

print(f'O valor inteiro de {percent_str} é {integer_value}.')  # Saída: O valor inteiro de 10% é 10.
