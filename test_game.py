import game


def test_get_choice_accepts_valid_choice(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: " 2 ")

    assert game.get_choice() == "2"


def test_get_choice_rejects_invalid_data(monkeypatch, capsys):
    choices = iter(["0", "abc", "3"])
    monkeypatch.setattr("builtins.input", lambda _: next(choices))

    assert game.get_choice() == "3"
    assert capsys.readouterr().out.count("Введите 1, 2 или 3.") == 2


def test_play_game_ends_with_victory(monkeypatch, capsys):
    monkeypatch.setattr("builtins.input", lambda _: "1")

    game.play_game()

    output = capsys.readouterr().out
    assert "Победа! Вы достигли цели." in output
    assert "сокровища=12" not in output


def test_play_game_ends_when_health_reaches_zero(monkeypatch, capsys):
    monkeypatch.setattr("builtins.input", lambda _: "3")

    game.play_game()

    output = capsys.readouterr().out
    assert "Ваше здоровье упало до нуля. Игра окончена." in output
    assert "Итог: энергия=0, здоровье=0, сокровища=8" in output


def test_play_game_ends_when_time_runs_out(monkeypatch, capsys):
    monkeypatch.setattr("builtins.input", lambda _: "2")

    game.play_game()

    output = capsys.readouterr().out
    assert "Время закончилось." in output
    assert "Итог: энергия=18, здоровье=18, сокровища=10" in output