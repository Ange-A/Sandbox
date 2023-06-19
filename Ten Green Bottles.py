def ten_green_bottles():
    for bottles in range(10, 0, -1):
        print(f"{bottles} green bottles, hanging on the wall,")
        print(f"{bottles} green bottles, hanging on the wall,")
        print("And if one green bottle should accidentally fall,")
        print(f"There'll be {bottles - 1} green bottles hanging on the wall.\n")

ten_green_bottles()
