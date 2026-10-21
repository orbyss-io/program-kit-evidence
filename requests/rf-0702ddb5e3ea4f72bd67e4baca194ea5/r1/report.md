# Dutch signed-out landing renders English copy; product-logo branding is unavailable

Program Kit 0.14.2 with Foundation 0.3.6 publishes an anonymous browser presentation
at `/auth/signed-out`. In an actual synthetic-account sign-out, configured
`DefaultLocale=nl`, `SupportedLocales=[nl,en]` and `Presentation.Locale=nl` produced
`<html lang="nl">` while displaying:

```
Session status
No local session is active.
Sign in
Return to application
```

The application name and selected green theme appear, but no logo image is rendered.
The captured complete presentation settings contract exposes ApplicationName,
Locale, Theme, route/return paths, confirmation, response policies and a bounded
Copy map. Theme accepts blue/green/slate; a logo/brand-asset setting is absent.

Reproduce with the native Web.Presentation and BFF features: configure the values
in `evidence/signed-out-observation.json`, sign in using a synthetic user, perform
native sign-out and inspect the anonymous landing. The observation is independently
executed; the selected publisher contract is inspected evidence. No claim is made
about releases after these exact selected versions.

Please assess (1) locale-aware default copy and documented propagation of the
consumer's selected language across authentication completion, and (2) a safe,
documented product-logo/branding contribution shared by anonymous authentication
pages. A per-shell Copy override exists as a manual-copy seam; it does not establish
automatic translation or propagation from an application's language selector.
The branding expectation is a consumer product requirement; the current contract
does not promise arbitrary brand assets. Report this as a proposed capability gap,
not an already accepted maintainer diagnosis or architecture.

No signed-out workaround or publisher replacement was applied. Unrelated settings
dialog and Keycloak field-border CSS repairs remain consumer-owned. The current
signed-out page is usable but has this language/branding discontinuity. Production,
real documents, newer-version behavior and maintainer disposition remain unknown.

Only the selected public contract and a sanitized public-page observation are
included. The consumer display name is replaced with a pseudonym. Original local
screenshots and full source remain local; no cookies, tokens, credentials, account
IDs, private paths, policy records, environment dumps or binary attachments are sent.
