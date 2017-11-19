# -*- coding: utf-8 -*-
class LineCallback(object):

    def __init__(self, callback):
        self.callback = callback

    def Pinverified(self, pin):
        self.callback("Klik Pin Kode '" + pin + "' to di mobile phone mu dalam 2 menit.")

    def QrUrl(self, url):
        self.callback("Masuk Line QRmu dengan handphone dalam 2 menit \n" + url)

    def default(self, str):
        self.callback(str)
