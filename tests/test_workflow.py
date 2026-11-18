import copy
import json
from pathlib import Path
import subprocess
import sys
import unittest

from captions.workflow import report


class WorkflowTest(unittest.TestCase):
    def setUp(self):
        self.path = Path(__file__).resolve().parents[1] / 'data' / 'sample.json'
        self.data = json.loads(self.path.read_text(encoding='utf-8'))

    def test_entry(self):
        result = subprocess.run([sys.executable, '-m', 'captions', 'intake', str(self.path)],
                                check=True, capture_output=True, text=True)
        self.assertEqual(json.loads(result.stdout), report(self.data))

    def test_audit_and_complaint_not_interchangeable(self):
        result = report(self.data)
        self.assertEqual(result['references']['c/1'],['v1','v2'])
        self.assertEqual(result['verification']['original'],{'missing':1})
        self.assertEqual(result['inbox'],[{'ticket':'R1','edition':'v2','frozen':True}])

    def test_duplicate_draw_is_rejected(self):
        self.data['draws'].append(copy.deepcopy(self.data['draws'][0]))
        with self.assertRaises(ValueError):
            report(self.data)
