from pytest import mark


class TestPikabu:
    @mark.pikabu_best
    def test_pikabu_best(self, pikabu_page):
        pikabu_page.open()
        pikabu_page.click_chapter_best()
        pikabu_page.search_text('Лучшие публикации')
