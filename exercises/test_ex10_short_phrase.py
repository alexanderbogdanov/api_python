def test_short_phrase():
    phrase = input("Set a phrase, which is shorter than 15 characters: \n")
    assert (
        len(phrase) < 15
    ), f"Your phrase isn't shorter than 15 characters, you dog. It's {len(phrase)}"
