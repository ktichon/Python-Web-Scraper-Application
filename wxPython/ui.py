"""UI module containing UI class."""
from frm_main import frmMain


class UI(frmMain):
    """UI class."""

    def __init__(self):
        """Init method."""
        try:
            frmMain.__init__(self, None)
        except Exception as e:
            print(f"UI::Init::{e}")

    def calc(self, first_name: str, last_name: str) -> str:
        """Perform some string maneuvers."""
        try:
            result = f"{last_name[::2]}, {first_name[::-1]}"
        except Exception as e:
            print(f"UI::calc::{e}")
        return result

    def cmdSave_click(self, event):
        """Save click event."""
        try:
            first = self.txtFirstName.Value
            last = self.txtLastName.Value
            result = self.calc(first, last)
            self.lblResult.Label = f"Mangled the names: {result}"
        except Exception as e:
            print(f"UI::cmdSave_click::{e}")
