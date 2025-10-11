from lxml import etree

tree = etree.parse("sv.xml")

# Ví dụ: lấy tất cả tên sinh viên
result = tree.xpath("//student/name/text()")
for r in result:
    print(r)
