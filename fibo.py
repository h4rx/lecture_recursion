def recursive_nth_fibo(n):
    if n <= 1:
        return n
    else:
        return (recursive_nth_fibo(n - 1) + recursive_nth_fibo(n - 2))


def main():
    n = int(input("Number of Fibonacci elements: "))
    fibo = recursive_nth_fibo(n)
    seq = []
    """
    for i in range(n):
        n_fibo = recursive_nth_fibo(i)
        seq.append(n_fibo)
    """
    seq = [recursive_nth_fibo(i) for i in range(n)]
    print(seq)

if __name__ == "__main__":
    main()
