import os
from numpy import linspace as ls, meshgrid, cos, sin, pi
from numpy.random import ranf
import matplotlib.pyplot as pp


def solve(u0, x0, a, b, s, r, phi):
    def ui(r, phi):
        return -u0 / x0 * (a / b) ** (s - 1) * r * cos(phi)

    def u(r, phi):
        return -u0 / x0 * (r / b) ** (s - 1) * r * cos(phi)

    def ue(r, phi):
        return -u0 / x0 * r * cos(phi)

    return ui(r, phi), u(r, phi), ue(r, phi)


if __name__ == '__main__':
    u0, x0, a, b, s = ranf(5) * 10
    # u0, x0, a, b, s = 1, 2, 3, 4, ranf() + 1

    dirname = f'u0={u0} x0={x0} a={a} b={b} s={s}'
    os.mkdir(dirname)
    os.chdir(dirname)

    r, phi = ls(0, 3), ls(0, 2 * pi)
    rm, phim = meshgrid(r, phi)

    ui, u, ue = solve(u0, x0, a, b, s, rm, phim)

    pp.figure()
    pp.contour(rm * cos(phim), rm * sin(phim), ui)
    pp.title('ui plot')
    pp.xlabel('x')
    pp.ylabel('y')
    pp.savefig('ui.png')

    pp.figure()
    pp.contour(rm * cos(phim), rm * sin(phim), u)
    pp.title('u plot')
    pp.xlabel('x')
    pp.ylabel('y')
    pp.savefig('u.png')

    pp.figure()
    pp.contour(rm * cos(phim), rm * sin(phim), ue)
    pp.title('ue plot')
    pp.xlabel('x')
    pp.ylabel('y')
    pp.savefig('ue.png')
