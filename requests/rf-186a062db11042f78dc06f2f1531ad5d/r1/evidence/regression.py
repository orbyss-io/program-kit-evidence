"""Regression for the native signed-package adapter with a retained tool lock."""
import json
import sys
import unittest
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "eng"))
import release_bundle


class PackageIdentityTests(unittest.TestCase):
    def test_signed_identity_matches_restore_without_changing_tool_lock(self):
        lock = ROOT / "eng/package_hash/packages.lock.json"
        before = lock.read_bytes()
        package = None
        expected = None
        for assets in (ROOT / "src").rglob("project.assets.json"):
            document = json.loads(assets.read_text(encoding="utf-8"))
            for identity, library in document["libraries"].items():
                if library.get("type") != "package":
                    continue
                name, version = identity.split("/")
                for folder in document["packageFolders"]:
                    candidate = Path(folder) / library["path"] / f"{name.lower()}.{version}.nupkg"
                    if candidate.is_file():
                        with zipfile.ZipFile(candidate) as archive:
                            signed = ".signature.p7s" in archive.namelist()
                        if signed:
                            package, expected = candidate, library["sha512"]
                            break
                if package:
                    break
            if package:
                break
        self.assertIsNotNone(package, "Run native composition prepare to acquire its packages first")
        try:
            self.assertEqual(expected, release_bundle.nuget_content_hash(ROOT, package))
        finally:
            self.assertEqual(before, lock.read_bytes(), "The retained tool lock must remain unchanged")


if __name__ == "__main__":
    unittest.main()
