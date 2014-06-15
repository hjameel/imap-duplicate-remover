#!/usr/bin/env python
import unittest
import mock

class TestImapDuplicateRemover(unittest.TestCase):
    @mock.patch("imaplib.IMAP4_SSL")
    def test_does_nothing_if_no_mails_in_mailbox(self, imap_4):
        import imap_duplicate_remover
        imap_duplicate_remover.remove_duplicates()

        assert not imap_4.return_value.store.called

if __name__ == "__main__":
    unittest.main()
