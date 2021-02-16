


resultados = [ ["Alfredo",20], ["Marcela",50], ["Ignacio",30], ["Loreto",10] ]



def cuantas(elem, conjunto):
  contador = 0
  for k in range(len(conjunto)):
    if conjunto[k] == elem:
      contador += 1
  return contador


print(cuantas("a","palabrata"))