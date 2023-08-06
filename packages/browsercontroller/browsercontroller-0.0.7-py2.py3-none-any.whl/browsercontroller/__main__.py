"""Entry point for the project."""


from browsercontroller.get_controller import get_ubuntu_apt_firefox_controller
from src.browsercontroller.check_if_firefox_is_installed import (
    run_bashardcodedommand,
)

# Check if apt version of firefox is installed, if not, ensure it is.
ensure_apt_firefox_command: str = (
    'bash -c "source src/browsercontroller/firefox_version.sh '
    + 'swap_snap_firefox_with_ppa_apt_firefox_installation"'
)
run_bashardcodedommand(bashCommand=ensure_apt_firefox_command)

get_ubuntu_apt_firefox_controller(
    url="https://www.github.com", default_profile=False
)
