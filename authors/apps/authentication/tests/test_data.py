"""
authentication test data
"""
valid_user = {
    "user": {
        "username": "Bagzie12",
        "email": "bagendadeogracious@gmail.com",
        "password": "Password123"
    }
}

valid_login = {
    "user": {
        "email": "bagendadeogracious@gmail.com",
        "password": "Password123"
    }
}

wrong_password = {
    "user": {
        "email": "bagendadeogracious@gmail.com",
        "password": "Password12"
    }
}

wrong_email = {
    "user": {
        "email": "bagenda@gmail.com",
        "password": "Password123"
    }
}

missing_password_data = {
    "user": {
        "email": "Password123"
    }
}
missing_email_data = {
    "user": {
        "password": "Password123"
    }
}
empty_username = {
    "user": {
        "username": "",
        "email": "bagendadeogracious@gmail.com",
        "password": "Password123"
    }
}
empty_email = {
    "user": {
        "username": "Bagzie",
        "email": "",
        "password": "Password123"
    }
}
empty_password = {
    "user": {
        "username": "Bagzie",
        "email": "bagendadeogracious@gmail.com",
        "password": ""
    }
}
invalid_user_email = {
    "user": {
        "username": "Bagzie",
        "email": "bagendadegmail.com",
        "password": "Password123"
    }
}

short_password = {
    "user": {
        "username": "Bagzie",
        "email": "bagendadeogracious@gmail.com",
        "password": "Pass"
    }
}

missing_username_key = {
    "user": {
        "email": "bagendadeogracious@gmail.com",
        "password": "Password123"
    }
}

invalid_username = {
    "user": {
        "username": "testus",
        "email": "testuser@gmail.com",
        "password": "testing123"
    }
}

invalid_password = {
    "user": {
        "username": "testuser",
        "email": "testuser@gmail.com",
        "password": "testingui"
    }
}
