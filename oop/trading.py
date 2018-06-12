# Enter your code here. Read input from STDIN. Print output to STDOUT


import OrderedDict        

class MostTraded(object):
    
    d=dict()

    def addTrade(self, ticker, volume):
        
        if d.get(ticker)  is not None:
            d(ticker)+=volume
        else:
            d(ticker)=volume
            
        
		
	def printMostTraded(mostTradedN):
        ab = OrderedDict(sorted(d.items(), key = lambda x:x[1],  reverse=True)

                
        for i, (key, value) in enumerate(a.iteritems()):
            if i==mostTradedN:
                return
        else:
            print(ticker, volume)

#	pass
		
if __name__ == "__main__":
    mostTraded = MostTraded()
	
	m.addTrade("IBM", 1000);
	m.addTrade("AAPL", 500);
	m.addTrade("NFLX", 1000);
	m.addTrade("AMZN", 700);
	m.addTrade("AAPL", 600);

	m.printMostTraded(2);
	
	# AAPL 1100
	# IBM  1000