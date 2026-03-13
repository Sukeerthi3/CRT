def count_digits(n: int) -> int:
    return len(str(abs(n)))

if __name__ == "_main_":
    n = int(input())
    print(count_digits(n))