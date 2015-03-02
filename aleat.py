#!/usr/bin/python

import random


class aleat:

    def parse(self, request, rest):
        return None

    def process(self, parsedRequest):
        url = str(random.randrange(161612316))
        return("200 OK",
               "<html><body><h1>URLs aleatorias</h1>" +
               "<a href='" + url + "'>Dame otra!</a>" +
               "</body></html>")
