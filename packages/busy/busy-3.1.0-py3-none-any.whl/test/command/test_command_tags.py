from unittest import TestCase
from tempfile import TemporaryDirectory
from pathlib import Path
from unittest import mock
from io import StringIO
from datetime import date as Date

from busy.command.tags_command import TagsCommand
from busy.queue.queue import Queue


# Tired of testing pure units, I present a 2-level integration test

class TestCommandTags(TestCase):

    def test_tags(self):
        q = Queue(items=['a #b', 'c #d', 'e #b'])
        c = TagsCommand()
        c._queue_ = q
        tx = c.call_method()
        self.assertEqual(tx, 'b\nd')
