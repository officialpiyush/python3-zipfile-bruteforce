from zipfile import ZipFile

with open("passwords.txt") as f:
    passwords = f.readlines()


def main():
    for password in passwords:
        try:
            with ZipFile("helloworld.zip") as z:
                z.extractall(pwd=bytes(password.strip("\n"), "utf-8"))
                print(f"\n\nThe password is - {password}")
                break
        except Exception as e:
            print(f"Extraction failed with password - {password}")
            pass


if __name__ == "__main__":
    main()
