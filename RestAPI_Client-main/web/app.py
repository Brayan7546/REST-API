import requests
from flask import Flask, render_template, request
import random
from flask_bootstrap import Bootstrap


app = Flask(__name__)
bootstrap = Bootstrap(app)
model = []


@app.route("/")
def index():
    return render_template('index.html')


@app.route('/new_pet', methods=['GET'])
def person():
    return render_template('new_pet.html')


@app.route('/pet_detail', methods=['POST'])
def pet_detail():
    api_url = "https://petstore.swagger.io/v2/pet"
    id = request.form['id']
    name = request.form['name']
    new_data = {
                    "id": id,
                    "category": {
                        "id": 0,
                        "name": "string"
                    },
                    "name": name,
                    "photoUrls": [
                        "string"
                    ],
                    "tags": [
                        {
                            "id": 0,
                            "name": "string"
                        }
                    ],
                    "status": "available"
                }
    response = requests.post(api_url, json=new_data)
    return render_template('pet_detail.html', value=(id, name))


@app.route('/pet', methods=['GET'])
def pets(status: str = "pending"):
    url2 = "https://petstore.swagger.io/v2/pet/findByStatus?status={0}".format(status)
    response = requests.get(url2)
    data_pets = [(i['id'], i['name'], i['status']) for i in response.json()]
    return render_template('pets.html', value=data_pets)


@app.route('/pet_update/<id_pet>', methods=['GET'])
def pet_update(id_pet):
    return render_template('pet_update.html', value=id_pet)


@app.route('/pet_update_detail', methods=['POST'])
def pet_update_detail():
    api_url_update = "https://petstore.swagger.io/v2/pet"
    id = request.form['id']
    name = request.form['name']
    status = request.form['status']
    update_data = {
                        "id": id,
                        "category": {
                            "id": 0,
                            "name": "string"
                        },
                        "name": name,
                        "photoUrls": [
                            "string"
                        ],
                        "tags": [
                            {
                                "id": 0,
                                "name": "string"
                            }
                        ],
                        "status": status
                    }
    response = requests.put(api_url_update, json=update_data)
    return render_template('pet_detail.html', value=(id, name, status))


@app.route('/pet_delete/<id_pet>', methods=['GET'])
def pet_delete(id_pet):
    api_url = "https://petstore.swagger.io/v2/pet/{0}".format(id_pet)
    response = requests.delete(api_url)
    return render_template('pet_detail.html', value="Delete successfully")


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500


@app.route('/order', methods=['GET'])
def order():
    return render_template('order.html')


@app.route('/place_order/<id_pet>', methods=['GET'])
def order_place(id_pet):
    api_url_order_place = "https://petstore.swagger.io/v2/store/order"
    Ramnumb = random.randint(1, 10)
    orders = {
        "id": Ramnumb,
        "petId": id_pet,
        "quantity": 1,
        "shipDate": "2022-04-07T03:49:22.461Z",
        "status": "placed",
        "complete": "true"
    }
    response = requests.post(api_url_order_place, json=orders)
    return render_template('order_place.html', value=orders)


@app.route('/order_find', methods=['POST'])
def order_find():
    order_id = request.form['id']
    api_url_order_find = "https://petstore.swagger.io/v2/store/order/{0}".format(order_id)
    response = requests.get(api_url_order_find)
    order_found = response.json()
    return render_template('order_find.html', value=order_found)


@app.route('/order_delete', methods=["POST"])
def order_delete():
    order_id = request.form['id']
    api_url_order_delete = "https://petstore.swagger.io/v2/store/order/{0}".format(order_id)
    response = requests.delete(api_url_order_delete)
    return render_template('order_delete.html')


@app.route('/inventory', methods=["GET"])
def inventory():
    api_url_inventory = "https://petstore.swagger.io/v2/store/inventory"
    response = requests.get(api_url_inventory)
    inventory_info = response.json()
    return render_template('inventory.html', value=inventory_info)


@app.route('/user_list_array', methods=['GET'])
def user_list_array():
    api_user_list_array = 'https://petstore.swagger.io/v2/user/createWithArray'
    response = requests.post(api_user_list_array)

    return render_template('user_list.html', value=response)


@app.route('/create_list', methods=['GET'])
def create_list():
    api_url_create_list = 'https://petstore.swagger.io/v2/user/createWithList'
    response = requests.post(api_url_create_list )
    return render_template('create_list.html', value=' ')


@app.route('/get_user', methods=['GET', 'POST'])
def user_get():
    username = request.form['username']
    api_url_user_get = "https://petstore.swagger.io/v2/user/{0}".format(username)
    response = requests.get(api_url_user_get)
    body = response.json()
    return render_template('user_get.html', value=body)


@app.route('/update_user', methods=['POST'])
def user_update():
    username = request.form['username']
    email = request.form['email']
    password = request.form['password']
    print(username, email, password)
    random_num = random.randint(1, 1000)
    api_url_user_update = "https://petstore.swagger.io/v2/user/{0}".format(username)
    model_user = {
        "id": 0,
        "username": "string",
        "firstName": "string",
        "lastName": "string",
        "email": "string",
        "password": "string",
        "phone": "string",
        "userStatus": 0
        }

    response = requests.put(api_url_user_update, json=model_user)
    return render_template('user_update.html', value='done')


@app.route('/update', methods=['GET'])
def update():
    return render_template('update.html')


@app.route('/user_create', methods=['POST'])
def user_create():
    api_url_user_create = 'https://petstore.swagger.io/v2/user'
    email = request.form['email']
    username = request.form['username']
    password = request.form['password']
    id = random.randint(1, 1000)
    model_user = {
        "id": 0,
        "username": "string",
        "firstName": "string",
        "lastName": "string",
        "email": "string",
        "password": "string",
        "phone": "string",
        "userStatus": 0
    }
    response = requests.post(api_url_user_create, json=model_user)
    return render_template('user_create.html', value=model_user)


@app.route('/user_delete', methods=['POST'])
def user_delete():
    username = request.form['username']
    print(username)
    api_url_user_delete = "https://petstore.swagger.io/v2/user/{0}".format(username)
    response = requests.delete(api_url_user_delete)
    return render_template('user_delete.html', value='User deleted')


@app.route('/user_login', methods=['GET', 'POST'])
def user_login():
    username = request.form['username']
    password = request.form['password']
    api_url_user_login = 'https://petstore.swagger.io/v2/user/login?username={0}&password={1}'.format(username, password)
    response = requests.get(api_url_user_login)
    user_info = response.json()
    return render_template('user_login.html', value = user_info)


@app.route('/user_logout', methods=['GET'])
def user_logout():
    api_url_user_logout = 'https://petstore.swagger.io/v2/user/logout'
    response = requests.get(api_url_user_logout)
    return render_template('user_logout.html', value='closed session')


@app.route('/user', methods=['GET'])
def user():
    return render_template('user.html')


if __name__ == '__main__':
    app.run()