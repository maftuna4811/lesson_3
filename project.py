import login
import register


def main():
    landing = input("""
         1.Login
         2.Register
             -->>>> """)

    if landing == "1":
        return login.login()

    elif landing == "2":
        return register.register()

    else:
        print("Error!!!")
        return main()


if __name__ == "__main__":
    main()