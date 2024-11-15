import re

# Compilando a expressão regular
pattern = re.compile('value[^"]*')

# String exemplo para correspondência
html_string = ("<span class=""icon" + ">R$</span> " + "<strong class=""value" + ">5,09</strong>" )


# Usando o padrão para encontrar correspondências
matches = pattern.findall(html_string)

# Exibindo as correspondências
print(matches)
