"""Independent regression tests for the synthetic claim-separation checker."""
import unittest
from check import CASES, assess

class ClaimSeparationTests(unittest.TestCase):
    def test_all_published_vectors(self):
        self.assertEqual(len(CASES), 9)
        self.assertEqual(len({case['id'] for case in CASES}), len(CASES))
        for case in CASES:
            with self.subTest(case=case['id']):
                self.assertEqual(assess(case), case['expected'])

    def test_each_dimension_changes_only_its_own_output(self):
        baseline = dict(authorized=True, execution_reported=True,
                        expected_effect='v1', observation='v1')
        original = assess(baseline)
        for field, changed, output in [
            ('authorized', False, 'authorization'),
            ('execution_reported', False, 'execution'),
            ('observation', 'v2', 'current_effect'),
        ]:
            with self.subTest(field=field):
                mutated = dict(baseline, **{field: changed})
                result = assess(mutated)
                self.assertNotEqual(result[output], original[output])
                self.assertEqual({k: v for k,v in result.items() if k != output},
                                 {k: v for k,v in original.items() if k != output})

    def test_missing_observation_is_not_mismatch(self):
        for authorized in (True, False):
            for reported in (True, False):
                case = dict(authorized=authorized, execution_reported=reported,
                            expected_effect='v1', observation=None)
                self.assertEqual(assess(case)['current_effect'], 'NOT_ESTABLISHED')

if __name__ == '__main__':
    unittest.main()
