import dill
'''
I'm going to iterate over every ticker and date
in the training data pickle and assign a 1 or 0
for FDA passes or failures

I'm going to write the tickers and dates to a plaintext file and tick them manually
'''    
data = dill.load(open("stock_price_training_slices.pkl", "r"))
scoresheet = open("score_sheet.txt", "w")
for datum in data:
    scoresheet.write(datum[0]+" "+datum[1]+" ?\n")
scoresheet.close()