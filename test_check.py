"""Negative tests and full synthetic claim-separation coverage."""
import itertools
import unittest
from check import CASES, assess

class ClaimSeparationTests(unittest.TestCase):
    def test_all_published_vectors(self):
        self.assertEqual(len(CASES), 12)
        self.assertEqual(len({c["id"] for c in CASES}), 12)
        for case in CASES:
            with self.subTest(case=case["id"]):
                self.assertEqual(assess(case), case["expected"])

    def test_complete_cross_product(self):
        seen = {(c["authorized"], c["execution_reported"], c["expected"]["current_effect"]) for c in CASES}
        wanted = set(itertools.product((True, False), (True, False),
                                      ("CONFIRMED", "CONTRADICTED", "NOT_ESTABLISHED")))
        self.assertEqual(seen, wanted)

    def test_dimension_independence(self):
        base = dict(authorized=True, execution_reported=True, expected_effect="v1", observation="v1")
        original = assess(base)
        for field, value, output in (
            ("authorized", False, "authorization"),
            ("execution_reported", False, "execution"),
            ("observation", "v2", "current_effect"),
        ):
            with self.subTest(field=field):
                result = assess(dict(base, **{field: value}))
                self.assertNotEqual(result[output], original[output])
                self.assertEqual({k:v for k,v in result.items() if k != output},
                                 {k:v for k,v in original.items() if k != output})

    def test_missing_observation_not_contradiction(self):
        for authorized, reported in itertools.product((True, False), repeat=2):
            case = dict(authorized=authorized, execution_reported=reported,
                        expected_effect="v1", observation=None)
            self.assertEqual(assess(case)["current_effect"], "NOT_ESTABLISHED")

    def test_reject_nonboolean_authority_and_report(self):
        base = dict(authorized=True, execution_reported=True, expected_effect="v1", observation="v1")
        for key in ("authorized", "execution_reported"):
            for bad in ("false", "true", 0, 1, None, [], {}):
                with self.subTest(key=key, bad=repr(bad)):
                    with self.assertRaises(TypeError):
                        assess(dict(base, **{key: bad}))

    def test_reject_invalid_observation_and_target(self):
        base = dict(authorized=True, execution_reported=True, expected_effect="v1", observation="v1")
        for key, bad in (("expected_effect", None), ("expected_effect", 1),
                         ("observation", False), ("observation", 2), ("observation", [])):
            with self.subTest(key=key, bad=repr(bad)):
                with self.assertRaises(TypeError):
                    assess(dict(base, **{key: bad}))

    def test_refusal_baseline_is_not_requested_value(self):
        # A denied write must leave the pre-existing state untouched.
        requested = "new"
        before = "old"
        refused = dict(authorized=False, execution_reported=False,
                       expected_effect=before, observation=before)
        self.assertEqual(assess(refused)["current_effect"], "CONFIRMED")
        self.assertNotEqual(requested, refused["expected_effect"])

if __name__ == "__main__":
    unittest.main()
