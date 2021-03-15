# Database-project

## Description
資料庫管理期末專案，由四個人共同完成，目標是運用所學的有關資料庫的知識，建置一個簡易的資料庫系統。

本組所選擇的主題是產銷履歷查詢系統，我們希望做一個關於農產品產銷履歷的資料庫專案，讓消費者可以直接透過我們提供的搜尋介面，得到其想了解的相關資訊，希望能夠使消費者吃得安心，餐廳的食材也能被溯源，相關加工品的原料若有使用到有產銷履歷的農產品也能夠被查詢。

- 功能：依據使用者對不同資訊的需求，包含產品名稱、加工產品名稱、生產者、餐廳業者、銷售通路、追溯號碼，我們提供了搜尋、新增、修改與刪除的功能。以搜尋為例，先選取分類後，再在後方的空白格輸入想了解的 query，我們就會回傳該 query 的相關資訊。

- 資料庫：在我們的資料庫中，主要的 entity 有履歷商品、 生產者、餐廳、銷售通路、加工廠商、加工產品(以上銷售通路、生產者、餐廳、加工廠商、加工產品僅包含有販售、生產或使用產銷履歷商品者)。

- ER diagram：
![image]https://github.com/JJJamieee/Database-project/blob/main/image1.jpg


## Feature Demo
1. 查詢
![image]https://github.com/JJJamieee/Database-project/blob/main/database_search.gif

2. 編輯
![image]https://github.com/JJJamieee/Database-project/blob/main/database_edit.gif

3. 刪除
![image]https://github.com/JJJamieee/Database-project/blob/main/database_delete.gif

4. 新增
![image]https://github.com/JJJamieee/Database-project/blob/main/database_create.gif

## Program Detail
本系統使用Django及SQLite建立。

- 前端除了將後端傳了的資料以表格顯示之外，還要在每列產生編輯鈕和刪除鈕，這兩個按鈕都分別是form的submit鈕，form裡包含了兩個隱藏的input，value分別設定為目前的項目種類(e.g.生產者or加工產品等)及該項的ID。
- 所有的查詢都由同一個函數來處理，先判斷dropdown list選擇的是哪一項，再對資料庫做query。
- 使用者點了編輯鈕後，會被導到另一個編輯頁面，此頁面會根據編輯鈕所傳來的類別和該項資料的ID，把原本的資料撈出來並顯示為表格的預設數值，使用者點了送出修改後再將資料更新。
- 使用者點了刪除鈕後，後端會根據刪除鈕所傳來的類別和該項資料的ID，將該項資料刪除，因為資料庫中所有關於Foreign Key的設定都是`on_delete=models.CASCADE`，所有與該項資料有關的資料都會一併被刪除。
- 使用者將新增頁面的表單填完後，點擊新增按鈕，前端便會將表單的值送到後端，後端再依此於資料庫中新增資料。

## Reference
- Django: https://www.djangoproject.com/
- Bootstrap: https://getbootstrap.com/
- Django介紹(MDN): https://developer.mozilla.org/zh-TW/docs/Learn/Server-side/Django/Introduction
- Django Girls 學習指南: https://djangogirlstaipei.gitbooks.io/django-girls-taipei-tutorial/content/
