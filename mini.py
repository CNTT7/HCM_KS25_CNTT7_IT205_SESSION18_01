def display_orders(orders):
    if not orders:
        print("ERR-02: Danh sach don hang trong.")
        return

    print(f"{'Ma HD':<10}{'Ten Dai Ly':<25}{'Gia Tri':>15}{'Trang Thai':>15}")
    print("-" * 65)

    for order in orders:
        print(
            f"{order['id']:<10}"
            f"{order['name']:<25}"
            f"{order['price']:>15,}"
            f"{order['status']:>15}"
        )


def add_order(orders):
    while True:
        order_id = input("Nhap ma don hang: ").strip()
        if order_id:
            break
        print("Ma don hang khong duoc de trong.")

    for order in orders:
        if order["id"] == order_id:
            print("ERR-01: Ma don hang da ton tai.")
            return

    while True:
        agency_name = input("Nhap ten dai ly: ").strip()
        if agency_name:
            break
        print("Ten dai ly khong duoc de trong.")

    while True:
        try:
            price = int(input("Nhap gia tri don hang: "))
            if price > 0:
                break
            print("Gia tri don hang phai lon hon 0.")
        except ValueError:
            print("Vui long nhap so nguyen hop le.")

    orders.append(
        {
            "id": order_id,
            "name": agency_name,
            "price": price,
            "status": "Unpaid"
        }
    )

    print("Them moi don hang thanh cong.")


def update_payment_status(orders):
    order_id = input("Nhap ma don hang can cap nhat: ").strip()

    for order in orders:
        if order["id"] == order_id:
            if order["status"] == "Paid":
                print("ERR-04: Don hang da duoc thanh toan truoc do.")
                return

            order["status"] = "Paid"
            print("Cap nhat trang thai thanh toan thanh cong.")
            return

    print("ERR-03: Khong tim thay ma don hang.")


def calculate_revenue(orders):
    total_revenue = 0

    for order in orders:
        if order["status"] == "Paid":
            total_revenue += order["price"]

    discount_percent = 5 if total_revenue >= 100_000_000 else 0
    discount_amount = total_revenue * discount_percent / 100

    return total_revenue, discount_percent, discount_amount


def main():
    orders = [
        {
            "id": "HD01",
            "name": "Dai ly Hoang Long",
            "price": 45000000,
            "status": "Paid"
        },
        {
            "id": "HD02",
            "name": "Tap hoa Minh Thu",
            "price": 15000000,
            "status": "Unpaid"
        }
    ]

    while True:
        print("\n===== HE THONG QUAN LY DON HANG DAI LY =====")
        print("1. Xem danh sach don hang")
        print("2. Tao moi don hang")
        print("3. Cap nhat trang thai thanh toan")
        print("4. Tinh tong doanh thu & Chiet khau")
        print("5. Thoat")

        try:
            choice = int(input("Nhap lua chon: "))
        except ValueError:
            print("Vui long nhap so tu 1 den 5.")
            continue

        if choice == 1:
            display_orders(orders)

        elif choice == 2:
            add_order(orders)

        elif choice == 3:
            update_payment_status(orders)

        elif choice == 4:
            total_revenue, discount_percent, discount_amount = calculate_revenue(orders)

            print("\n===== BAO CAO DOANH THU =====")
            print(f"Tong doanh thu: {total_revenue:,.0f} VND")
            print(f"Ty le chiet khau: {discount_percent}%")
            print(f"So tien chiet khau: {discount_amount:,.0f} VND")

        elif choice == 5:
            print("Cam on ban da su dung chuong trinh.")
            break

        else:
            print("Lua chon khong hop le. Vui long chon tu 1 den 5.")


main()