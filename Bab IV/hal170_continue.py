# @igmerwina
# Bab III - Contoh Continue
""" Kurang paham :o """

from __future__ import print_function

def main():
    for i in range(1,11):
        if i % 2 == 0:  #genap
            continue

        # ngeprin bilangan ganjil
        print(i, end='\t')

if __name__ == "__main__":
    main()
