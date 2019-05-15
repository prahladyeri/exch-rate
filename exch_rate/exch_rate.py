##
# exch-rate is a simple tool to fetch currency exchange rates and convert them.
#
# @author Prahlad Yeri<prahladyeri@yahoo.com>
# @license MIT
#
import requests
import json
import argparse

__version__ = "0.2"

def main():
	parser = argparse.ArgumentParser(prog='exch-rate', usage='exch-rate [-h] from to \n(example: exch-rate usd inr)', description="Call with from and to exchange symbols. Example: exch-rate USD INR")
	parser.add_argument("from", help="From currency")
	parser.add_argument("to", help="To currency")
	args = parser.parse_args()
	#
	url = "https://free.currencyconverterapi.com/api/v5/convert?q=%s_%s&compact=y&apiKey=d08e67b83d5caf3c3887"
	#fmcurr, tocurr = "BTC", "usd"
	fmcurr, tocurr = getattr(args, 'from'), args.to
	url = url % (fmcurr, tocurr)
	sess = requests.session()
	res = sess.request("GET", url)
	obj = json.loads(res.text)
	if len(obj.keys()) != 0:
		#vald = obj["%s_%s" % (fmcurr, tocurr)]
		#print('obj', obj)
		vald = obj[next(iter(obj))]
		print(vald['val'])
	else:
		print("No values found, please check symbols.")

if __name__ == "__main__":
	main()