#!/usr/bin/python

estado = None


class suma:

    def parse(self, request, rest):
        try:
            listaNums = rest.split('/')
            if len(listaNums) != 2:
                return None
            num1 = int(listaNums[0])
            num2 = int(listaNums[1])
            operandos = (num1, num2)
        except ValueError:
            return None
        return operandos

    def process(self, parsedRequest):
        if not parsedRequest:
            return("400 Bad Request",
                   "<html><body><h1>Error: /suma/numero1/numero2</h1>" +
                   "</body></html>")
        (num1, num2) = parsedRequest
        suma = num1 + num2
        return("200 OK",
               "<html><body><h1>" + str(num1) + " + " + str(num2) +
               " = " + str(suma) + "</h1>" +
               "</body></html>")
