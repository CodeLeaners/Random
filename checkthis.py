def letterN(n):
    result = []
    stars = 2
    midspace = n-2

    result.append("*" + " "*midspace + "*")
    midspace -=1

    result.append("**" + " "*midspace + "*")

    midspace -= 1
    space = 1
    for i in range(n//2):
        result.append("*" + " "*space + "*" + " "*midspace+ "*")
        midspace -= 1
        space += 1
    
    result.append("*" + " "*space + "*")
    
    return result

def letterL(n):
    result = []
    space = n-1
    stars = n

    for _ in range(n-1):
        result.append("*"+" "*space)
    result.append("*"*stars)

    return result

def letterW(n):
    result = []
    midspace = n*3 -3
    space = 0
    
    for _ in range(n//2-1):
        result.append(" "*space + "*" + " "*midspace + "*" + " "*space)
        midspace -= 2
        space += 1

    midspace = midspace//2
    result.append(" "*space + "*" + " "*midspace + "*" + " "*midspace + "*" + " "*space)
    midspace -= 2
    space += 1

    middspace = 1
    for _ in range(n//2 -1):
        result.append(" "*space + "*" + " "*midspace + "*" + " "*middspace + "*" + " "*midspace + "*" + " "*space)
        space += 1
        midspace -= 2
        middspace += 2

    result.append(" "*space + "*" + " "*middspace+ "*" + " "*space)

    return result

def letterI(n):
    result= []
    stars = n+2
    space = stars//2 -1
    lastspace = stars - space+1
    result.append("*"*stars)
    
    for i in range(n-2):
        result.append(" "*space + "*" + " "*lastspace)
    
    result.append("*"*stars)
    return result



    print(*result, sep="\n")

def letterJ(n):
    result = []
    stars = n
    space = n//2

    result.append("*"*stars)

    lastspace = stars-space-1
    for _ in range(n-3):
        result.append(" "*space+"*" + " "*lastspace)
    
    space-=1
    result.append("*" + " "*space+"*" + " "*lastspace)

    space+=2
    result.append("*"*space + " "*lastspace)

    # print(*result, sep="\n")
    return result

def letterR(n):
    result = []
    stars = n
    space = n-2
    
    result.append("*"*stars)
    
    for _ in range(n//2 -2):
        result.append("*" + " "*space + "*")

    result.append("*"*stars)
    space = 1

    lastspace = n-3
    for _ in range(n//2):
        result.append("*" + " "*space + "*" + " "*lastspace)
        space += 1
        lastspace -= 1
    return result

def letterP(n):
    result = []
    stars = n+1
    space = stars-2

    result.append("*"*stars)
    
    for i in range(n//2 -2):
        result.append("*" + " "*space + "*")
    
    result.append("*"*stars)
    space+=1
    for i in range(n//2):
        result.append("*" + " "*space)
    
    return result

def letterA(n):
    result = []
    space = n-1
    midspace = 1
    
    result.append(" "*space + "*" + " "*space )
    space -= 1

    for i in range(n//2 -1):
        result.append(" "*space + "*" + " "*midspace + "*" + " "*space)
        space -= 1
        midspace += 2

    midspace += 2
    result.append(" "*space + "*"*midspace + " "*space)
    space -= 1

    for i in range(n//2 -1):
        result.append(" "*space + "*" + " "*midspace + "*" + " "*space)
        space -= 1
        midspace += 2

    return result

def letterO(n):
    space = n//2
    midspace = 1
    lastspace = (n//2)-1
    result = []

    result.append(" "*space + "*" + " "*lastspace)
    lastspace -= 1

    space -= 1
    for i in range(n//2):
        result.append(" "*space + "*" + " "*midspace + "*" + " "*lastspace)
        space -= 1
        midspace += 2
        lastspace -= 1

    result.extend(result[::-1])
        
    return result

def patternAppender(*patterns):
    finalPattern = []
    for i in range(len(patterns[0])):
        iThElements = [p[i] for p in patterns]
        finalPattern.append(' '.join(iThElements))
    return finalPattern

n = 6

finalResult = patternAppender(letterP(n), letterR(n), letterA(n), letterJ(n), letterJ(n), letterA(n), letterW(n), letterA(n), letterL(n))
print(*finalResult, sep="\n")