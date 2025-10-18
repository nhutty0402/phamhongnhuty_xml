<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0"
  xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

  <xsl:output method="html" encoding="UTF-8" indent="yes"/>

  <xsl:template match="/QUANLY">
    <html>
      <head>
        <meta charset="UTF-8"/>
        <title>Quản lý bàn ăn - Kết quả truy vấn</title>
        <style>
          body {
            font-family: Arial, sans-serif;
            background-color: #f9fafb;
            padding: 20px;
          }
          h2 {
            background-color: #007bff;
            color: white;
            padding: 10px;
            text-align: center;
            border-radius: 8px;
          }
          table {
            border-collapse: collapse;
            width: 90%;
            margin: 20px auto;
            background-color: white;
            box-shadow: 0 2px 6px rgba(0,0,0,0.1);
            border-radius: 8px;
            overflow: hidden;
          }
          th, td {
            border: 1px solid #ddd;
            padding: 8px;
            text-align: center;
          }
          th {
            background-color: #007bff;
            color: white;
          }
          tr:nth-child(even) {
            background-color: #f2f2f2;
          }
          tr:hover {
            background-color: #e6f7ff;
          }
        </style>
      </head>

      <body>
        <h1 style="text-align:center; color:#333;">KẾT QUẢ TRUY VẤN DỮ LIỆU</h1>

        <!-- 1. Danh sách tất cả các bàn -->
        <h2>1. Danh sách tất cả các bàn</h2>
        <table>
          <tr><th>STT</th><th>Số bàn</th><th>Tên bàn</th></tr>
          <xsl:for-each select="BANS/BAN">
            <tr>
              <td><xsl:value-of select="position()"/></td>
              <td><xsl:value-of select="SOBAN"/></td>
              <td><xsl:value-of select="TENBAN"/></td>
            </tr>
          </xsl:for-each>
        </table>

        <!-- 2. Danh sách nhân viên -->
        <h2>2. Danh sách các nhân viên</h2>
        <table>
          <tr><th>STT</th><th>Mã NV</th><th>Tên</th><th>Giới tính</th><th>SDT</th><th>Địa chỉ</th></tr>
          <xsl:for-each select="NHANVIENS/NHANVIEN">
            <tr>
              <td><xsl:value-of select="position()"/></td>
              <td><xsl:value-of select="MANV"/></td>
              <td><xsl:value-of select="TENV"/></td>
              <td><xsl:value-of select="GIOITINH"/></td>
              <td><xsl:value-of select="SDT"/></td>
              <td><xsl:value-of select="DIACHI"/></td>
            </tr>
          </xsl:for-each>
        </table>

        <!-- 3. Danh sách món ăn -->
        <h2>3. Danh sách các món ăn</h2>
        <table>
          <tr><th>STT</th><th>Mã món</th><th>Tên món</th><th>Giá</th></tr>
          <xsl:for-each select="MONS/MON">
            <tr>
              <td><xsl:value-of select="position()"/></td>
              <td><xsl:value-of select="MAMON"/></td>
              <td><xsl:value-of select="TENMON"/></td>
              <td><xsl:value-of select="GIA"/></td>
            </tr>
          </xsl:for-each>
        </table>

        <!-- 4. Thông tin nhân viên NV02 -->
        <h2>4. Thông tin của nhân viên NV02</h2>
        <table>
          <tr><th>Mã NV</th><th>Tên</th><th>Giới tính</th><th>SDT</th><th>Địa chỉ</th></tr>
          <xsl:for-each select="NHANVIENS/NHANVIEN[MANV='NV02']">
            <tr>
              <td><xsl:value-of select="MANV"/></td>
              <td><xsl:value-of select="TENV"/></td>
              <td><xsl:value-of select="GIOITINH"/></td>
              <td><xsl:value-of select="SDT"/></td>
              <td><xsl:value-of select="DIACHI"/></td>
            </tr>
          </xsl:for-each>
        </table>

        <!-- 5. Các món ăn có giá > 50000 -->
        <h2>5. Danh sách món ăn có giá &gt; 50,000</h2>
        <table>
          <tr><th>STT</th><th>Mã món</th><th>Tên món</th><th>Giá</th></tr>
          <xsl:for-each select="MONS/MON[GIA &gt; 50000]">
            <tr>
              <td><xsl:value-of select="position()"/></td>
              <td><xsl:value-of select="MAMON"/></td>
              <td><xsl:value-of select="TENMON"/></td>
              <td><xsl:value-of select="GIA"/></td>
            </tr>
          </xsl:for-each>
        </table>

        <!-- 6. Thông tin hóa đơn HD03 -->
        <h2>6. Thông tin hóa đơn HD03</h2>
        <table>
          <tr><th>Số HĐ</th><th>Tên nhân viên</th><th>Số bàn</th><th>Ngày lập</th><th>Tổng tiền</th></tr>
          <xsl:for-each select="HOADONS/HOADON[SOHD='HD03']">
            <tr>
              <td><xsl:value-of select="SOHD"/></td>
              <td><xsl:value-of select="/QUANLY/NHANVIENS/NHANVIEN[MANV=current()/MANV]/TENV"/></td>
              <td><xsl:value-of select="SOBAN"/></td>
              <td><xsl:value-of select="NGAYLAP"/></td>
              <td><xsl:value-of select="TONGTIEN"/></td>
            </tr>
          </xsl:for-each>
        </table>

        <!-- 7. Tên món ăn trong hóa đơn HD02 -->
        <h2>7. Tên các món ăn trong hóa đơn HD02</h2>
        <table>
          <tr><th>STT</th><th>Tên món</th></tr>
          <xsl:for-each select="HOADONS/HOADON[SOHD='HD02']/CTHDS/CTHD">
            <tr>
              <td><xsl:value-of select="position()"/></td>
              <td><xsl:value-of select="/QUANLY/MONS/MON[MAMON=current()/MAMON]/TENMON"/></td>
            </tr>
          </xsl:for-each>
        </table>

        <!-- 8. Tên nhân viên lập hóa đơn HD02 -->
        <h2>8. Tên nhân viên lập hóa đơn HD02</h2>
        <table>
          <tr><th>Tên nhân viên</th></tr>
          <tr>
            <td>
              <xsl:value-of select="/QUANLY/NHANVIENS/NHANVIEN[MANV=/QUANLY/HOADONS/HOADON[SOHD='HD02']/MANV]/TENV"/>
            </td>
          </tr>
        </table>

        <!-- 9. Đếm số bàn -->
        <h2>9. Số lượng bàn</h2>
        <table><tr><th>Tổng số bàn</th></tr>
          <tr><td><xsl:value-of select="count(BANS/BAN)"/></td></tr>
        </table>

        <!-- 10. Đếm số hóa đơn lập bởi NV01 -->
        <h2>10. Số hóa đơn lập bởi NV01</h2>
        <table><tr><th>Số lượng hóa đơn</th></tr>
          <tr><td><xsl:value-of select="count(HOADONS/HOADON[MANV='NV01'])"/></td></tr>
        </table>

        <!-- 11. Danh sách món từng bán cho bàn số 2 -->
        <h2>11. Danh sách các món từng bán cho bàn số 2</h2>
        <table>
          <tr><th>STT</th><th>Tên món</th></tr>
          <xsl:for-each select="HOADONS/HOADON[SOBAN='2']/CTHDS/CTHD">
            <tr>
              <td><xsl:value-of select="position()"/></td>
              <td><xsl:value-of select="/QUANLY/MONS/MON[MAMON=current()/MAMON]/TENMON"/></td>
            </tr>
          </xsl:for-each>
        </table>

        <!-- 12. Nhân viên từng lập hóa đơn cho bàn số 3 -->
        <h2>12. Danh sách nhân viên từng lập hóa đơn cho bàn số 3</h2>
        <table>
          <tr><th>STT</th><th>Tên nhân viên</th></tr>
          <xsl:for-each select="HOADONS/HOADON[SOBAN='3']">
            <tr>
              <td><xsl:value-of select="position()"/></td>
              <td><xsl:value-of select="/QUANLY/NHANVIENS/NHANVIEN[MANV=current()/MANV]/TENV"/></td>
            </tr>
          </xsl:for-each>
        </table>

        <!-- 13. Các món được gọi nhiều hơn 1 lần -->
        <h2>13. Các món ăn được gọi nhiều hơn 1 lần</h2>
        <table>
          <tr><th>STT</th><th>Tên món</th></tr>
          <xsl:for-each select="MONS/MON">
            <xsl:variable name="ma" select="MAMON"/>
            <xsl:if test="count(/QUANLY/HOADONS/HOADON/CTHDS/CTHD[MAMON=$ma]) &gt; 1">
              <tr>
                <td><xsl:value-of select="position()"/></td>
                <td><xsl:value-of select="TENMON"/></td>
              </tr>
            </xsl:if>
          </xsl:for-each>
        </table>

      </body>
    </html>
  </xsl:template>
</xsl:stylesheet>
