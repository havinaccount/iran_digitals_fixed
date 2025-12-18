import os

# Making a dictionary with a fixed number for saving info
phone_book: dict[str, list[str]] = {
    "sara": ["09011111111"]
}

def terminal_cleanup():
    """
    The function `terminal_cleanup` clears the terminal screen based on the operating system.
    """
    os.system("clear" if os.name == "posix" else 'cls')

# App's main menu
menu_text: str = """
--- دفترچه تلفن ---
1- افزودن مخاطب
2- افزودن شماره به مخاطب
3- جستجوی شماره تلفن با اسم
4- حذف مخاطب
5- تعداد مخاطبین
6- خروج
"""

terminal_cleanup()

# Infinite loop for repeating the contacts app
while True:

    # Get input from user
    user_choice: str = input(menu_text)
    match user_choice:
        
    # Check if user is exiting
        case "6":
            terminal_cleanup()
            print("خداحافظ\n")
            break

    # Make a add contact feature
        case "1":
            name: str = input("اسم مخاطب رو وارد کن: ")
            if name in phone_book:
                result_message: str = "مخاطبی با این نام از قبل وجود داره"
            else:
                number: str = input("شماره تلفن رو وارد کن: ")
                phone_book[name] = [number]
                result_message: str = "مخاطب با موفقیت اضافه شد"

    # Make a adding other numbers to contacts feature
        case "2":
            name: str = input("اسم مخاطب رو وارد کن: ")
            if name not in phone_book:
                result_message: str = "مخاطبی با این نام پیدا نشد"
            else:
                number: str = input("شماره جدید رو وارد کن: ")
                phone_book[name].append(number)
                result_message: str = "شماره جدید اضافه شد"

    # Search the contact using it's name
        case "3":
            name: str = input("اسم مخاطب رو وارد کن: ")
            if name in phone_book:
                result_message: str = str(phone_book[name])
            else:
                result_message: str = "مخاطبی با این نام پیدا نشد"

    # Add a user deleting feature
        case "4":
            name: str = input("اسم مخاطب رو وارد کن: ")
            if name in phone_book:
                del phone_book[name]
                result_message: str = "مخاطب حذف شد"
            else:
                result_message: str = "مخاطبی با این نام پیدا نشد"

    # Show how many contacts are registered
        case "5":
            result_message: str = "تعداد مخاطب‌ها: " + str(len(phone_book))

    # Manage a unknown choice
        case _:
            result_message: str = "ورودی باید مقداری بین 1 تا 6 باشه"

    # Check if the user wants to continue using the app
    result_message += "\n - آیا می‌خوای ادامه بدی؟ (بله/خیر): "

    cont: str = input(result_message)
    if cont == ["خیر", ""] or cont.upper() == "N":
        terminal_cleanup()
        print("خداحافظ\n")
        break
