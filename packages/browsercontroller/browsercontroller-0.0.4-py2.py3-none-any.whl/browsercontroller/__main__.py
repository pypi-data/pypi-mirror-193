"""Entry point for the project."""

from browsercontroller.get_controller import get_ubuntu_apt_firefox_controller

# TODO: Check if apt version of firefox is installed, if not, ensure it is.
# run_bashardcodedommand()

get_ubuntu_apt_firefox_controller(
    url="https://www.startpagina.nl",
    default_profile=False)
