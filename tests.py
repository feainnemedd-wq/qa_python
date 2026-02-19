import pytest
from main import BooksCollector

class TestBooksCollector:

    # 1. Проверка добавления книги с валидным названием (параметризация)
    @pytest.mark.parametrize('name', ['A', 'Книга длиной ровно в сорок символов (40)!'])
    def test_add_new_book_valid_name_added(self, name):
        collector = BooksCollector()
        collector.add_new_book(name)
        assert name in collector.get_books_genre()

    # 2. Название книги длиннее 40 символов не должно добавиться
    def test_add_new_book_name_longer_40_chars_not_added(self):
        collector = BooksCollector()
        long_name = 'Это очень длинное название книги, которое превышает сорок символов'
        collector.add_new_book(long_name)
        assert long_name not in collector.get_books_genre()

    # 3. У добавленной книги изначально нет жанра (пустая строка)
    def test_add_new_book_has_no_genre_by_default(self):
        collector = BooksCollector()
        collector.add_new_book('Дракула')
        assert collector.get_book_genre('Дракула') == ''

    # 4. Установка жанра книге из списка допустимых
    def test_set_book_genre_successfully(self):
        collector = BooksCollector()
        collector.add_new_book('Дюна')
        collector.set_book_genre('Дюна', 'Фантастика')
        assert collector.get_book_genre('Дюна') == 'Фантастика'

    # 5. Вывод списка книг с определенным жанром
    def test_get_books_with_specific_genre_filtered(self):
        collector = BooksCollector()
        collector.add_new_book('Оно')
        collector.set_book_genre('Оно', 'Ужасы')
        assert 'Оно' in collector.get_books_with_specific_genre('Ужасы')

    # 6. Получение всего словаря книг
    def test_get_books_genre_returns_dict(self):
        collector = BooksCollector()
        collector.add_new_book('Колобок')
        assert isinstance(collector.get_books_genre(), dict)

    # 7. Книги с возрастным рейтингом отсутствуют в списке для детей
    def test_get_books_for_children_excludes_adult_genres(self):
        collector = BooksCollector()
        collector.add_new_book('Шрек')
        collector.set_book_genre('Шрек', 'Мультфильмы')
        collector.add_new_book('Сияние')
        collector.set_book_genre('Сияние', 'Ужасы')
        children_books = collector.get_books_for_children()
        assert 'Шрек' in children_books and 'Сияние' not in children_books

    # 8. Добавление книги в избранное
    def test_add_book_in_favorites_added(self):
        collector = BooksCollector()
        collector.add_new_book('1984')
        collector.add_book_in_favorites('1984')
        assert '1984' in collector.get_list_of_favorites_books()

    # 9. Удаление книги из избранного
    def test_delete_book_from_favorites_removed(self):
        collector = BooksCollector()
        collector.add_new_book('Ведьмак')
        collector.add_book_in_favorites('Ведьмак')
        collector.delete_book_from_favorites('Ведьмак')
        assert 'Ведьмак' not in collector.get_list_of_favorites_books()

    # 10. Получение списка избранных книг
    def test_get_list_of_favorites_books_initially_empty(self):
        collector = BooksCollector()
        assert collector.get_list_of_favorites_books() == []
