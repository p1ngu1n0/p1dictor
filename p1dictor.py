#!/usr/bin/python3

import itertools, string
import argparse
from progress.bar import Bar

def banner():
	print( "\n    ▄███████▄ ████████▄   ▄█   ▄████████     ███      ▄██████▄     ▄████████ ")
	print( "   ███    ███ ███   ▀███ ███  ███    ███ ▀█████████▄ ███    ███   ███    ███ ")
	print( "   ███    ███ ███    ███ ███▌ ███    █▀     ▀███▀▀██ ███    ███   ███    ███ ")
	print( "   ███    ███ ███    ███ ███▌ ███            ███   ▀ ███    ███  ▄███▄▄▄▄██▀ ")
	print( " ▀█████████▀  ███    ███ ███▌ ███            ███     ███    ███ ▀▀███▀▀▀▀▀   ")
	print( "   ███        ███    ███ ███  ███    █▄      ███     ███    ███ ▀███████████ ")
	print( "   ███        ███   ▄███ ███  ███    ███     ███     ███    ███   ███    ███ ")
	print( "  ▄████▀      ████████▀  █▀   ████████▀     ▄████▀    ▀██████▀    ███    ███ ")
	print( "                                                                  ███    ███ \n")



def main(nume, out, chars):

	nume = int(nume)
	charss = len(chars)
	total = charss**nume

	bar1 = Bar(' Generando:', max=total)

	for i in itertools.product(list(chars), repeat=nume):
		f =  open(out+".lst", "a")
		f.write(''.join(i)+"\n")
		bar1.next()
	bar1.finish()
	f.close()
	print("\n Generado completado "+out+".lst\n")


if __name__ == '__main__':
	__author__ = "p1ngu1n0"

	parser = argparse.ArgumentParser(description='p1dictor.py create by @_p1ngu1n0_')
	parser.add_argument('-n','--num', help='Numero de caracteres',required=True)
	parser.add_argument('-c','--char',help='Caracteres a usar', required=True)
	parser.add_argument('-o','--output',help='Nombre de salida', required=True)
	args = parser.parse_args()

	ar1 = args.num
	ar2 = args.output
	ar3 = args.char
	banner()
	main(ar1, ar2, ar3)




