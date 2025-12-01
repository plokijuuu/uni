def gen_time(start, stop, step):
    h, m, s = start
    end_h, end_m, end_s = stop
    step_h, step_m, step_s = step

    def to_seconds(t):
        return t[0] * 3600 + t[1] * 60 + t[2]

    current = to_seconds(start)
    end = to_seconds(stop)
    step_sec = to_seconds(step)

    while current <= end:
        ch = current // 3600
        cm = (current % 3600) // 60
        cs = current % 60
        yield (ch, cm, cs)
        current += step_sec

for time in gen_time((8, 10, 0), (10, 50, 15), (0, 15, 12)):
    print(time)
