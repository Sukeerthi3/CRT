def reverse_number(n: int) -> int:
    return int(str(n)[::-1])

if __name__ == "_main_":
    n = int(input())
    print(reverse_number(n))