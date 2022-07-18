from coldtype import *
from coldtype.warping import warp
from coldtype.fx.skia import phototype

wav = __sibling__("media/lyric_test.wav")

midi = MidiTimeline(__sibling__("media/lyric_test.mid"), duration=240, bpm=120, fps=30)
imbue_f = Font.Cacheable("/Users/jesi/fonts/Imbue/Imbue.ttf")


@animation((1000, 400), timeline=midi)
def drummachine(f):
    pens = StSt("Hola como estamos", font=imbue_f, font_size=200).align(f.a.r)
    return PS(
        [
            P(f.a.r).f(rgb(0.1, 0.1, 0.1)),
            pens.f(rgb(0.5, 0.5, 0.5, 0)),
        ]
    )
