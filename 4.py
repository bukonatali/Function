# Напишите декоратор, который будет считать, сколько раз была вызвана декорируемая функция


def simple_decore(a):
    def wrapper():
        global summa
        wrapper.count += 1
        return a()
    wrapper.count = 0
    return wrapper

@simple_decore
def f():
    print("Test function 1")
f()
f()
f()
f()
print(f.count)

