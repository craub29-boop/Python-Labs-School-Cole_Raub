import runpy

ns = runpy.run_path('wordle zolver')
suggest_word = ns['suggest_word']
all_words = ns['load_word_list']()


def test_cluster_guess_uses_real_dictionary_word():
    words = ["dusty", "gusty", "musty"]
    guess = suggest_word(words, full_words=all_words)
    assert guess in all_words
    assert guess not in words
    assert len(set(guess) & {"d", "g", "m"}) >= 2


def test_regular_word_list_still_returns_valid_guess():
    words = ["stare", "crane", "slate", "share"]
    guess = suggest_word(words, full_words=all_words)
    assert isinstance(guess, str)
    assert len(guess) == 5
