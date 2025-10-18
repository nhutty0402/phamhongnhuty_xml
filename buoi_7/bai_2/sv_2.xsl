<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0"
  xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

  <!-- Xuất ra dạng HTML -->
  <xsl:output method="html" encoding="UTF-8" indent="yes"/>

  <xsl:template match="/school">
    <html>
      <head>
        <meta charset="UTF-8"/>
        <title>Danh sách sinh viên</title>
        <style>
          body {
            font-family: Arial, sans-serif;
            background-color: #f9fafb;
            padding: 20px;
          }
          h2 {
            text-align: center;
            color: #333;
          }
          table {
            border-collapse: collapse;
            width: 80%;
            margin: 0 auto;
            background-color: white;
            box-shadow: 0 2px 6px rgba(0,0,0,0.1);
            border-radius: 8px;
            overflow: hidden;
          }
          th, td {
            border: 1px solid #ddd;
            padding: 10px;
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
        <h2>DANH SÁCH SINH VIÊN</h2>
        <table>
          <tr>
            <th>Mã sinh viên</th>
            <th>Họ tên</th>
            <th>Ngày sinh</th>
            <!-- <th>Lớp</th> -->
          </tr>
          <xsl:for-each select="student">
            <tr>
              <td><xsl:value-of select="id"/></td>
              <td><xsl:value-of select="name"/></td>
              <td><xsl:value-of select="date"/></td>
              <!-- <td><xsl:value-of select="grade"/></td> -->
            </tr>
          </xsl:for-each>
        </table>
      </body>
    </html>
  </xsl:template>
</xsl:stylesheet>
