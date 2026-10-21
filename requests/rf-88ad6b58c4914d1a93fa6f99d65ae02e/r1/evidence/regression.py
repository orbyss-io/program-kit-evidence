"""A product's adopted effects must not be attributed to every pure project."""
import sys
import unittest
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / ".specify/extensions/program-kit-governance/scripts"))
from feature_context import context


class CoreEffectRoutingTests(unittest.TestCase):
    def inspect(self, source, inherit=False):
        with patch("feature_context.adopted_context", return_value={"tags": {"dotnet", "api", "persistence"}}):
            return context(ROOT, ROOT / "specs/001-policy-management", "implementation",
                           prose_override="src/PolicyManagement/PolicyManagement.Core/PolicyManagement.Core.csproj",
                           actual_source=[source], inherit_adoption=inherit)

    def test_adoption_still_selects_product_guidance(self):
        self.assertIn("api", self.inspect("", inherit=True))

    def test_empty_and_pure_core_have_no_observed_effects(self):
        for source in ["", "public record PolicyLabel(string Value);"]:
            with self.subTest(source=source):
                self.assertFalse(self.inspect(source) & {"api", "persistence"})

    def test_actual_effects_are_retained(self):
        self.assertIn("persistence", self.inspect("public class PolicyDb : DbContext { }"))
        self.assertIn("api", self.inspect("using Microsoft.AspNetCore.Http;\napp.MapGet(\"/\", () => 1);"))


if __name__ == "__main__":
    unittest.main()
