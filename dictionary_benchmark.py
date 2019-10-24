import timeit
from sys import argv


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

stmt = "sentence(1000000)"
timer1000000 = timeit.Timer(stmt, setup=setup)

iterations = int(argv[1])
result = round(timer10.timeit(number=iterations) * 1000 / iterations)
print("Average time for 10-word sentence: " + str(result) + " ms")

result = round(timer100.timeit(number=iterations) * 1000 / iterations)
print("Average time for 100-word sentence: " + str(result) + " ms")

result = round(timer1000.timeit(number=iterations) * 1000 / iterations)
print("Average time for 1000-word sentence: " + str(result) + " ms")

result = round(timer10000.timeit(number=iterations) * 1000 / iterations)
print("Average time for 10000-word sentence: " + str(result) + " ms")

result = round(timer100000.timeit(number=iterations) * 1000 / iterations)
print("Average time for 100000-word sentence: " + str(result) + " ms")

result = round(timer1000000.timeit(number=iterations) * 1000 / iterations)
print("Average time for 1000000-word sentence: " + str(result) + " ms")
