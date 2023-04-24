def recursive_nth_fibo(n):
    if n <= 1:
        return n
    else:
        return (recursive_nth_fibo(n - 1) + recursive_nth_fibo(n - 2))


def main():
    fibo = recursive_nth_fibo(5)
    print(fibo)

if __name__ == "__main__":
    main()
