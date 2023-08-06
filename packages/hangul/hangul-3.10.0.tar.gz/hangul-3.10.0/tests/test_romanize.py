from hangul import Hangul, romanize


def test_romanize():
    app = Hangul()
    assert app.jamo('를') == ('ᄅ', 'ᅳ', 'ᆯ')
    assert app.romanize('나는 TV를 사랑').read() == 'naneun TVreul sarang'
    assert app.romanize('없을').read() == 'eopseul'
    assert romanize('생각') == 'saenggak'
