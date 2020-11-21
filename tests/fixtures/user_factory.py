from schemas.user import UserCreate, User, UserUpdate

user_one_data = {
    'id': '863050cc-3d13-4eac-b960-09f4a3265caa',
    'name': 'Vitor Martins',
    'email': 'contato@vitormartins.dev',
    'password': 'xalala',
    'cpf_cnpj': '11122233344',
    'address': 'Rua dos Bobos, 0',
    'active': False,
    'picture': None,
    'reset_password_token': None,
    'reset_password_expires_in': None,
    'created_at': '2020-11-20T19:58:28.827040',
    'updated_at': '2020-11-20T19:55:30.534635'
}


def valid_user_one_data():
    return user_one_data.copy()


def valid_user_one_data_without_password():
    data = valid_user_one_data()
    data.pop('password')
    return data


def valid_user_one_create():
    return UserCreate(
        name=user_one_data['name'],
        email=user_one_data['email'],
        cpf_cnpj=user_one_data['cpf_cnpj'],
        address=user_one_data['address'],
        password=user_one_data['password'],
    )


def valid_user_one_update():
    return UserUpdate(
        name='Vitor Matheus',
        address='Rua Xalala, 5'
    )


def valid_user_one_updated_without_password():
    data = valid_user_one_data()
    data.pop('password')
    update = valid_user_one_update()
    data['name'] = update.name
    data['address'] = update.address
    return data


def valid_user_one():
    return User(**user_one_data)


def valid_user_one_updated():
    return User(**valid_user_one_updated_without_password())
