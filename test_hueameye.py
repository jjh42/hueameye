import unittest
import hueameye

class TestReply(unittest.TestCase):
    def test_get_info_empty_result(self):
        """Check we can query email addresses."""
        self.assertEqual(hueameye.get_info('jjh@42quarks.com'), {})
        self.assertEqual(hueameye.get_info('test@example.com'), {})
    
    def test_get_info_with_result(self):
        res = hueameye.get_info('chein@edgewood.edu')
        self.assertEqual(len(res), 3)

    def test_empty_build_msg(self):
        """Check that build message works with no info."""
        msg = hueameye.build_msg('test@example.com', {})
        self.assertTrue(msg.body.find('We got nothing') > 0)

    def test_nonempty_build_msg(self):
        """Check that build message works when we do have info."""
        msg = hueameye.build_msg('test@example.com', {'Name' : 'Sarah Jane',
                                                       'Gender' : 'Female'})
        for l in ['Gender', 'Female', 'Name', 'Sarah']:
            self.assertTrue(msg.body.find(l) > 0)

