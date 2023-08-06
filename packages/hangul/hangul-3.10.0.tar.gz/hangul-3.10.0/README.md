## Hangul-Latin Transliteration

### Installation

```console
$ pip install hangul
```

### Usage

```python
>>> import hangul
>>> hangul.romanize('나는 TV를 사랑')
naneun TVreul sarang
```

In-memory file-like object

```python
>>> import hangul
>>> hangul.Hangul().romanize('나는 TV를 사랑')
<_io.StringIO object at memory>
```

### References

* https://web.archive.org/web/20070916025652/http://www.korea.net/korea/kor_loca.asp?code=A020303

* https://www.korean.go.kr/front_eng/roman/roman_01.do