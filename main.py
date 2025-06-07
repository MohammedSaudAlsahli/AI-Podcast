import httpx


def main():
    a = httpx.get("https://google.com")
    print(a.status_code)


if __name__ == "__main__":
    main()
