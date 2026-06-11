Coffee Shop API 

#ru
Это прототип  backend системы для сети кофеен с использованием Django. проект структурирован и полность. готов к маштабированию 

#eng
This is a prototype backend system for a coffee shop chain using Django. The project is structured and fully scalable.

#Technology
- Python 3.11
- Django 5.12x
- Django REST Framework
- PostgresSQL
- Swagger

#Installing
 - cd project
 - py -3.11 -m venv venv
 - venv\Scripts\activate
 - pip install -r req.txt

#Применение Миграций | Using Migrations
- python manage.py migrate
- python manage.py createsuperuser

#Запуск | Launch
- python manage.py runserver

API доступен по адресу: `http://127.0.0.1:8000/ 

Swagger: `http://127.0.0.1:8000/swagger/

#API Endpoints

Категория | Category  

- GET: 'categories/' - Cписок всех товаров | List of all categories  
- GET: 'category/id/' - Вывод одной категории по ID | Displaying a single category by ID  
- PATCH: 'category/change/id/' Частичное изменение категории по ID | Partial change of category by ID  
- POST: 'category/create/' Создание новой категории | Creating new category  
- DELETE: 'category/delete/id/' Удаление категории по ID | Deleting category by ID  

Продукты | Products

- GET: 'products/' - Список всех продуктов | List of all products  
- GET: 'product/id/' - Вывод одного продукта по ID | Displaying a single product by ID  
- POST: 'product/create/' - Создание нового продукта | Creating a new product  
- PATCH: 'product/change/id/' - Частичное изменение продукта по ID | Partial change of product by ID  
- DELETE: 'product/delete/id/' - Удаление продукта по ID | Deleting product by ID  

Заказ | Order

- GET: 'orders/' - Список всех заказов | List of all products
- GET: 'order/id/' - Вывод одного заказа по ID | Displaying a single order by ID
- POST: 'order/create/' - Создание нового заказа | Creating a new order
- PATCH: 'order/change/id/' - Частичное изменение заказа | Partial change of order by ID
- DELETE: 'order/delete/id/' - Удаление заказа по ID | Deleting order by ID

Корзина | Cart

- GET: 'carts/' - Список всех корзин | List of all carts
- GET: 'carts/id/' - Вывод одной корзины по ID | Displaying a single cart by ID
- POST: 'cart/create/' - Создание новой корзины | Creating a new cart
- PATCH: 'cart/change/id/' - Частичное изменение корзины по ID | Partial change of cart by ID
- DELETE: 'cart/delete/id/' - Удаление корзины по ID | Deleting cart by ID

Товар в корзине | Item in cart

- GET: 'cartitems/' - Список всех товаров в корзине | List of all items in cart
- GET: 'cartitem/id/' - Вывод одной товаров в корзине | Displaying a single item in cart
- POST: 'cartitem/create/' - Создание нового товара в корзине | Creating a new item in cart
- PATCH: 'cartitem/change/id/' - Частичное изменение товара в корзине по ID | Partial change of item in cart by ID
- DELETE: 'cartitem/delete/id/' - Удаление товара в корзине по ID | Deleting item in cart by ID


Пользователь | User

- POST: 'register/' - Регистрация нового пользователя | Registration new user
- POST: 'login/' - Вход в существующего пользователя | Log in
- GET: 'verify/' - Верификация нового пользователя | Verification a new user
- POST: 'token/' - Получение токена | Getting a token
- POST: 'token/refresh/' - Обновление токена | Updating token
- GET: 'me/' - Получить информацию о текущем пользователе | Get information about the current user
- GET: 'getAll' - Вывод все пользователь | List of all users
- GET: 'user/id/' - Вывод одного пользователя | Displaying a single user
- PATCH: 'user/change/id/' - Частичное изменение пользователя по ID | Partial change of user by ID
- DELETE: 'user/delete/id/' - Удаление пользователя по ID | Deleting user by ID


Примечания | Notes

#ru  
Для добавления продуктов в корзины и заказы, я создал нову. модель под названием CartItem туда добавляются продукты, номер корзины, товары, и заказы. После этого в http://127.0.0.1:8000/app/carts/ подсчитывается автоматически заказы в корзине и выводится.

#eng  
To add products to carts and orders, I created a new model called CartItem . It contains products, a cart number and orders. After that, http://127.0.0.1:8000/app/carts/ automatically calculates the orders in the cart and displays them.

#ru  
Также в http://127.0.0.1:8000/app/cart/create/ никакие поля добавлять не надо, система сама создает корзины при нажатии кнопки POST

#eng  
Also, in http://127.0.0.1:8000/app/cart/create/ you don’t need to add any fields, the system itself creates carts when you press the POST button