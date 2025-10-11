from lxml import etree

# Đọc file XML
tree = etree.parse("sv.xml")

# Đọc file chứa biểu thức XPath
with open("sinhvien_xpath.txt", "r", encoding="utf-8") as f:
    lines = [line.strip() for line in f if line.strip() and not line.startswith("#")]

# Chạy từng biểu thức
for expr in lines:
    try:
        result = tree.xpath(expr)
        print(f"\n👉 Biểu thức: {expr}")
        print("Kết quả:")
        for r in result:
            print("-", r if isinstance(r, str) else etree.tostring(r, pretty_print=True).decode())
    except Exception as e:
        print(f"Lỗi khi chạy {expr}: {e}")
