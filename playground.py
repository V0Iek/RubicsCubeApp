from classes import Button

def playground(screen, cube):
    btn_u = Button(screen, 10, screen.get_height() * .8, screen.get_height() / 21.6, screen.get_height() / 21.6, "U", (128, 128, 128), (0, 128, 128), cube.U)
    btn_up = Button(screen, 70, screen.get_height() * .8, screen.get_height() / 21.6, screen.get_height() / 21.6, "U'", (128, 128, 128), (0, 128, 128), cube.Up)
    btn_e = Button(screen, 130, screen.get_height() * .8, screen.get_height() / 21.6, screen.get_height() / 21.6, "E", (128, 128, 128), (0, 128, 128), cube.E)
    btn_ep = Button(screen, 190, screen.get_height() * .8, screen.get_height() / 21.6, screen.get_height() / 21.6, "E'", (128, 128, 128), (0, 128, 128), cube.Ep)
    btn_d = Button(screen, 250, screen.get_height() * .8, screen.get_height() / 21.6, screen.get_height() / 21.6, "D", (128, 128, 128), (0, 128, 128), cube.D)
    btn_dp = Button(screen, 310, screen.get_height() * .8, screen.get_height() / 21.6, screen.get_height() / 21.6, "D'", (128, 128, 128), (0, 128, 128), cube.Dp)
    btn_l = Button(screen, 370, screen.get_height() * .8, screen.get_height() / 21.6, screen.get_height() / 21.6, "L", (128, 128, 128), (0, 128, 128), cube.L)
    btn_lp = Button(screen, 430, screen.get_height() * .8, screen.get_height() / 21.6, screen.get_height() / 21.6, "L'", (128, 128, 128), (0, 128, 128), cube.Lp)
    btn_m = Button(screen, 490, screen.get_height() * .8, screen.get_height() / 21.6, screen.get_height() / 21.6, "M", (128, 128, 128), (0, 128, 128), cube.M)
    btn_mp = Button(screen, 10, screen.get_height() * .9, screen.get_height() / 21.6, screen.get_height() / 21.6, "M'", (128, 128, 128), (0, 128, 128), cube.Mp)
    btn_r = Button(screen, 70, screen.get_height() * .9, screen.get_height() / 21.6, screen.get_height() / 21.6, "R", (128, 128, 128), (0, 128, 128), cube.R)
    btn_rp = Button(screen, 130, screen.get_height() * .9, screen.get_height() / 21.6, screen.get_height() / 21.6, "R'", (128, 128, 128), (0, 128, 128), cube.Rp)
    btn_f = Button(screen, 190, screen.get_height() * .9, screen.get_height() / 21.6, screen.get_height() / 21.6, "F", (128, 128, 128), (0, 128, 128), cube.F)
    btn_fp = Button(screen, 250, screen.get_height() * .9, screen.get_height() / 21.6, screen.get_height() / 21.6, "F'", (128, 128, 128), (0, 128, 128), cube.Fp)
    btn_s = Button(screen, 310, screen.get_height() * .9, screen.get_height() / 21.6, screen.get_height() / 21.6, "S", (128, 128, 128), (0, 128, 128), cube.S)
    btn_sp = Button(screen, 370, screen.get_height() * .9, screen.get_height() / 21.6, screen.get_height() / 21.6, "S'", (128, 128, 128), (0, 128, 128), cube.Sp)
    btn_b = Button(screen, 430, screen.get_height() * .9, screen.get_height() / 21.6, screen.get_height() / 21.6, "B", (128, 128, 128), (0, 128, 128), cube.B)
    btn_bp = Button(screen, 490, screen.get_height() * .9, screen.get_height() / 21.6, screen.get_height() / 21.6, "B'", (128, 128, 128), (0, 128, 128), cube.Bp)

    buttons = [btn_u, btn_up, btn_e, btn_ep, btn_d, btn_dp, btn_l, btn_lp, btn_m, btn_mp, btn_r, btn_rp, btn_f, btn_fp, btn_s, btn_sp, btn_b, btn_bp]

    screen.fill(screen.get_at((0, 0)))
    cube.draw_cube(screen)

    return buttons