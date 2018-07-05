print('Ingresar un numero')
n = int(input())

def row(n, min):
  v = []
  count = n
  while count > 1:
    if min > count:
      v.append(min)
    else:
      v.append(count)
    count -= 1

  while count <= n:
    if min > count:
      v.append(min)
    else:
      v.append(count)
    count += 1

  print(v)
  return v

def colum(n):

  m = []
  count = n

  while count > 1:
    m.append(row(n, count))
    count -= 1

  while count <= n:
    m.append(row(n, count))
    count += 1
  return m

colum(n)