<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0"
  xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

<xsl:output method="html" indent="yes" encoding="UTF-8"/>

<xsl:template match="/school">
<html>
<head>
<meta charset="UTF-8"/>
<title>Danh sách sinh viên</title>
<style>
  body {
    font-family: 'Segoe UI', Arial, sans-serif;
    background: linear-gradient(to bottom right, #e3f2fd, #ffffff);
    padding: 20px;
  }
  h2 {
    background-color: #1976d2;
    color: white;
    padding: 10px 15px;
    border-radius: 6px;
    font-size: 18px;
  }
  table {
    width: 100%;
    border-collapse: collapse;
    margin: 15px 0 35px 0;
    box-shadow: 0 0 8px rgba(0,0,0,0.1);
    border-radius: 8px;
    overflow: hidden;
  }
  th {
    background-color: #64b5f6;
    color: #fff;
    padding: 10px;
    text-align: left;
  }
  td {
    padding: 8px 10px;
    border-bottom: 1px solid #ddd;
  }
  tr:hover {
    background-color: #e3f2fd;
  }
</style>
</head>
<body>

<!-- 1️⃣ Liệt kê tất cả sinh viên -->
<h2>1️⃣ Thông tin tất cả sinh viên (Mã và Họ tên)</h2>
<table>
<tr><th>STT</th><th>Mã SV</th><th>Họ và tên</th></tr>
<xsl:for-each select="student">
<tr>
  <td><xsl:value-of select="position()"/></td>
  <td><xsl:value-of select="id"/></td>
  <td><xsl:value-of select="name"/></td>
</tr>
</xsl:for-each>
</table>

<!-- 2️⃣ Danh sách sinh viên theo điểm -->
<h2>2️⃣ Danh sách sinh viên (Mã, Họ tên, Điểm) – Sắp xếp giảm dần theo điểm</h2>
<table>
<tr><th>STT</th><th>Mã</th><th>Họ tên</th><th>Điểm</th></tr>
<xsl:for-each select="student">
  <xsl:sort select="grade" data-type="number" order="descending"/>
  <tr>
    <td><xsl:value-of select="position()"/></td>
    <td><xsl:value-of select="id"/></td>
    <td><xsl:value-of select="name"/></td>
    <td><xsl:value-of select="grade"/></td>
  </tr>
</xsl:for-each>
</table>

<!-- 3️⃣ Sinh viên sinh tháng gần nhau -->
<h2>3️⃣ Danh sách sinh viên sinh tháng gần nhau</h2>
<table>
<tr><th>STT</th><th>Họ tên</th><th>Ngày sinh</th><th>Tháng sinh</th></tr>
<xsl:for-each select="student">
  <xsl:sort select="substring(date,6,2)" data-type="number" order="ascending"/>
  <tr>
    <td><xsl:value-of select="position()"/></td>
    <td><xsl:value-of select="name"/></td>
    <td><xsl:value-of select="date"/></td>
    <td><xsl:value-of select="substring(date,6,2)"/></td>
  </tr>
</xsl:for-each>
</table>

<!-- 4️⃣ Các khóa học có sinh viên học -->
<h2>4️⃣ Các khóa học có sinh viên đăng ký (sắp xếp theo tên khóa)</h2>
<table>
<tr><th>Mã khóa học</th><th>Tên khóa học</th></tr>
<xsl:for-each select="course">
  <xsl:sort select="name" order="ascending"/>
  <xsl:variable name="cid" select="id"/>
  <xsl:if test="../enrollment/courseRef = $cid">
    <tr>
      <td><xsl:value-of select="id"/></td>
      <td><xsl:value-of select="name"/></td>
    </tr>
  </xsl:if>
</xsl:for-each>
</table>

<!-- 5️⃣ Sinh viên học Hóa học 201 -->
<h2>5️⃣ Danh sách sinh viên đăng ký khóa học "Hóa học 201"</h2>
<table>
<tr><th>Mã SV</th><th>Họ tên</th></tr>
<xsl:for-each select="enrollment[courseRef='c3']">
  <xsl:variable name="sid" select="studentRef"/>
  <xsl:for-each select="../student[id=$sid]">
    <tr>
      <td><xsl:value-of select="id"/></td>
      <td><xsl:value-of select="name"/></td>
    </tr>
  </xsl:for-each>
</xsl:for-each>
</table>

<!-- 6️⃣ Sinh viên sinh năm 1997 -->
<h2>6️⃣ Danh sách sinh viên sinh năm 1997</h2>
<table>
<tr><th>STT</th><th>Mã SV</th><th>Họ tên</th><th>Ngày sinh</th></tr>
<xsl:for-each select="student[starts-with(date,'1997')]">
<tr>
  <td><xsl:value-of select="position()"/></td>
  <td><xsl:value-of select="id"/></td>
  <td><xsl:value-of select="name"/></td>
  <td><xsl:value-of select="date"/></td>
</tr>
</xsl:for-each>
</table>

<!-- 7️⃣ Sinh viên họ “Trần” -->
<h2>7️⃣ Danh sách sinh viên họ “Trần”</h2>
<table>
<tr><th>STT</th><th>Mã SV</th><th>Họ tên</th></tr>
<xsl:for-each select="student[starts-with(name,'Trần')]">
<tr>
  <td><xsl:value-of select="position()"/></td>
  <td><xsl:value-of select="id"/></td>
  <td><xsl:value-of select="name"/></td>
</tr>
</xsl:for-each>
</table>

</body>
</html>
</xsl:template>
</xsl:stylesheet>
