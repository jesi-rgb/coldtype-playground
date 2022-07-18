from coldtype import *

# from coldtype.warping import warp
from coldtype.fx.skia import phototype

wav = __sibling__("media/3onE_audio.wav")

midi = MidiTimeline(__sibling__("media/3onE_midi.mid"), duration=240, bpm=120, fps=30)
ancho_f = Font.Cacheable("/Users/jesi/fonts/ANCHO/Ancho_variable/AnchoGX.ttf")


# @animation((1280, 720), timeline=midi, audio=wav)
def three_on_e(f):
    melody = f.t
    melody_ch = melody.ki(64)
    me, mi = melody_ch.adsr([1, 40], find=1)
    me_a, mi_a = melody_ch.adsr([1, 10], find=1)

    groupings = {0: 0, 1: slice(2, 4), 2: -1}
    # print(mi, me)

    style = Style(ancho_f, font_size=200, wght=0.5, opacity=0)

    three_on_e_pens = StSt("3 on e", style).align(f.a.r).f(rgb(0, 0, 0, 0))
    a_pen = StSt("A", style).align(f.a.r).f(rgb(0, 0, 0, 0))

    print(mi % 7)
    if mi % 7 == 0 or mi % 7 == 4:  # 3
        three_on_e_pens[mi // 3 % len(three_on_e_pens)].f(rgb(0.5, 0.5, 0.5, me))
    elif mi % 7 == 1 or mi % 7 == 5:  # on
        three_on_e_pens[2].f(rgb(0.5, 0.5, 0.5, me))
        three_on_e_pens[3].f(rgb(0.5, 0.5, 0.5, me))

    elif mi % 7 == 2 or mi % 7 == 6:  # e
        three_on_e_pens[-1].f(rgb(0.5, 0.5, 0.5, me))

    elif mi % 7 == 4:
        a_pen[0].f(rgb(0.5, 0.5, 0.5, me_a))

    return PS([P(f.a.r).f(rgb(0.2, 0.2, 0.2)), three_on_e_pens, a_pen])


@animation((1280, 720), timeline=midi, audio=wav)
def three_on_e(f):
    r = Rect(1280, 720).inset(100, 80).align(f.a.r)

    melody = f.t
    melody_ch = melody.ki(64)
    me, mi = melody_ch.adsr([1, 40], find=1)
    me_a, mi_a = melody_ch.adsr([1, 10], find=1)

    style = Style(ancho_f, font_size=600, wght=0.5, opacity=0)
    # print(f.a.r)

    three_on_e = {
        0: StSt("3", style).f(0.4, 0).align(f.a.r),
        1: StSt("on", style).f(0.4, 0).align(f.a.r),
        2: StSt("E", style).f(0.4, 0).align(f.a.r),
        3: StSt("A", style).f(0.4, 0).align(f.a.r),
    }

    if mi % 7 == 0 or mi % 7 == 4:  # 3
        three_on_e[0].f(rgb(0.5, 0.5, 0.5, me))
    elif mi % 7 == 1 or mi % 7 == 5:  # on
        three_on_e[1].f(rgb(0.5, 0.5, 0.5, me))
    elif mi % 7 == 2 or mi % 7 == 6:  # e
        three_on_e[2].f(rgb(0.5, 0.5, 0.5, me))
    elif mi % 7 == 3:
        three_on_e[3].f(rgb(0.5, 0.5, 0.5, me_a))

    return PS(
        [
            P(f.a.r).f(rgb(0.2, 0.2, 0.2)),
            three_on_e.values(),
        ]
    )


def release(passes):
    FFMPEGExport(three_on_e, passes).h264().write()
