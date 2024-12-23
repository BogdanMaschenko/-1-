import sys
from math import sqrt


def check_coef(coeff):
    try:
        float(coeff)
    except:
        print('Введено некоректное значение коэффициента.')
        return False
    return True

def get_coef(index, prompt):
    while 1:
        try:
            coef_str = sys.argv[index]
        except:
            print(prompt)
            coef_str = input()
        if check_coef(coef_str):
            coef = float(coef_str)
            return coef


def get_roots(a, b, c):
    result = []
    D = b * b - 4 * a * c
    if D == 0.0:
        root = -b / (2.0 * a)
        if root >= 0:
            sq_root = sqrt(root)
            result.append((sq_root, -sq_root))
    elif D > 0.0:
        sqD = sqrt(D)
        root1 = (-b + sqD) / (2.0 * a)
        root2 = (-b - sqD) / (2.0 * a)
        if root1 >= 0:
            sq_root1 = sqrt(root1)
            result.append((sq_root1, -sq_root1))
        elif root2 >= 0:
            sq_root2 = sqrt(root2)
            result.append((sq_root2, -sq_root2))
    return result


def main():
    a = get_coef(1, 'Введите коэффициент А:')
    b = get_coef(2, 'Введите коэффициент B:')
    c = get_coef(3, 'Введите коэффициент C:')
    roots = get_roots(a, b, c)
    len_roots = len(roots)
    if len_roots == 0:
        print('Нет корней')
    elif len_roots == 1:
        print('Пара корней: {}'.format(roots[0]))
    elif len_roots == 2:
        print('Две пары корней: {} и {}'.format(roots[0], roots[1]))


if __name__ == "__main__":
    main()
