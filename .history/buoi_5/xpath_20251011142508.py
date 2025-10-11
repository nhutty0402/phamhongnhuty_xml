from lxml import etree
import os

def run_xpath(filename, queries, ns=None):
    print(f"\n------------------- KIỂM TRA FILE: {filename} ------------------------\n")
    path = os.path.join(os.getcwd(), filename)
    tree = etree.parse(path)
    root = tree.getroot()

    for desc, expr in queries:
        print(f" {desc}")
        print(f"🧭 XPath: {expr}")
        try:
            if 'nhiều hơn 1 lần' in desc:
                mamon_list = root.xpath('//q:CTHD/q:MAMON/text()', namespaces=ns)
                seen = {}
                for m in mamon_list:
                    seen[m] = seen.get(m, 0) + 1
                # lọc món xuất hiện >1
                mon_trung = [m for m, c in seen.items() if c > 1]
                if not mon_trung:
                    print('❌ Không có kết quả.\n')
                    continue
                # Lấy tên các món tương ứng
                for m in mon_trung:
                    ten = root.xpath(f"//q:MON[q:MAMON='{m}']/q:TENMON/text()", namespaces=ns)
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


# --- QUERIES ---
queries_sinhvien = [
    ("Lấy tất cả sinh viên", "//student"),
    ("Liệt kê tên tất cả sinh viên", "//student/name/text()"),
    ("Lấy tất cả id sinh viên", "//student/id/text()"),
    ("Lấy ngày sinh của sinh viên có id='SV01'", "//student[id='SV01']/date/text()"),
    ("Lấy tất cả các khóa học", "//enrollment/course/text()"),
    ("Lấy toàn bộ thông tin của sinh viên đầu tiên", "//student[1]/*/text()"),
    ("Lấy mã sinh viên đăng ký khóa học 'Vatly203'", "//enrollment[course='Vatly203']/studentRef/text()"),
    ("Lấy tên sinh viên học môn 'Toan101'", "//student[id=//enrollment[course='Toan101']/studentRef]/name/text()"),
    ("Lấy tên sinh viên học môn 'Vatly203'", "//student[id=//enrollment[course='Vatly203']/studentRef]/name/text()"),
    ("Lấy tên và ngày sinh của sinh viên sinh năm 1997", "//student[starts-with(date,'1997')]/name/text() | //student[starts-with(date,'1997')]/date/text()"),
    ("Lấy tên sinh viên có ngày sinh trước năm 1998", "//student[number(substring(date,1,4))<1998]/name/text()"),
    ("Đếm tổng số sinh viên", "count(//student)"),
    ("Lấy phần tử <date> ngay sau <name> của SV01", "//student[id='SV01']/name/following-sibling::date/text()"),
    ("Lấy phần tử <id> ngay trước <name> của SV02", "//student[name='Lê Thị Hồng Cẩm']/preceding-sibling::id/text()"),
    ("Lấy toàn bộ node <course> trong enrollment có studentRef='SV03'", "//enrollment[studentRef='SV03']/course/text()"),
    ("Lấy sinh viên có họ là 'Trần'", "//student[starts-with(name,'Trần')]/name/text()"),
    ("Lấy năm sinh của sinh viên SV01", "substring(//student[id='SV01']/date/text(),1,4)"),
    ("Lấy tất cả sinh viên chưa đăng ký môn nào", "//student[not(id=//enrollment/studentRef)]")
]

queries_quanan = [
    ("Lấy tất cả bàn", "//q:BAN"),
    ("Lấy tất cả nhân viên", "//q:NHANVIEN"),
    ("Lấy tất cả tên món", "//q:MON/q:TENMON/text()"),
    ("Lấy tên nhân viên có mã NV00000002", "//q:NHANVIEN[q:MANV='NV00000002']/q:TENNV/text()"),
    ("Lấy tên nhân viên NV00000003", "//q:NHANVIEN[q:MANV='NV00000003']/q:TENNV/text()"),
    ("Lấy số điện thoại nhân viên NV00000003", "//q:NHANVIEN[q:MANV='NV00000003']/q:SDT/text()"),
    ("Lấy tên món có giá > 50000", "//q:MON[q:GIA>50000]/q:TENMON/text()"),
    ("Lấy số bàn của hóa đơn SOHD=1003", "//q:HOADON[q:SOHD=1003]/q:TENBAN/text()"),
    ("Lấy tên món có mã MON0000002", "//q:MON[q:MAMON='MON0000002']/q:TENMON/text()"),
    ("Lấy ngày lập của hóa đơn SOHD=1003", "//q:HOADON[q:SOHD=1003]/q:NGAYLAP/text()"),
    ("Lấy tất cả mã món trong hóa đơn SOHD=1001", "//q:CTHD[q:SOHD=1001]/q:MAMON/text()"),
    ("Lấy tên món trong hóa đơn SOHD=1001", "//q:MON[q:MAMON=//q:CTHD[q:SOHD=1001]/q:MAMON]/q:TENMON/text()"),
    ("Lấy tên nhân viên lập hóa đơn SOHD=1002", "//q:NHANVIEN[q:MANV=//q:HOADON[q:SOHD=1002]/q:MANV]/q:TENNV/text()"),
    ("Đếm số bàn", "count(//q:BAN)"),
    ("Đếm số hóa đơn lập bởi NV00000001", "count(//q:HOADON[q:MANV='NV00000001'])"),
    ("Lấy tên tất cả món có trong hóa đơn bàn số 2", "//q:MON[q:MAMON=//q:CTHD[q:SOHD=//q:HOADON[q:TENBAN='BAN0000002']/q:SOHD]/q:MAMON]/q:TENMON/text()"),
    ("Lấy tất cả nhân viên từng lập hóa đơn cho bàn số 3", "//q:NHANVIEN[q:MANV=//q:HOADON[q:TENBAN='BAN0000003']/q:MANV]/q:TENNV/text()"),
    ("Lấy tất cả hóa đơn mà nhân viên nữ lập", "//q:HOADON[q:MANV=//q:NHANVIEN[q:GIOITINH='Nữ']/q:MANV]"),
    ("Lấy tất cả nhân viên từng phục vụ bàn số 1", "//q:NHANVIEN[q:MANV=//q:HOADON[q:TENBAN='BAN0000001']/q:MANV]/q:TENNV/text()"),
    ("Lấy tất cả món được gọi nhiều hơn 1 lần", ""),  # ✅ xử lý đặc biệt trong code
    ("Lấy tên bàn của hóa đơn SOHD=1002", "//q:HOADON[q:SOHD=1002]/q:TENBAN/text()"),
    ("Lấy ngày lập hóa đơn SOHD=1002", "//q:HOADON[q:SOHD=1002]/q:NGAYLAP/text()")
]

if __name__ == "__main__":
    print(f"📂 Đang chạy tại: {os.getcwd()}")
    run_xpath("sinhvien.xml", queries_sinhvien)
    run_xpath("quanlybanan.xml", queries_quanan, ns={'q': 'http://example.com/quanan'})
    input("Nhấn Enter để thoát...")