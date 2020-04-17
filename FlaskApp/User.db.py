class db():
    def __init__(self, login, password):
        self.password = password
        self.login = login

    def append(self, login, password):
        self.login = login
        self.password = password
        conn = sqlite3.connect("One.db")
        cursor = conn.cursor()
        cursor.execute("""UPDATE employees
                    SET login1 = login, 
                    password1 = password""")
        conn.commit()
        conn.close()

    @property
    def __class__(self: _T) -> Type[_T]:
        return super().__class__()