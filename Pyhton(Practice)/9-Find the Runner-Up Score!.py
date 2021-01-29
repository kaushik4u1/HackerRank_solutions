if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    a=sorted(list(set(arr))) #Sets  cannot have multiple occurrences of the same element and store unordered values.
    print(a[-2])
