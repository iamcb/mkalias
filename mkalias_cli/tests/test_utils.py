from mkalias_cli import utils


def test_check_path_of_dir(tmpdir):
    assert utils.check_path(tmpdir) == True


def test_check_path_of_file(tmp_path):
    f = tmp_path / "test_file01"
    f.write_text("content")
    assert utils.check_path(f) == True
