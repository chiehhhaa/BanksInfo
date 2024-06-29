# 台灣銀行代碼查詢
透過Django與政府開放平台的CSV串接，並結合Alpine.js實現使用者查詢台灣各銀行分行詳細資訊的功能。

## 網站：
https://bank.diswork.cc/

## 功能：
1. 查詢銀行及分行名稱
2. 輸入關鍵字查詢
3. 分行資料顯示
4. 一鍵複製分行代碼
5. 一鍵複製網址
6. 一鍵重新整理

## 專案初始化
### 虛擬環境:
```
$ pip install poetry
$ poetry init -n
$ poetry shell
$ poetry install
```
```
$ make server
```
### CSV存入資料庫
```
$ python manage.py import_csv data/bankInfo.csv
```

## 使用技術：
- 前端：HTML, CSS, Alpine.js
- 後端：Python Django
- 資料庫：MySQL
- 版本控制：Git
- 部署：AWS EC2
