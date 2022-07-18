from coldtype import *
from coldtype.fx.skia import phototype
import coldtype.fx.shapes as shapes

imbue_f = Font.Cacheable("/Users/jesi/fonts/Imbue/Imbue.ttf")
ancho_f = Font.Cacheable("/Users/jesi/fonts/ANCHO/Ancho_variable/AnchoGX.ttf")
kyviv_f = Font.Cacheable(
    "/Users/jesi/fonts/KyivType2020-14-12/KyivType-VariableGX/KyivTypeSans-VarGX.ttf"
)
tourney_f = Font.Cacheable("/Users/jesi/fonts/Tourney/Tourney.ttf")
trispace_f = Font.Cacheable("/Users/jesi/fonts/Trispace/Trispace.ttf")

tl = Timeline(60)

h = random()


# @animation((800, 300), timeline=tl, bg=hsl(h, 0.5, 0.8), render_bg=1)
def rafa(f):
    color = hsl(h, 0.5, 0.8)
    return PS(
        [
            StSt(
                "vamos rafa",
                ancho_f,
                80,
                ro=1,
                rotate=-10 + f.e("eeio", loops=1) * 30,
                tu=-100 + f.e("eeio", loops=2) * 500,
                wght=f.e("qeio", loops=2),
            )
            .align(f.a.r)
            .f(hsl(h, 0.5, 0.5))
            .layer(
                lambda p: p.outline(10)
                .removeOverlap()
                .castshadow(-45, 30)
                .f(None)
                .s(color.darker(0.5))
                .sw(4),
                lambda ps: ps.s(color.lighter(0.3)).sw(4),
            )
        ]
    )


# @animation((800, 800), timeline=tl, bg=hsl(h, 0.5, 0.8), render_bg=1)
def quieres(f):
    color = hsl(h, 0.5, 0.8)
    return (
        PS(
            [
                StSt(
                    "Quieres un",
                    imbue_f,
                    80,
                    wght=0.5,
                    rotate=-40 + f.e("eeio", loops=1) * 60,
                )
                .fssw(color.darker(0.3), color.darker(0.6), 2)
                .align(f.a.r),
                StSt("dato", ancho_f, 80, wght=0.8, tu=f.e("seio", loops=2) * 1000)
                .align(f.a.r)
                .f(color.darker(0.35))
                .layer(lambda p: p.castshadow(-90, f.e("eeio", loops=1) * 100)),
                StSt("de pequeño\nno eras tan", imbue_f, 80, wght=0.7)
                .f(color.darker(0.6))
                .align(f.a.r)
                .translate(x=-100 + f.e("qeio", loops=1) * 300, y=0),
                StSt("pesado", kyviv_f, 120, wght=0.8, ro=1)
                .pen()
                .fssw(color.darker(0.6), color.darker(0.9), sw=12)
                .layer(
                    lambda p: p.outline(10)
                    .removeOverlap()
                    .castshadow(-45, 10 + f.e("qeio", loops=2) * 30)
                    .f(None)
                    .s(color.darker(0.5))
                    .sw(4),
                    lambda ps: ps.s(color.lighter(0.3)).sw(4),
                )
                # .distribute_on_path(sine)
                .align(f.a.r).translate(0, -80)
                # .ch(phototype(f.a.r, blur=4, cut=130, cutw=40, fill=hsl(0.45, 1, 0.6))),
            ]
        )
        .reverse_pens()
        .distribute(v=1)
        .track(-30, v=1)
        .translate(x=0, y=-140)
        # .align(f.a.r, th=1, tv=1)
    )


def webazo(f):
    color = hsl(h, 0.5, 0.8)
    return PS(
        [
            P().rect(f.a.r).f(color),
            StSt(
                "balls\nand\ncock",
                ancho_f,
                60,
                wght=f.e("qeio", loops=2),
                ro=1,
                tu=1300 - f.e("ceio", loops=1) * 2000,
                rotate=f.e("ceio", loops=1) * 180,
            ).align(f.a.r)
            # .understroke(color.darker(0.6), sw=10)
            .fssw(color.darker(0.2), color.darker(0.6), 10).scale(1.5, 1.5)
            # .ch(phototype(f.a.r, blur=2, cut=120, cutw=60)),
        ]
    )


@animation((800, 800), timeline=tl)
def trispace(f):
    circle = (
        P()
        .oval(f.a.r.inset(150))
        .reverse()
        .f(rgb255(234, 100, 100).darker(0.4))
        .align(f.a.r)
    )
    return PS(
        [
            P().rect(f.a.r).f(rgb255(234, 100, 100)),
            circle,
            StSt(
                "Thanks so much!",
                trispace_f,
                80,
                wght=1,
                ro=1,
                # tu=1300 - f.e("ceio", loops=1) * 2000,
                tu=0,
                # rotate=-40 + f.adj(-g.i * 4).e("eeio", loops=2) * 80,
                fit=circle.length(),
            )
            .understroke(sw=10)
            .f(1)
            .distribute_on_path(circle, offset=f.e("ceio", loops=1) * 400)
            # .rotate(f.e("ceio", loops=1) * 720, point=f.a.r.pc)
            .ch(phototype(f.a.r, blur=2, cut=120, cutw=60)),
        ]
    )


