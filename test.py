import sys

N = 100

generator_iter = ((i, j, k) for i in range(N)
                  if i % 3 == 0
                  for j in range(N)
                  if j % 3 == 1
                  for k in range(N)
                  if k % 3 == 2
                  )
print(f"size of generator_iter: {sys.getsizeof(generator_iter)}")

print(generator_iter.__next__())
print(generator_iter.__next__())

generator_list = [(i, j, k) for i in range(N)
                  if i % 3 == 0
                  for j in range(N)
                  if j % 3 == 1
                  for k in range(N)
                  if k % 3 == 2
                  ]
print(f"size of generator_list: {sys.getsizeof(generator_list)}")
