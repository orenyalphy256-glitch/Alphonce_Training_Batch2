def greet(name):
    return f"Hello, {name}"

def multiply(a, b):
    return a * b

if __name__ == "__main__":
    user = input("Your name: ")
    print(greet(user))
    print("3 * 4 =", multiply(3, 4))
        