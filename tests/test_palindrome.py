def test_pytest():
    assert 2+2 == 4

    from main import palindrome

    def test_palindrome_happy():
        assert palindrome("radar") == True
        assert palindrome("Radar") == True

    def test_palindrome_unhappy():
        assert palindrome("radars") == False