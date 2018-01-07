from elizabeth import Text, Personal


class Dildo:
    def answer():
        text = Text('ru')
        a = text.text(quantity=1)
        return a


class RandomMail:
    def mail():
        personal = Personal('ru')
        login = personal.email(gender='female')
        password = personal.password(length=15)
        b = 'login: ' + login + '\n' + 'pass: ' + password + '\n \n Enjoy, sweety...'
        return b
