class univariate():
        def qualQuan(dataset):
            qual=[]
            quan=[]
            for columnname in dataset.columns:
                    print(columnname)
                    if (dataset[columnname].dtype=='O'):
                        #print("qual",columns)
                        qual.append( columnname)
                    
                    else:
                        #print("quan",columns)
                        quan.append(columnname)
            return qual,quan