from lxml import etree
import os

def run_xpath(filename, queries, ns=None):
    print(f"\n------------------- KIỂM TRA: {filename} ------------------------\n")
    path = os.path.join(os.getcwd(), filename)
    tree = etree.parse(path)
    root = tree.getroot()

    for desc, expr in queries:
        print(f"👉 {desc}")
        print(f"🧭 XPath: {expr}")
        try:
            if 'nhiều hơn 1 lần' in desc:
                # SỬA: Sum SOLUONG thay vì chỉ count CTHD
                from collections import defaultdict
                dish_count = defaultdict(int)
                cthds = root.xpath('//q:CTHD', namespaces=ns)
                for cthd in cthds:
                    mamon = cthd.xpath('./q:MAMON/text()', namespaces=ns)[0]
                    soluong = int(cthd.xpath('./q:SOLUONG/text()', namespaces=ns)[0])
                    dish_count[mamon] += soluong
                mon_trung = [m for m, c in dish_count.items() if c > 1]
                if not mon_trung:
                    print('❌ Không có kết quả.\n')
                    continue
                for m in mon_trung:
                    ten = root.xpath(f"//q:MON[q:MAMON/text()='{m}']/q:TENMON/text()", namespaces=ns)
                    for t in ten:
                        print(' -', t)
                print()
                continue

            result = root.xpath(expr, namespaces=ns)

            # Nếu kết quả là số
            if isinstance(result, float):
                print(" -", int(result) if result.is_integer() else result)
                print()
                continue

            # Nếu rỗng
            if not result:
                print("❌ Không có kết quả.\n")
                continue

            # In kết quả
            for r in result:
                if isinstance(r, etree._Element):
                    print(" -", etree.tostring(r, encoding='unicode', pretty_print=True).strip())
                else:
                    print(" -", r)
            print()

        except Exception as e:
            print(f"⚠️ Lỗi: {e}\n")

# Queries sửa (chỉ 2 query cần thay)
queries_sinhvien = [  # Giữ nguyên
    # ... (giữ nguyên như cũ)
]

queries_quanan = [
    ("Lấy tất cả bàn", "//q:BAN"),
    ("Lấy tất cả nhân viên", "//q:NHANVIEN"),
    ("Lấy tất cả tên món", "//q:MON/q:TENMON/text()"),
    ("Lấy tên nhân viên có mã NV00000002", "//q:NHANVIEN[q:MANV/text()='NV00000002']/q:TENNV/text()"),
    ("Lấy tên nhân viên NV00000003", "//q:NHANVIEN[q:MANV/text()='NV00000003']/q:TENNV/text()"),
    ("Lấy số điện thoại nhân viên NV00000003", "//q:NHANVIEN[q:MANV/text()='NV00000003']/q:SDT/text()"),
    ("Lấy tên món có giá > 50000", "//q:MON[number(q:GIA/text()) > 50000]/q:TENMON/text()"),  # SỬA: number() và /text()
    ("Lấy số bàn của hóa đơn SOHD=1003", "//q:BAN[q:TENBAN=//q:HOADON[q:SOHD/text()='1003']/q:TENBAN]/q:SOBAN/text()"),  # SỬA: Join lấy SOBAN
    ("Lấy tên món có mã MON0000002", "//q:MON[q:MAMON/text()='MON0000002']/q:TENMON/text()"),  # Thêm /text() cho an toàn
    ("Lấy ngày lập của hóa đơn SOHD=1003", "//q:HOADON[q:SOHD/text()='1003']/q:NGAYLAP/text()"),
    ("Lấy tất cả mã món trong hóa đơn SOHD=1001", "//q:CTHD[q:SOHD/text()='1001']/q:MAMON/text()"),
    ("Lấy tên món trong hóa đơn SOHD=1001", "//q:MON[q:MAMON/text() = //q:CTHD[q:SOHD/text()='1001']/q:MAMON/text()]/q:TENMON/text()"),
    ("Lấy tên nhân viên lập hóa đơn SOHD=1002", "//q:NHANVIEN[q:MANV/text() = //q:HOADON[q:SOHD/text()='1002']/q:MANV/text()]/q:TENNV/text()"),
    ("Đếm số bàn", "count(//q:BAN)"),
    ("Đếm số hóa đơn lập bởi NV00000001", "count(//q:HOADON[q:MANV/text()='NV00000001'])"),
    ("Lấy tên tất cả món có trong hóa đơn bàn số 2", "//q:MON[q:MAMON/text()=//q:CTHD[q:SOHD/text()=//q:HOADON[q:TENBAN/text()='BAN0000002']/q:SOHD/text()]/q:MAMON/text()]/q:TENMON/text()"),
    ("Lấy tất cả nhân viên từng lập hóa đơn cho bàn số 3", "//q:NHANVIEN[q:MANV/text()=//q:HOADON[q:TENBAN/text()='BAN0000003']/q:MANV/text()]/q:TENNV/text()"),
    ("Lấy tất cả hóa đơn mà nhân viên nữ lập", "//q:HOADON[q:MANV/text()=//q:NHANVIEN[q:GIOITINH/text()='Nữ']/q:MANV/text()]"),
    ("Lấy tất cả nhân viên từng phục vụ bàn số 1", "//q:NHANVIEN[q:MANV/text()=//q:HOADON[q:TENBAN/text()='BAN0000001']/q:MANV/text()]/q:TENNV/text()"),
    ("Lấy tất cả món được gọi nhiều hơn 1 lần", ""),  # Đã sửa trong hàm
    ("Lấy tên bàn của hóa đơn SOHD=1002", "//q:HOADON[q:SOHD/text()='1002']/q:TENBAN/text()"),
    ("Lấy ngày lập hóa đơn SOHD=1002", "//q:HOADON[q:SOHD/text()='1002']/q:NGAYLAP/text()")
]

if __name__ == "__main__":
    print(f"📂 Đang chạy tại: {os.getcwd()}")
    run_xpath("sinhvien.xml", queries_sinhvien)
    run_xpath("quanlybanan.xml", queries_quanan, ns={'q': 'http://example.com/quanan'})
    # input("Nhấn Enter để thoát...")  # Comment nếu cần