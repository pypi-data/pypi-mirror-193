from sdfspu.sdf_text import (
    randstring,
    split_name,
    obsc_email,
    path_is_url,
    dict_to_json_file,
    str_hash,
)


def test_randstring():
    pass


def test_randstring():
    assert isinstance(randstring(), str)
    assert len(randstring(k_=20)) == 20
    assert len(randstring(k_=120)) == 120
    assert " " not in randstring()


def test_split_name():
    assert split_name("ok simple") == ("ok", "simple")
    assert split_name("solo") == ("", "solo")
    assert split_name("three part name") == ("three part", "name")
    assert split_name("name with-hyphen") == ("name", "with-hyphen")
    assert split_name("") == ("", "")


def test_obsc_email():
    assert obsc_email("something@example.com") == "som...@e..."


def test_path_is_url():
    assert path_is_url("https://github.com/soundmaking/sdfspu")
    assert path_is_url("http://example.com")  # noqa
    assert not path_is_url("/home/pi/gitclones/sdfspu/tests/test_sdf_text.py")
    assert not path_is_url("192.168.1.123")


def test_str_hash():
    example_hash = "0bc83cb571cd1c50ba6f3e8a78ef1346"
    assert str_hash("myemailaddress@example.com") == example_hash
    assert str_hash("myemailaddress@example.com ") == example_hash
    assert str_hash("MyEmailAddress@example.com ") == example_hash
    assert str_hash(" MyEmailAddress@example.com ") == example_hash
    assert str_hash("MyEmailAddress@example.com") == example_hash
