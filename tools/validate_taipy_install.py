import logging
import os
import sys


def test_import_taipy_packages() -> bool:
    """
    Import taipy package and call gui, Scenario and rest attributes.
    """
    import taipy as tp

    valid_install = True
    if not hasattr(tp, "gui"):
        logging.error("Taipy installation has no attribute gui")
        valid_install = False
    if not hasattr(tp, "Scenario"):
        logging.error("Taipy installation has no attribute Scenario")
        valid_install = False
    if not hasattr(tp, "rest"):
        logging.error("Taipy installation has no attribute rest")
        valid_install = False

    return valid_install


def is_taipy_gui_install_valid() -> bool:
    from pathlib import Path

    import taipy

    taipy_gui_core_path = Path(taipy.__file__).absolute().parent / "gui_core" / "lib" / "taipy-gui-core.js"
    if not taipy_gui_core_path.exists():
        logging.error("File taipy-gui-core.js not found in taipy installation path")
        return False

    taipy_gui_webapp_path = Path(taipy.__file__).absolute().parent / "gui" / "webapp"

    if not os.path.exists(taipy_gui_webapp_path):
        return False

    if not any(fname.endswith('.js') for fname in os.listdir(taipy_gui_webapp_path)):
        logging.error("Missing js files inside taipy gui webapp folder")
        return False

    return True


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)

    logging.info("Trying to import taipy and verify it's main attributes")
    if not test_import_taipy_packages() or not is_taipy_gui_install_valid():
        sys.exit(1)

    logging.info("Taipy installation Validated")
    sys.exit(0)
