def banner(slogan: str) -> str:
    return slogan.upper()


if __name__ == '__main__':
    repeat_count = int(input("Mitu korda soovid sloganit korrata? "))
    slogan = input("Milline on sinu slogan? ")
    banner_text = banner(slogan)
    print(f"{banner_text}\n" * repeat_count)