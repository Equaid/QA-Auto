from modules.ui.page_objects.sign_in_page import SignInPage
import pytest


@pytest.mark.ui
def test_check_incorrect_username_page_object():
    # створення об'єкту сторінки
    sign_in_page = SignInPage()

    # Відкриваємо сторінку https://github.com.login
    sign_in_page.go_to()

    # виконуємо спробуй увійти в систему GitHub
    sign_in_page.try_login("page_object@gmail.com" , "wrong paswond")

    #перевіряємо, що назва сторіки така яку ми очікуємо
    assert sign_in_page.check_tittle("Sign in to GitHub · GitHub")

    #закриваємо браузер
    sign_in_page.close()

