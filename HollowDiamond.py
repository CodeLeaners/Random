#    *
#   * *
#  *   *
# *     *
#  *   *
#   * *
#    *

# n is any random number 

n = 7
space = n//2
midspace = 1
result = []

result.append(" "*space + "*")

space -= 1
for i in range(n//2):
    result.append(" "*space + "*" + " "*midspace + "*")
    space -= 1
    midspace += 2

print(*result, sep="\n")
print(*result[:-1:][::-1], sep="\n")