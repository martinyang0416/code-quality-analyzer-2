import sys
import re
from sympy import expand, sympify, SympifyError

def preprocess(s):
    s = re.sub(r'([a-z])\s*\^\s*(\d)', r'\1**\2', s)
    s = s.replace(' ', '*')
    s = re.sub(r'(\))([a-z0-9(])', r'\1*\2', s)
    s = re.sub(r'([a-z])([a-z0-9(])', r'\1*\2', s)
    s = re.sub(r'(\d)([a-z(])', r'\1*\2', s)
    return s

def process_block(block):
    if not block:
        return
    correct_line = block[0]
    processed_correct = preprocess(correct_line)
    try:
        correct_expr = expa