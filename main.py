from DataBase import connect
import named_tuples


def run():
    while True:
        command = input("\nBuyruqlar ro'yxati:\n\n"
                        "1. Show Models       - Mashina modellari va ularning ranglarini ko'rsatish\n"
                        "2. Show Emails       - Mijozlarning e-mail manzillarini ko'rsatish\n"
                        "3. Show Country      - Mijozlarning davlatlarini ko'rsatish\n"
                        "4. Show Employees    - Har bir davlatdagi xodimlar sonini ko'rsatish\n"
                        "5. Show Brands       - Brandlar va ularning modellari sonini ko'rsatish\n"
                        "6. Show Brands (Filter) - Modellari soni 5 dan yuqori bo'lgan brandlarni ko'rsatish\n"
                        "7. Show Tables       - Barcha jadvallarni ko'rsatish\n"
                        "8. Show Sums         - Modellarning umumiy narxini ko'rsatish\n"
                        "9. Show Brand Counts - Har bir branddagi modellarning sonini ko'rsatish\n"
                        "10. Add Brand        - Yangi brand qo'shish\n"
                        "11. Add Color        - Yangi color qo'shish\n"
                        "12. Add Model        - Yangi model qo'shish\n"
                        "\nO'zingizga kerakli buyruqni kiriting: ").lower()
        if command == "show models":
            named_tuples.showModels()

        elif command == "show emails":
            named_tuples.showEmails()

        elif command == "show country":
            named_tuples.showCountry()

        elif command == "show employees":
            named_tuples.showEmployees()

        elif command == "show brands":
            named_tuples.showBrands()

        elif command == "show brands (filter)":
            named_tuples.showBrandsFilter()

        elif command == "show tables":
            named_tuples.showOrders()

        elif command == "show sums":
            named_tuples.sum_models()

        elif command == "show brand counts":
            named_tuples.brandCounts()

        elif command == "add brand":
            name = input("Brand nomini kiriting: ").title()
            connect.insert_brands(name)
            print(f"\n{name} muvaffaqiyatli qo'shildi!")

        elif command == "add color":
            color = input("Color nomini kiriting: ").title()
            connect.insert_colors(color)
            print(f"{color} muvaffaqiyatli qo'shildi!")

        elif command == "add model":
            name = input("Model nomini kiriting: ").title()
            price = input("Model narxini kiriting: ")
            try:
                price = float(price)
            except ValueError:
                print("Xato! Narx faqat son bo'lishi kerak.")
                continue
            named_tuples.show_all_brands()
            brand_id = input("Brand ID'sini kiriting: ")
            if not brand_id.isdigit():
                print("Xato! Brand ID faqat raqam bo'lishi kerak.")
                continue
            brand_id = int(brand_id)
            named_tuples.show_colors()
            color_id = input("Color ID'sini kiriting: ")
            if not color_id.isdigit():
                print("Xato! Color ID faqat raqam bo'lishi kerak.")
                continue
            color_id = int(color_id)
            count = input("Mashina sonini kiriting: ")
            try:
                count = int(count)
            except ValueError:
                print("Xato! Mashina soni faqat butun son bo'lishi kerak.")
                continue
            connect.insert_models(name, price, brand_id, color_id, count)
            print(f"{name} - muvaffaqiyatli qo'shildi!")


if __name__ == '__main__':
    run()
