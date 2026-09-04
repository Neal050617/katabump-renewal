import unittest
from unittest.mock import patch

import main


class RenewalResultTests(unittest.TestCase):
    def test_explicit_success_is_true(self):
        with patch.object(main, "_read_alert", return_value="Server renewed successfully"), patch.object(
            main, "send_tg_message"
        ):
            self.assertTrue(main._check_renew_result(object()))

    def test_unknown_result_is_false(self):
        with patch.object(main, "_read_alert", return_value=""), patch.object(
            main.time, "sleep"
        ), patch.object(main, "send_tg_message"):
            self.assertFalse(main._check_renew_result(object()))

    def test_not_due_is_operational_success(self):
        with patch.object(main, "_goto_server_detail", return_value="not_due"):
            self.assertTrue(main.renew_server(object()))

    def test_missing_renew_entry_fails(self):
        with patch.object(main, "_goto_server_detail", return_value="error"):
            self.assertFalse(main.renew_server(object()))


if __name__ == "__main__":
    unittest.main()
