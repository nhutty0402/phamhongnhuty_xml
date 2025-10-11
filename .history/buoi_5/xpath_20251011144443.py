import os
from lxml import etree
from collections import defaultdict

def run_xpath(filename, queries, ns=None):
    """
    Chạy các query XPath trên file XML.
    - Đối với query đặc biệt (xpath == ""), xử lý bằng Python.
    """
    try:
        tree = etree.parse(filename)
        root = tree.getroot()
        for label, xpath in queries:
            if xpath == "":  # Query đặc biệt: Lấy tất cả món được gọi nhiều hơn 1 lần
                # Thu thập tất cả CTHD, group theo MAMON, sum SOLUONG
                cthds = root.xpath("//q:CTHD", namespaces=ns)
                dish_count = defaultdict(int)
                for cthd in cthds:
                    mamon = cthd.xpath("./q:MAMON/text()", namespaces=ns)[0]
                    soluong = int(cthd.xpath("./q:SOLUONG/text()", namespaces=ns)[0])
                    dish_count[mamon] += soluong
                # Lấy tên món có tổng SOLUONG > 1
                mons = root.xpath("//q:MON", namespaces=ns)
                result = []
                for mon in mons:
                    mamon = mon.xpath("./q:MAMON/text()", namespaces=ns)[0]
                    tenmon = mon.xpath("./q:TENMON/text()", namespaces=ns)[0]
                    if dish_count[mamon] > 1:
                        result.append(tenmon)
                print(f"{label}: {result}")
                continue
            
            # Chạy XPath thông thường
            result = root.xpath(xpath, namespaces=ns)
            if isinstance(result, (list, tuple)) and len(result) > 0 and isinstance(result[0], etree._Element):
                # Nếu là elements, in text content
                texts = [elem.text for elem in result if elem.text]
                print(f"{label}: {texts}")
            else:
                print(f"{label}: {result}")
    except FileNotFoundError:
        print(f"Lỗi: Không tìm thấy file {filename}")
    except Exception as e:
        print(f"Lỗi khi chạy {label}: {e}")
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
    # Chạy cho sinhvien.xml (nếu có file và queries)
    if queries_sinhvien:  # Chỉ chạy nếu có queries
        run_xpath("sinhvien.xml", queries_sinhvien)
    # Chạy cho quanlybanan.xml
    run_xpath("quanlybanan.xml", queries_quanan, ns={'q': 'http://example.com/quanan'})
    input("Nhấn Enter để thoát...")
    