# @renderable((800, 800))
# def trispace(r):
#     return PS(
#         [
#             (P().rect(r).f(rgb(1, 0.7, 0.7))),
#             StSt(
#                 "Rosanita",
#                 trispace_f,
#                 80,
#                 wght=0.9,
#                 tu=700,
#                 r=1,
#                 ro=1,
#                 rotate=45,
#             )
#             .rotate(-45)
#             .fssw(rgb255(250, 108, 100), rgb255(250, 108, 100).darker(0.4), 3)
#             .scale(1.5, scaleY=1.6)
#             .align(r, th=1, tv=1),
#         ]
#     )


# @renderable((800, 800))
def thumbnail_blog(r):
    return PS(
        [
            (P().rect(r).f(hsl(0, 0, 0.14))),
            StSt(
                "COLDTYPE",
                Font.ColdtypeObviously(),
                200,
                wdth=10,
                tu=-100,
                r=1,
                rotate=10,
            )
            .rotate(45, r.pc)
            .align(r, th=True, tv=True)
            .f(1)
            .understroke(sw=20)
            .ch(phototype(r, blur=4, cut=130, cutw=20, fill=hsl(0.45, 1, 0.6))),
        ]
    )


# @animation((1000, 400), timeline=tl)
def imbue(f: Frame):
    e = f.a.progress(f.i, loops=1, easefn="eeio").e

    return (
        PS(
            [
                (P().rect(f.a.r).f(hsl(0.40 - e / 20, 1, 0.5))),
                StSt(
                    "Imbue",
                    imbue_f,
                    300 + e * 10,
                    wght=e * 10,
                    tu=-100 + e * 500,
                    ro=1,
                )
                .pen()
                .f(hsl(0.4 - e / 20, 1, 0.3))
                .layer(
                    lambda p: p.castshadow(-90, e * 100).f(hsl(0.4, 0.7, 0.2)),
                    lambda p: p.s(hsl(0.4, 1, 0.1)).sw(1 + e * 5),
                )
                .align(f.a.r, x="mdx", y="mdy", th=True, tv=True),
            ]
        ),
    )


# @animation((1000, 400), timeline=tl)
def ancho(f: Frame):
    e = f.a.progress(f.i, loops=1, easefn="eeio").e

    return (
        PS(
            [
                (P().rect(f.a.r).f(hsl(0.15 - e / 30, 0.9, 0.8))),
                StSt(
                    "ANCHO",
                    ancho_f,
                    150,
                    wght=f.e("qeio", loops=2),
                    rotate=f.e("qeio", loops=4) * 180,
                    tu=1000 - f.e("seio", loops=1) * 1500,
                    ro=1,
                    r=1,
                )
                .align(f.a.r)
                .understroke()
                .f(hsl(0.05 + 0.05 * f.e("qeio", loops=1), 1, 0.5))
                .layer(
                    # lambda p: p.castshadow(-90, e * 100).f(hsl(0.1, 0.7, 0.2)),
                    lambda p: p.s(hsl(0.1, 1, 0.1)).sw(1 + e * 5),
                )
                .align(f.a.r, x="mdx", y="mdy", th=True, tv=True),
            ]
        ),
    )


# @animation((1000, 400), timeline=tl)
def Kyviv(f: Frame):
    e = f.a.progress(f.i, loops=1, easefn="seio").e

    return (
        PS(
            [
                (P().rect(f.a.r).f(hsl(0.65 - e / 20, 0.9, 0.4))),
                StSt(
                    "KYVIV",
                    kyviv_f,
                    150,
                    wght=10 * f.e("eeio", loops=2),
                    tu=500 - f.e("seio", loops=2) * 500,
                    rotate=f.e("seio", loops=1) * 360,
                    ro=1,
                    r=1,
                )
                .align(f.a.r)
                .understroke()
                .f(hsl(0.15 + 0.05 * f.e("qeio", loops=1), 1, 0.8))
                .layer(
                    lambda p: p.s(hsl(0.64, 1, 0.2)).sw(8),
                )
                .align(f.a.r, x="mdx", y="mdy", th=True, tv=True),
            ]
        ),
    )


# @animation((1000, 400), timeline=tl)
def tourney(f: Frame):
    e = f.a.progress(f.i, loops=1, easefn="seio").e

    c1 = hsl(0.45, 1, 0.1 + f.e("eeio", loops=2) * 0.1)
    c2 = hsl(0.50, 1, 0.1 + f.e("qeio", loops=2) * 0.12)
    return (
        PS(
            [
                (P().rect(f.a.r).f(Gradient.Horizontal(f.a.r, c1, c2))),
                StSt(
                    "TOURNEY",
                    tourney_f,
                    220,
                    wght=20,
                    tu=-40 - f.e("seio", loops=2) * 390,
                    rotate=-15 + f.e("seio", loops=2) * 45,
                    translate=f.e("seio") * 100,
                    ro=1,
                    r=0 if f.e("seio", loops=0.5) < 0.5 else 1,
                )
                .align(f.a.r)
                .understroke(sw=20)
                .f(1)
                .align(f.a.r, x="mdx", y="mdy", th=True, tv=True)
                .ch(phototype(f.a.r, blur=4, cut=130, cutw=40, fill=hsl(0.45, 1, 0.6))),
            ]
        ),
    )


def release(passes):
    FFMPEGExport(trispace, passes).gif().write()
