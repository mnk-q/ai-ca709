from functools import reduce 
import pandas as pd 
import pprint 
class Classifier(): 
    data = None 
    class_attr = None 
    priori = {} 
    cp = {} 
    hypothesis = None 
    def __init__(self,filename=None, class_attr=None ): 
        self.data = pd.read_csv(filename, sep=',', header =(0)) 
        self.class_attr = class_attr 
    def calculate_priori(self): 
        class_values = list(set(self.data[self.class_attr])) 
        class_data = list(self.data[self.class_attr]) 
        for i in class_values: 
            self.priori[i] = class_data.count(i)/float(len(class_data)) 
        print ("Priori Values: ", self.priori) 
    def get_cp(self, attr, attr_type, class_value): 
        data_attr = list(self.data[attr]) 
        class_data = list(self.data[self.class_attr]) 
        total =1 
        for i in range(0, len(data_attr)): 
            if class_data[i] == class_value and data_attr[i] == attr_type: 
                total+=1 
        return total/float(class_data.count(class_value)) 
    def calculate_conditional_probabilities(self, hypothesis): 
        for i in self.priori: 
            self.cp[i] = {} 
            for j in hypothesis: 
                self.cp[i].update({ hypothesis[j]: self.get_cp(j, hypothesis[j], i)})
        print ("\nCalculated Conditional Probabilities: \n") 
        pprint.pprint(self.cp) 
    def classify(self): 
        print ("Result: ") 
        for i in self.cp: 
            print (i, " ==> ", reduce(lambda x, y: x*y, self.cp[i].values())*self.priori[i]) 
if __name__ == "__main__": 
    c = Classifier(filename="./weather.csv", class_attr="play" ) 
    c.calculate_priori() 
    c.hypothesis = {"outlook":'rainy', "temperature":"mild", "humidity":'normal' , "windy":'t'} 
    c.calculate_conditional_probabilities(c.hypothesis) 
    c.classify() 
