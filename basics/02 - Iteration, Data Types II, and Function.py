"""

1. Looping
    For loop
    While loop

2. Tipe Data
    List

    Tuple
    Set
    Dictionary

    Comprehension

3. Function

"""

"""

for (int i=0; i<10; i++) {
    cout << i;
}

"""

# range(nilai_akhir)
# for i in range(10):
#     print(i)

# range(nilai_awal, nilai_akhir)
#       inclusive,  exclusive
# for i in range(11, 20):
#     print(i)

# range(nilai_awal, nilai_akhir, step)
# for i in range(100, 110, 2):
#     print(i)



# Mencari Bilangan Prima

primes = []

for i in range(2, 10):

    counter = 0
    j = 1

    for j in range(j, i+1):
        if (i % j == 0):
            counter += 1

    if counter <= 2:
        primes.append(i)

print(primes)



"""

Study Club SI

["S", "t", "u" .. " ", .." "S", "I"]

"""

# name = "Study Club SI"

# for c in name:
#     print(c)

# int primes[10] = {2, 3, 5, 7, ..}

primes = [3, 5, 7, 11, 2, 13, 17, 19, 'ini bukan angka']
        # 0, 1, 2, 3, 4, ...

primes.append(29)
primes.append(23)
primes.append(100)

primes.remove('ini bukan angka')
primes.remove(100)

print(primes)

primes.sort(reverse=True)
print(primes)


# Sorting a string

name = "Study Club SI 2021"
list_name = list(name)

list_name.sort()
print(list_name)

"""

1. Simbol
2. Numerik
3. Huruf KAPITAL
4. Huruf non-kapital

"""






