def number_generator(n):
    for i in range(n):
        print("inside coroutine", i)
        yield i
        print("after yield", i)

gen = number_generator(5)

print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))