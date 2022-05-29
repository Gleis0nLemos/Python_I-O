for i in xrange(6):
    with saved(cr):
        cr.rotate(2 * math.pi * i / 6)
        cr.rectangle(-25, -60, 50, 40)
        cr.stroke()