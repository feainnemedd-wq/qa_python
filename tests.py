import pytest
from main import BooksCollector

class TestBooksCollector:

    # 1. Добавление книги (1 и 40 символов)
    @pytest.mark.parametrize('name', ['A', 'Книга длиной ровно сорок символов (40)!!'])
    def test_add_new_book_valid_name_added(self, name):
        collector = BooksCollector()
        collector.add_new_book(name)
        assert name in collector.get_books_genre()

    # 2. Название > 40 символов
    def test_add_new_book_name_longer_40_chars_not_added(self):
        collector = BooksCollector()
        long_name = 'Это очень длинное название книги, которое точно больше 40 символов'
        collector.add_new_book(long_name)
        assert long_name not in collector.get_books_genre()

    # 3. Установка жанра
    def test_set_book_genre_successfully(self):
        collector = BooksCollector()
        collector.add_new_book('Дюна')
        collector.set_book_genre('Дюна', 'Фантастика')
        assert collector.get_book_genre('Дюна') == 'Фантастика'

    # 4. Жанр для детей (исключаем Ужасы и Детективы)
    def test_get_books_for_children_excludes_adult_genres(self):
        collector = BooksCollector()
        collector.add_new_book('Шрек')
        collector.set_book_genre('Шрек', 'Мультфильмы')
        collector.add_new_book('Оно')
        collector.set_book_genre('Оно', 'Ужасы')
        children_books = collector.get_books_for_children()
        assert 'Шрек' in children_books and 'Оно' not in children_books

    # 5. Добавление в избранное
    def test_add_book_in_favorites_added(self):
        collector = BooksCollector()
        collector.add_new_book('1984')
        collector.add_book_in_favorites('1984')
        assert '1984' in collector.get_list_of_favorites_books()

    # 6. Удаление из избранного
    def test_delete_book_from_favorites_removed(self):
        collector = BooksCollector()
        collector.add_new_book('Ведьмак')
        collector.add_book_in_favorites('Ведьмак')
        collector.delete_book_from_favorites('Ведьмак')
        assert 'Ведьмак' not in collector.get_list_of_favorites_books()

    # 7. Получение списка по жанру
    def test_get_books_with_specific_genre_filtered(self):
        collector = BooksCollector()
        collector.add_new_book('Дракула')
        collector.set_book_genre('Дракула', 'Ужасы')
        assert 'Дракула' in collector.get_books_with_specific_genre('Ужасы')

    # 8. Повторное добавление книги (не должна добавляться второй раз)
    def test_add_new_book_double_add_not_possible(self):
        collector = BooksCollector()
        collector.add_new_book('Колобок')
        collector.add_new_book('Колобок')
        assert len(collector.get_books_genre()) == 1

    # 9. Жанр книги, которой нет в списке
    def test_get_book_genre_for_non_existent_book_returns_none(self):
        collector = BooksCollector()
        assert collector.get_book_genre('Неизвестность') is None

    # 10. Проверка типа возвращаемого значения словаря
    def test_get_books_genre_returns_dict(self):
        collector = BooksCollector()
        assert isinstance(collector.get_books_genre(), dict)
