from . import timework as tw

import time
from random import randint

def test_no_split():
    """
    output example:
      [TIMEWORK] Start:  Mon Feb  8 04:11:38 2021
      [TIMEWORK] Stop:   00:00:01.438
      [TIMEWORK] Finish: Mon Feb  8 04:11:41 2021
    """
    with tw.Stopwatch() as s:
        assert -.1 < s._initial - time.time() < .1
        time.sleep(.3)
        assert s._running is True
        s.pause()
        assert s._running is False
        time.sleep(.4)
        assert s._running is False
        s.resume()
        assert s._running is True
        time.sleep(.5)
        time.sleep(.6)
        assert s._running is True
        s.stop()
        assert s._running is False
        time.sleep(.7)


def test_split():
    """
    output example:
      [TIMEWORK] Start:  Mon Feb  8 04:03:13 2021
      [TIMEWORK] Split:  00:00:00.804 | 00:00:00.804
      [TIMEWORK] Split:  00:00:01.411 | 00:00:00.606
      [TIMEWORK] Stop:   00:00:02.114 | 00:00:00.703
      [TIMEWORK] Finish: Mon Feb  8 04:03:16 2021
    """
    with tw.Stopwatch() as s:
        assert s._running is True
        time.sleep(.3)
        s.pause()
        assert s._running is False
        time.sleep(.4)
        s.resume()
        assert s._running is True
        time.sleep(.5)
        s.split()
        assert s._start_at != s._initial
        time.sleep(.6)
        s.split()
        assert s._start_at - s._initial > .6
        time.sleep(.7)
        assert s._running is True