"""Synthetic cumulative-disclosure boundary tests; no production authorization claims."""
import unittest

def decide(committed, observed, reconstruction_sets, threshold_proven):
    """Return a claim-separated decision; missing evidence fails closed."""
    if not committed or not threshold_proven or reconstruction_sets is None:
        return "DENY_UNESTABLISHED"
    released = set(observed)
    if any(set(s).issubset(released) for s in reconstruction_sets):
        return "DENY_RECONSTRUCTABLE"
    return "PERMIT_WITHIN_MODEL"

class CumulativeDisclosureTests(unittest.TestCase):
    def test_precommitment_without_derivation_is_insufficient(self):
        self.assertEqual(decide(True, ["a"], [{"a", "b"}], False), "DENY_UNESTABLISHED")

    def test_missing_reconstruction_model_fails_closed(self):
        self.assertEqual(decide(True, ["a"], None, True), "DENY_UNESTABLISHED")

    def test_non_fungible_chunks_cross_early(self):
        # A key plus one payload chunk reconstructs; scalar 3-of-N misses it.
        self.assertEqual(decide(True, ["key", "payload1"], [{"key", "payload1"}, {"key", "payload2"}], True), "DENY_RECONSTRUCTABLE")

    def test_same_count_different_sets(self):
        model = [{"key", "payload1"}]
        self.assertEqual(decide(True, ["key", "payload1"], model, True), "DENY_RECONSTRUCTABLE")
        self.assertEqual(decide(True, ["payload1", "payload2"], model, True), "PERMIT_WITHIN_MODEL")

    def test_per_step_reversible_does_not_override_cumulative(self):
        self.assertEqual(decide(True, ["key", "payload1"], [{"key", "payload1"}], True), "DENY_RECONSTRUCTABLE")

if __name__ == "__main__":
    unittest.main()
