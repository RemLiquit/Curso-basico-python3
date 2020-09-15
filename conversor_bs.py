bolivianos = input('Cuantos bolivianos tienes?')
bolivianos = float(bolivianos)
dolares = 6.91
dolares = bolivianos / dolares
dolares = round(dolares, 2)
dolares = str(dolares)

print('Tienes $' + dolares + 'dolares')
