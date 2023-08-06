from pathlib import Path

def test_aboutpage():
    readme_file = Path(__file__).parent.parent / 'Readme.md'
    assert readme_file.is_file()