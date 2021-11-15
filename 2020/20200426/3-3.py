n = int(input())

word_list = [input() for i in range(n)]
l = len(set(word_list))
        
print(l)