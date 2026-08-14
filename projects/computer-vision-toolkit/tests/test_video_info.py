from pathlib import Path

from projects.computer_vision_toolkit.main import video_info


def test_missing_video_raises(tmp_path: Path):
    missing = tmp_path / "missing.mp4"
    try:
        video_info(str(missing))
    except FileNotFoundError:
        return
    raise AssertionError("expected FileNotFoundError")
