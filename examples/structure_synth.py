import surrealist as sr

sounds_dir = "~/Desktop/my_samples/"
out_dir = "~/Desktop/"

b = sr.EventBuffer()


def r1(i: int = 0, s: sr.State = sr.State()) -> None:
    if i >= 60:
        return

    s = s.length("*0.98").stutter("+6").speed("-0.08")
    b.append(sr.Event("bd", s))

    s = s.timestamp("+0.04")
    b.append(sr.Event("sn", s))

    s = s.timestamp("+0.04")
    r1(i + 1, s)


def main():
    s = sr.State().length("1.5").amp("0.9")
    r1(0, s)

    s = sr.State().timestamp("2.2").length("0.8").speed("10").stutter("10").distort("0.8").amp("0.4")
    r1(10, s)

    s = sr.State().timestamp("2.5").length("0.5")
    r1(10, s)

    s = sr.State().timestamp("5.0").length("1.1").amp("0.8")
    r1(30, s)

    s = sr.State().timestamp("5.2").length("0.8").distort("0.5").amp("0.8")
    r1(20, s)

    s = sr.State().timestamp("5.8").length("2.0").speed("12").stutter("30").distort("0.2").amp("0.4")
    r1(20, s)

    r = b.render(sounds_dir)
    r.write(out_dir)
    r.play()


if __name__ == "__main__":
    main()
