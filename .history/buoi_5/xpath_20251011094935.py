# 1. Lấy tất cả sinh viên
//student

# 2. Liệt kê tên tất cả sinh viên
//student/name/text()

# 3. Lấy tất cả id của sinh viên
//student/id/text()

# 4. Lấy ngày sinh của sinh viên có id = "SV01"
//student[id='SV01']/date/text()

# 5. Lấy các khóa học
//enrollment/course/text()

# 6. Lấy toàn bộ thông tin của sinh viên đầu tiên
//student[1]

# 7. Lấy mã sinh viên đăng ký khóa học "Vatly203"
//enrollment[course='Vatly203']/studentRef/text()

# 8. Lấy tên sinh viên học môn "Toan101"
//student[id=//enrollment[course='Toan101']/studentRef]/name/text()

# 9. Lấy tên sinh viên học môn "Vatly203"
//student[id=//enrollment[course='Vatly203']/studentRef]/name/text()

# 10. Lấy ngày sinh của sinh viên có id = "SV01"
//student[id='SV01']/date/text()

# 11. Lấy tên và ngày sinh của mọi sinh viên sinh năm 1997
//student[starts-with(date, '1997')]/(name|date)/text()

# 12. Lấy tên của các sinh viên có ngày sinh trước năm 1998
//student[number(substring(date,1,4)) < 1998]/name/text()

# 13. Đếm tổng số sinh viên
count(//student)

# 14. Lấy tất cả sinh viên chưa đăng ký môn nào (sau khi thêm dữ liệu 2 SV mới)
//student[not(id = //enrollment/studentRef)]

# 15. Lấy phần tử <date> anh em ngay sau <name> của SV01
//student[id='SV01']/name/following-sibling::date

# 16. Lấy phần tử <id> anh em ngay trước <name> của SV02
//student[id='SV02']/name/preceding-sibling::id

# 17. Lấy toàn bộ node <course> trong cùng một <enrollment> với studentRef='SV03'
//enrollment[studentRef='SV03']/course

# 18. Lấy sinh viên có họ là “Trần”
//student[starts-with(name, 'Trần')]

# 19. Lấy mã sinh của sinh viên SV01
//student[id='SV01']/date/text()
