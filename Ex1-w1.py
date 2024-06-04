def exercise1(tp,fp,fn):
    if type(tp) == int:
        print("tp must be int")
    elif type(fp)==int:
        print("tp must be int")
    elif type(fn)==int:
        print("tf must be int")
    else:
        precision = tp/(tp+fp)
        recall = tp/(tp+fn)
        return (precision * recall)/(precision + recall)

exercise1 ( tp =2 , fp ='a', fn =4)
