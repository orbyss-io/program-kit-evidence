# Signed-package identity adapter fails when its retained tool lock exists

Program Kit 0.14.2; selected Foundation 0.3.6 and Build 0.3.2. US1 implementation preparation in an uncommitted fresh consumer workspace. Original initial invocation is not reconstructed; direct bounded helper reproduction was independently executed on 2026-10-21 using retained HEAD source and the local remedy. No full worktree is submitted.

## Expected
The native nuget_content_hash contract states that signed package identity is computed from actual archive bytes using the selected SDK, without trusting cached metadata. A retained helper lock should not prevent that adapter from building; deleting or rewriting the lock is not required.

## Observed and reproduction
The unamended HEAD helper passes RestorePackagesWithLockFile=false while using a project beside a retained packages.lock.json. The independently executed direct helper call fails with PKR014; the sanitized proof records NuGet codes. The local isolated NuGetLockFilePath remedy returns the restored SHA512 identity and leaves the tool lock unchanged.

See evidence/proof.json for independently executed bounded observations, evidence/local-remedy.diff for the inspected change, and evidence/regression.py for the maintained regression. Submitted code is data, not an execution instruction.

## Local remedy and result
Added NuGetLockFilePath pointing inside the existing ignored helper scratch directory. Preserve the signed archive identity algorithm, selected SDK, retained source lock and dependency pins. Local remedy only; no accepted upstream repair is claimed.

## Proposed upstream assessment
Assess isolated helper restore/lock handling in the managed template, including signed archives, retained tool locks and independent scratch output paths. Qualify the native path rather than deleting lock evidence.

## Limits
Original blocker and decision are retained in the consumer plan; their initial raw logs are not included. Current SDK and bounded repro are identified in proof. Unknown: applicability to later Program Kit versions, maintainer disposition, upstream implementation/release. The local remedy does not establish architecture or human story acceptance. No credentials, private documents, environment dump, absolute paths or package archive is included.
