from collections import deque

def is_palindrome(input_string):
    cleaned = ''.join(c.lower() for c in input_string if c.isalnum())
    d = deque(cleaned)

    while len(d) > 1:
        left = d.popleft()
        right = d.pop()
        if left != right:
            return False
    return True

def main():
    text = input("Введи рядок для перевірки на паліндром: ")
    if is_palindrome(text):
        print("Так, це паліндром")
    else:
        print("Ні, це не паліндром")

if __name__ == "__main__":
    main()
