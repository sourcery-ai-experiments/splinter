import io
import tempfile


class HTMLSnapshotTest(object):
    def test_html_snapshot(self):
        """Should take an html snapshot of the current page."""
        filename = self.browser.html_snapshot()
        self.assertTrue(tempfile.gettempdir() in filename)

    def test_html_snapshot_with_prefix(self):
        """Should add the prefix to the snapshot filename"""
        filename = self.browser.html_snapshot(name="foobar")
        self.assertTrue("foobar" in filename)

    def test_html_snapshot_with_suffix(self):
        """Should add the suffix to the snapshot filename"""
        filename = self.browser.html_snapshot(suffix="xml")
        self.assertEqual("xml", filename[-3:])

    def test_html_snapshot_content_correct(self):
        """The content of an HTML snapshot should match the actual page."""
        html = self.browser.html

        filename = self.browser.html_snapshot()
        with io.open(filename, 'r', encoding='utf-8') as f:
            snapshot = f.read()
        self.assertEqual(snapshot, html)
