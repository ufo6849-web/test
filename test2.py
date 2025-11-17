import sys

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def greet(name: str) -> str:
    """주어진 이름으로 간단히 인사문을 반환합니다."""
    name = name.strip() or "손님"
    return f"안녕하세요, {name}님! 만나서 반가워요."

def main():
    try:
        if len(sys.argv) > 1:
            name = " ".join(sys.argv[1:])
            print(greet(name))
        else:
            name = input("이름을 입력하세요: ")
            print(greet(name))
    except (KeyboardInterrupt, EOFError):
        print("\n안녕히 가세요.")

if __name__ == "__main__":
    main()