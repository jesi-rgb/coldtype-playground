from coldtype import *
from coldtype.warping import warp
from coldtype.fx.skia import phototype

wav = __sibling__("media/webos.wav")

midi = MidiTimeline(__sibling__("media/test.mid"), duration=240, bpm=120, fps=30)
imbue_f = Font.Cacheable("/Users/jesi/fonts/Imbue/Imbue.ttf")

ar = {
    "KD": [5, 10],
    "KD2": [5, 100],
    "CW": [15, 75],
    "HT": [10, 10],
    "RS": [5, 5],
    "SD": [5, 20],
    "TM": [5, 10],
    "CN": [2, 7],
    "OH": [10, 25],
    "CL": [2, 35],
}


@animation((1000, 400), timeline=midi, audio=wav)
def drummachine(f):
    drums = f.t
    # print(drums.notes)
    kick = drums.ki(53)
    second_kick = drums.ki(36)
    snare = drums.ki(40)
    hihat = drums.ki(42)
    conga = drums.ki(43)
    conga_low = drums.ki(41)
    open_hat = drums.ki(46)
    clave = drums.ki(37)

    style = Style(
        imbue_f,
        440,
        tu=open_hat.adsr(ar["OH"], r=(-50, 200)),
        wght=snare.adsr(ar["SD"], r=(0.01, 0.8)),
        # ro=1,
        # r=1,
    )

    pens = StSt(
        "DAMN",
        style,
    ).align(f.a.r)

    cne, cni = conga.adsr(ar["SD"], find=1)

    pens[cni % len(pens)].scale(1 - cne * 0.3)
    # if si % 2 == 0:  # every other conga hit
    # pens[0].translate(-20 * se, 0)
    # pens[1].translate(30 * se, 0)
    # pens[0].rotate(se * 10)
    # else:
    #     pens[2].translate(150 * se, 0)
    #     pens[3].translate(-150 * se, 0)

    sde, sdi = snare.adsr(ar["SD"], find=1)

    he, hi = hihat.adsr(ar["HT"], find=True)
    # pens[hi % len(pens)].translate(0, 40 * he)

    ohe, ohi = open_hat.adsr(ar["OH"], find=True)
    # pens.translate(0, -50 * ohe)
    # pens.scale(1 - ohe * 0.3)

    cle, cli = clave.adsr(ar["CL"], find=True)
    # print(cli, cli // 6 % len(pens))
    pens[(cli // 6 % len(pens))].scale(1 + cle * 0.8, 1)

    cngle, cngli = conga_low.adsr(ar["CL"], find=True)
    pens[(cngli // 5 % len(pens))].rotate(cngle * 10)
    pens[(cni % len(pens))].rotate(cne * -30)

    ke, ki = kick.adsr(ar["KD"], find=True)
    pens.scale(1, 1 - ke * 0.2)

    ske, ski = second_kick.adsr(ar["KD2"], find=True)

    return PS(
        [
            P(f.a.r).f(rgb(0.1, 0.1, 0.1)),
            pens.f(rgb(0.5, 0.5, 0.5)),
            pens[ski // 2 % len(pens)].f(rgb(0.4, 0.4, 0.1)),
        ]
    )


def release(passes):
    FFMPEGExport(drummachine, passes).h264().write()
