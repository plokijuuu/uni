import hashlib


class AuthenticException(Exception):
    pass


class PasswordTooShort(AuthenticException):
    pass


class UsernameAlreadyExists(AuthenticException):
    pass


class IncorrectUsername(AuthenticException):
    pass


class IncorrectPassword(AuthenticException):
    pass


class NotLoggedError(AuthenticException):
    pass


class PermissionError(Exception):
    pass


class NotPermittedError(AuthenticException):
    pass


class User:
    def __init__(self, username, password):
        self.username = username
        self.password = self._encrypt_password(username, password)
        self.is_logged = False

    def _encrypt_password(self, username, password):
        combo = (username + password).encode("utf-8")
        return hashlib.sha256(combo).hexdigest()

    def check_password(self, password):
        return self.password == self._encrypt_password(self.username, password)


class Authenticator:
    def __init__(self):
        self.users = {}

    def add_user(self, username, password):
        if username in self.users:
            raise UsernameAlreadyExists("Użytkownik już istnieje.")

        if len(password) <= 7:
            raise PasswordTooShort("Hasło musi mieć więcej niż 7 znaków.")

        self.users[username] = User(username, password)

    def login(self, username, password):
        if username not in self.users:
            raise IncorrectUsername("Niepoprawna nazwa użytkownika.")

        user = self.users[username]

        if not user.check_password(password):
            raise IncorrectPassword("Niepoprawne hasło.")

        user.is_logged = True
        return True

    def is_logged_in(self, username):
        return username in self.users and self.users[username].is_logged


class Authorizor:
    def __init__(self, authenticator):
        self.authenticator = authenticator
        self.permissions = {}

    def add_permission(self, permission):
        if permission in self.permissions:
            raise PermissionError("Uprawnienie już istnieje.")
        self.permissions[permission] = set()

    def permit_user(self, username, permission):
        if permission not in self.permissions:
            raise PermissionError("Brak takiego uprawnienia.")

        if username not in self.authenticator.users:
            raise IncorrectUsername("Nie ma takiego użytkownika.")

        self.permissions[permission].add(username)

    def check_permission(self, username, permission):
        if not self.authenticator.is_logged_in(username):
            raise NotLoggedError("Użytkownik nie jest zalogowany.")

        if permission not in self.permissions:
            raise PermissionError("Nie ma takiego uprawnienia.")

        if username not in self.permissions[permission]:
            raise NotPermittedError("Brak uprawnienia.")

        return True


auth = Authenticator()
authorizor = Authorizor(auth)


class Editor:
    def __init__(self):
        self.username = None
        self.options = {
            "a": self.login,
            "b": self.test,
            "c": self.change,
            "d": self.quit
        }

    def login(self):
        username = input("Podaj nazwę użytkownika: ")
        password = input("Podaj hasło: ")

        try:
            auth.login(username, password)
            self.username = username
            print("Zalogowano pomyślnie.")
        except (IncorrectUsername, IncorrectPassword) as e:
            print(f"Błąd logowania: {e}")

    def is_permitted(self, permission):
        try:
            return authorizor.check_permission(self.username, permission)
        except (NotLoggedError, PermissionError, NotPermittedError) as e:
            print(f"Brak dostępu: {e}")
            return False

    def test(self):
        if self.is_permitted("test"):
            print("Testowanie programu...")

    def change(self):
        if self.is_permitted("edit"):
            print("Edytowanie programu...")

    def quit(self):
        print("Koniec programu.")
        exit(0)

    def run(self):
        print("=== MENU EDITORA ===")
        print("a - zaloguj")
        print("b - testowanie programu")
        print("c - edycja programu")
        print("d - wyjście")

        while True:
            choice = input("Wybierz opcję: ").lower()
            action = self.options.get(choice)
            if action:
                action()
            else:
                print("Nieznana opcja.")


try:
    auth.add_user("admin", "superhaslo1")
    auth.add_user("tester", "testowanie123")
    auth.add_user("editor", "edytor_haslo")
except (PasswordTooShort, UsernameAlreadyExists) as e:
    print(e)

try:
    authorizor.add_permission("test")
    authorizor.add_permission("edit")
except PermissionError:
    pass

authorizor.permit_user("tester", "test")
authorizor.permit_user("admin", "test")
authorizor.permit_user("admin", "edit")
authorizor.permit_user("editor", "edit")

if __name__ == "__main__":
    editor = Editor()
    editor.run()
