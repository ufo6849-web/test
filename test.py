# -*- coding: utf-8 -*-
"""
간단한 계산기 프로그램
GitHub 연습용 프로젝트
"""

def add(a, b):
    """두 숫자를 더합니다."""
    return a + b

def subtract(a, b):
    """두 숫자를 뺍니다."""
    return a - b

def multiply(a, b):
    """두 숫자를 곱합니다."""
    return a * b

def divide(a, b):
    """두 숫자를 나눕니다."""
    if b == 0:
        return "0으로 나눌 수 없습니다!"
    return a / b

def main():
    """메인 함수"""
    print("=== 간단한 계산기 ===")
    print("1. 덧셈")
    print("2. 뺄셈")
    print("3. 곱셈")
    print("4. 나눗셈")
    print("5. 종료")

    while True:
        choice = input("\n원하는 연산을 선택하세요 (1-5): ")

        if choice == '5':
            print("프로그램을 종료합니다.")
            break

        if choice in ['1', '2', '3', '4']:
            try:
                num1 = float(input("첫 번째 숫자를 입력하세요: "))
                num2 = float(input("두 번째 숫자를 입력하세요: "))

                if choice == '1':
                    result = add(num1, num2)
                    print(f"결과: {num1} + {num2} = {result}")
                elif choice == '2':
                    result = subtract(num1, num2)
                    print(f"결과: {num1} - {num2} = {result}")
                elif choice == '3':
                    result = multiply(num1, num2)
                    print(f"결과: {num1} × {num2} = {result}")
                elif choice == '4':
                    result = divide(num1, num2)
                    print(f"결과: {num1} ÷ {num2} = {result}")
            except ValueError:
                print("올바른 숫자를 입력해주세요!")
        else:
            print("올바른 선택지를 입력해주세요 (1-5)")

if __name__ == "__main__":
    main()
