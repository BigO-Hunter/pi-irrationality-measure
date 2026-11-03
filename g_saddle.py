"""Zeilberger–Zudilin's exact g(y) saddle analysis (arXiv:1912.06345).

g(y) = y(y^2+6y+25)^2/(y-25)^3, saddle roots of 2y^3-125y^2-500y-625=0.
Measure: 1 + log N_3 / |log N_1| + correction terms (Salikhov F(n)/lcm).
Reproduction target: 7.10320533413700172750577342281...
"""
import mpmath as mp

mp.mp.dps = 60


def g(y):
    return y*(y*y+6*y+25)**2/(y-25)**3


def saddle_roots():
    f = lambda y: 2*y**3-125*y**2-500*y-625
    roots = []
    for guess in (mp.mpc(-2, 1.013), mp.mpc(-2, -1.013), 66.34):
        roots.append(mp.findroot(f, guess, tol=mp.mpf('1e-50')))
    return roots


def measure():
    ys = saddle_roots()
    # y_3 = the large positive root (b_n growth); y_{1,2} = conjugate pair (I_n decay)
    far = max(ys, key=lambda y: abs(y))
    near = [y for y in ys if y != far]
    n3 = g(far)
    n1 = g(near[0])
    corr = -mp.mpf(5)/2*mp.log(2) + 4 - mp.pi/(2*mp.sqrt(3)) + mp.log(3*mp.sqrt(3)/4)
    logI = mp.log(abs(n1)) + corr
    logB = mp.log(abs(n3)) + corr
    return 1 + logB/abs(logI), (n1, n3, logI, logB, far, near)


if __name__ == '__main__':
    val, (n1, n3, logI, logB, far, near) = measure()
    print('far saddle y3 =', mp.nstr(far, 16))
    print('N3 = g(y3) =', mp.nstr(n3, 18))
    print('|N1| =', mp.nstr(abs(n1), 16))
    print('log|I_n|/n =', mp.nstr(logI, 16))
    print('log b_n/n  =', mp.nstr(logB, 16))
    print('measure    =', mp.nstr(val, 20))
    print('target:      7.10320533413700172750577342281')
