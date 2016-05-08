import Queue
import threading
import util
import ruleset
import http
import pytest

class TestRunner():
    """
    Runner that accepts stages of a test and verifies expected and actual
    responses
    @TODO
    Accept logger objects for assertions
    """
    def test_status(self, expected_status, actual_status):
        """
        Compares the expected output against actual output of test and stage
        In a separate function to make debugging easy with py.test
        """
        assert expected_status == actual_status
        
    def run_stage(self, stage):
        """
        Runs a stage in a test by building an httpua object with the stage
        input, waits for output then compares expected vs actual output
        """
        http_ua = http.HttpUA(stage.input)
        http_ua.send_request()
        self.test_status(stage.output.status,http_ua.response_object.status)