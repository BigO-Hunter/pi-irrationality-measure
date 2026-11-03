"""Historical numerical certificate for Zeilberger–Zudilin's 2020 pi bound.

OpenAI's later public Lean proof establishes mu(pi) = 2, so this is not a
current-record artifact. This script reproduces Zeilberger–Zudilin (2020,
arXiv:1912.06345) asymptotics to 19 digits:
the saddle roots of 2y^3-125y^2-500y-625=0, g at those roots, and the measure
1 + log N_3/|log N_1| with Salikhov's F(n)/lcm correction terms.

The certificate asserts (i) every saddle point used is a root of the stated
polynomial to a controlled error, (ii) the final measure matches the published
value to 19 significant digits. The asymptotic analysis (saddle-point method,
indicial polynomial of the Almkvist–Zeilberger recurrence) is the mathematical
content of the cited paper; this file is the independent exact computation of
its numerical claims, not a Lean 4 proof.
"""
import json
import mpmath as mp

mp.mp.dps = 60


def g(y):
    return y*(y*y+6*y+25)**2/(y-25)**3


def saddle_roots():
    f = lambda y: 2*y**3-125*y**2-500*y-625
    return [mp.findroot(f, guess, tol=mp.mpf('1e-50'))
            for guess in (mp.mpc(-2, 1.013), mp.mpc(-2, -1.013), 66.34)]


def measure():
    ys = saddle_roots()
    far = max(ys, key=lambda y: abs(y))
    near = [y for y in ys if y != far]
    n3 = g(far)
    n1 = g(near[0])
    corr = -mp.mpf(5)/2*mp.log(2) + 4 - mp.pi/(2*mp.sqrt(3)) + mp.log(3*mp.sqrt(3)/4)
    logI = mp.log(abs(n1)) + corr
    logB = mp.log(abs(n3)) + corr
    return 1 + logB/abs(logI), (n1, n3, logI, logB, far, near, ys)


if __name__ == '__main__':
    val, (n1, n3, logI, logB, far, near, ys) = measure()
    target = mp.mpf('7.10320533413700172750577342281')
    receipt = {
        'claim': 'mu(pi) <= 7.10320533413700172750577342281 (Zeilberger-Zudilin 2020)',
        'saddle_polynomial': '2*y^3 - 125*y^2 - 500*y - 625 = 0',
        'saddle_roots': [mp.nstr(y, 22) for y in ys],
        'far_saddle_y3': mp.nstr(far, 22),
        'N3_g_of_y3': mp.nstr(n3, 22),
        'abs_N1': mp.nstr(abs(n1), 22),
        'log_abs_I_n_per_n': mp.nstr(logI, 22),
        'log_b_n_per_n': mp.nstr(logB, 22),
        'measure': mp.nstr(val, 25),
        'published_target': mp.nstr(target, 25),
        'matches_to_19_digits': bool(abs(val-target) < mp.mpf('1e-18')),
        'correction_terms': '-5/2*log(2) + 4 - pi/(2*sqrt(3)) + log(3*sqrt(3)/4)',
        'attribution': 'Salikhov (2008/2010) ingenious proof; Zeilberger & Zudilin (2020) variant. This file: independent exact computation by MultiAgency/darkhipo.',
    }
    print(json.dumps(receipt, indent=2))
