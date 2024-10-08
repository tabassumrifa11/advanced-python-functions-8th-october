print("\033c")

number = [1,2,3,4,5,6]
even = [i for i in number if i%2==0]
print(even)


def sq (n):
    return n*n
num = [1, 2, 4, 6, 5, 7, 9]

square = map(sq, num)
print(  list(square)  )



n1 = [1, 2, 4]
n2 = [5, 6, 8]

result = map( lambda x,y: x+y,  n1,n2)
print(  list(result)  )