import json
import os
import hashlib

class UserManager:
    def __init__(self, db_path='users.json'):
        self.db_path = db_path
        self.users = self._load_users()
        self._current_user = None  #当前登录的用户名

    def _load_users(self):
        if not os.path.exists(self.db_path):
            return {}
        with open(self.db_path, 'r', encoding='utf-8') as f:
            return json.load(f)

    def _save_users(self):
        with open(self.db_path, 'w', encoding='utf-8') as f:
            json.dump(self.users, f, indent=2)

    def _hash_password(self, password):
        return hashlib.sha256(password.encode('utf-8')).hexdigest()

    def try_register(self, username, password):
        if username in self.users:
            return False, "用户名已存在"
        if not username or not password:
            return False, "用户名和密码不能为空"
        self.users[username] = self._hash_password(password)
        self._save_users()
        return True, "注册成功"

    def try_login(self, username, password):
        if username not in self.users:
            return False, "用户名不存在"
        if self.users[username] != self._hash_password(password):
            return False, "密码错误"
        self._current_user = username
        return True, "登录成功"

    def is_logged_in(self):
        return self._current_user is not None

    def current_user(self):
        return self._current_user

    def logout(self):
        self._current_user = None
