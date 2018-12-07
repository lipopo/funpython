#-*- coding: utf8 -*-
import unittest
from funypy.a_paint import aPaint

class TestApaint(unittest.TestCase):
    def test_apaint(self):
        recode = aPaint.img2paint(
            "./template_img.png",
            100,
            100
        )
        print recode
        encode_code = aPaint.paint_encoder(
            recode, "abnkso12'"
        )
        print encode_code

        decode_code = aPaint.paint_decoder(
            encode_code,
            "abnkso12'"
        )
        print decode_code

if __name__ == "__main__":

    unittest.main()

