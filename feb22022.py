primes = [2, 3, 5, 7, 11]
empty_list = []

non_primes = [4, 6, 8, 9, 10 ]
numbers = primes + non_primes
numbers.sort(reverse = True)

primes.append(13)

names = ["Bob", "Alisya", "Katherine"]
mixed = ["Bob", 13]

"Bob -> 0 index"
"Alisya -> 1 index"
"Katherine -> 2 index/-1 index"

boy = names[0]
print(boy)

alisya = names[1]
print(alisya)

katherine = names[-1]
print(katherine)

a_and_k = names[1:3]
b_and_a_and_k = names[0:]
print(a_and_k)
print(b_and_a_and_k)

"2D Lists"

p_np = [[2, 1], [3, 4], [5, 6]]
index = p_np[2][1]
print(index)

".remove()", ".count()", "len()", ".pop()"

def long_words(n, str):
    word_len = []
    txt = str.split(" ")
    for x in txt:
        if len(x) > n:
           word_len.append(x)
    return word_len

print(long_words(3, "The fast zombie switches"))
    
