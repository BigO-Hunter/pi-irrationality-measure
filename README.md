# Historical certificate for the Zeilberger–Zudilin π bound

**Status update (3 November 2026):** this is now a historical numerical
certificate, not a current-record artifact. OpenAI's September 2026 preprint
[*The irrationality exponent of π is 2*](https://github.com/openai/math/tree/main/preprints/The-irrationality-exponent-of-pi-is-2-September-24-2026)
proves the exact value μ(π) = 2, and its public
[Lean formalization](https://github.com/openai/math/blob/main/lean/OAI/NumberTheory/PiExponent/Main.lean)
contains `pi_irrationalityExponent_eq_two`. Prove2Me marks the corresponding
[campaign](https://prove2.me/campaigns/pi-irrationality-measure) solved on
28 October 2026. Consequently no improvement within the Salikhov integral
family can improve the best-known upper bound.

This repository independently computes, at 60-digit precision, the asymptotic
quantities behind the Zeilberger–Zudilin (2020) upper bound

    mu(pi) <= 7.10320533413700172750577342281...

and **reproduces that published value to 19 significant digits**. It does not
contain a Lean formalization or a new proof of the bound.

## What is whose

- **V. Kh. Salikhov** (2008/2010): the ingenious integral and its partial-fraction
  method that produced the earlier record 7.606308.
- **Doron Zeilberger & Wadim Zudilin** (2020, arXiv:1912.06345): the variant of
  Salikhov's construction that produced the 2020 record 7.103205334137, the
  Almkvist–Zeilberger recurrence, its indicial polynomial, and the saddle-point
  asymptotics this certificate recomputes.
- **MultiAgency / darkhipo**: the independent exact computation — the saddle
  roots of `2y^3 - 125y^2 - 500y - 625 = 0`, `g(y) = y(y^2+6y+25)^2/(y-25)^3`
  evaluated at those roots, the correction terms from Salikhov's F(n)/lcm
  structure, and the final measure. This is a certificate of the numerical
  claims of the cited paper, not a new proof of the bound and not (yet) a
  Lean 4 formalization.

## The certificate

`certify_pi.py` computes:

- the three saddle roots of `2y^3 - 125y^2 - 500y - 625 = 0`
  (y3 = 66.339501524621408..., matching the paper's 66.33950152);
- `N_3 = g(y_3) = 21851.69139621956...` (paper: 21851.691396);
- `|N_1| = 0.029458495928116876...` (paper: 0.029458495928);
- `log|I_n|/n = -1.902916485599982` (paper: -1.90291648559998);
- `log b_n/n = 11.61389004533105` (paper: 11.613890045331);
- the measure `1 + log N_3 / |log N_1| = 7.103205334137001727505773...`,
  equal to the published target to 19 significant digits.

`receipt.json` records all of these with `matches_to_19_digits: true`.

## Reproduction

    python3 certify_pi.py

(stdlib mpmath only; no other dependencies.)

## Later literature

- Yufei Bai (2026, arXiv:2609.11276) improved the integral-family bound to
  7.101862832357 before the exact μ(π) = 2 result.
- David Niedbala Giraudin (2026, arXiv:2609.37459) subsequently gave a
  closed-form law for the Salikhov–Zeilberger–Zudilin–Bai family, calibrated it
  against all three bounds, and supplied computational evidence that Bai's point
  is the family's global optimum. Its global-optimality conclusion is labelled
  a conjecture by that preprint, not a proof.
