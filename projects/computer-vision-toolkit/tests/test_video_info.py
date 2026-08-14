from pathlib import Path
import importlib.util

MODULE = Path(__file__).parents[1] / "main.py"
spec = importlib.util.spec_from_file_location("cv_toolkit", MODULE)
assert spec and spec.loader
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


def test_missing_video_raises(tmp_path: Path):
    missing = tmp_path / "missing.mp4"
    try:
        module.video_info(str(missing))
    except FileNotFoundError:
        return
    raise AssertionError("expected FileNotFoundError")
