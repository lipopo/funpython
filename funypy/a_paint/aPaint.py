# -*- coding: utf8 -*-
import sys
import cv2
import numpy as np
import click
import random
from PIL import Image
from io import BytesIO

coders = "abcdefghijklmnopqestuvwxyz0123456789/?>.,<'\";:]}[{=+-_)(*&^%$#@!~`|\\"

def img2paint(img_path, col, row, img=None, cmin=0,cmax=100):
    if img is None:
        img = cv2.imread(img_path)
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY).astype(np.uint8)
    img_canny = cv2.Canny(img_gray, cmin, cmax)

    height, width = img_canny.shape

    b_height, b_width = (height // col, width // row)
    output_code = ""
    h_idx, w_idx = (height // b_height, width // b_width)

    for h in range(h_idx):
        for w in range(w_idx):
            cop = " "
            cop_img = img_canny[h*b_height:(h+1)*b_height,w*b_width:(w+1)*b_width]
            if np.sum(cop_img) > 0:
                cop = "."

            output_code += cop
        output_code += "\n"

    return output_code

def coder_generate(n_set):
    u_set = n_set
    while True:
        yield random.choice(u_set)

def paint_encoder(code, setter):
    coder_use = coders
    dot_gen = coder_generate(setter)
    for c in setter:
        coder_use = coder_use.replace(c,"")
    code_gen = coder_generate(coder_use)
    new_code = ""
    for c_idx,c in enumerate(code):
        if c == "\n":
            ucode = c
        elif c == ".":
            ucode = dot_gen.next()
        else:
            ucode = code_gen.next()
        new_code += ucode
    return new_code

def paint_decoder(code, setter):
    new_code = ""
    for c in code:
        if c == "\n":
            ucode = "\n"
        elif c in setter:
            ucode = "."
        else:
            ucode = " "
        new_code += ucode
    return new_code

@click.group()
def cli():
    pass


@cli.command("paint")
@click.option("-col", "col", help="ColNums", default=11)
@click.option("-row", "row", help="RowNums", default=11)
@click.option("--encode", "-E", is_flag=True)
@click.option("--secret", "-S", default="absfgs'")
@click.argument("img_path")
def run_img2paint(col, row, img_path, encode, secret):
    code = img2paint(img_path, col, row)
    if encode:
        code = paint_encoder(code, secret)
    click.echo(code)

@cli.command("decode-paint")
@click.option("--secret", "-S", default="absfgs'")
@click.argument("file", type=click.File("r"))
def decode_file(file, secret):
    code = file.read()
    decode_code = paint_decoder(code, secret)
    click.echo(decode_code)
