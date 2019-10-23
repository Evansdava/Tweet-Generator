import timeit
# from dictionary_words import sentence


stmt = "sentence(10)"
setup = "from dictionary_words import sentence"
timer10 = timeit.Timer(stmt, setup=setup)

stmt = "sentence(100)"
timer100 = timeit.Timer(stmt, setup=setup)

stmt = "sentence(1000)"
timer1000 = timeit.Timer(stmt, setup=setup)

stmt = "sentence(10000)"
timer10000 = timeit.Timer(stmt, setup=setup)

stmt = "sentence(100000)"
timer100000 = timeit.Timer(stmt, setup=setup)

stmt = "sentence(100000)"
timer1000000 = timeit.Timer(stmt, setup=setup)

iterations = 10
result = timer10.timeit(number=iterations)
print("time for 10-word sentence: " + str(result))

result = timer100.timeit(number=iterations)
print("time for 100-word sentence: " + str(result))

result = timer1000.timeit(number=iterations)
print("time for 1000-word sentence: " + str(result))

result = timer10000.timeit(number=iterations)
print("time for 10000-word sentence: " + str(result))

result = timer100000.timeit(number=iterations)
print("time for 100000-word sentence: " + str(result))

result = timer1000000.timeit(number=iterations)
print("time for 1000000-word sentence: " + str(result))
