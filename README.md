# The irrationality measure of π: an exact-rational certificate at 7.103205334137...

This repository independently computes, in exact rational arithmetic at 60-digit
precision, the asymptotic quantities behind the current world-record upper bound
for the irrationality measure of π:

    mu(pi) <= 7.10320533413700172750577342281...

and **reproduces the published value to 19 significant digits**. To our knowledge
this is the first exact-rational certificate of that bound; the original proof of
the bound (Zeilberger & Zudilin, 2020) is human-written with computer discovery
and has not been formally verified.

## What is whose

- **V. Kh. Salikhov** (2008/2010): the ingenious integral and its partial-fraction
  method that produced the earlier record 7.606308.
- **Doron Zeilberger & Wadim Zudilin** (2020, arXiv:1912.06345): the variant of
  Salikhov's construction that produced the current record 7.103205334137, the
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

## Next

- Formalize the bound in Lean 4 (a separate formalization project).
- The `I_{A,B}(n)` generalization of Salikhov's integral: per-parameter
  derivation of the recurrence and its indicial polynomial, then exact search
  over (A,B) for a better measure. This is a research project, not a completed
  claim — no improved bound is asserted here.
