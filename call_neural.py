'''This demonstrate how to call the neural netowork.'''
from neural import neural_net
import numpy as np

'''Initialize the network.'''

input_node = 3
hidden_node = 3
output_node = 2
learning_rate = 0.3

#object intilization
n = neural_net(input_node,hidden_node,output_node,learning_rate)


f = open('data1.csv','r')
f_list = f.readlines()
f.close()

for record in f_list:
    all_val = record.split(',')
    inputs = (np.asfarray(all_val[1:])/255.0*0.99)+0.01
    targets = np.zeros(output_node) +0.01
        
    targets[int(all_val[0])] = 0.99
    n.training(inputs , targets)
    
    pass



'''Testing of the neural network'''
score = []#score list , 0- incorrect, 1 - correct

t = open('test.csv','r')
t_list = t.readlines()
t.close()

for record in t_list:
    all_val = record.split(',')
    #print(all_val)
    correct_label = int(all_val[0])
    #print('correct label -',correct_label)
    inputs = (np.asfarray(all_val[1:])/255.0*0.99)+0.01
    outputs = n.query(inputs)
    
    label = np.argmax(outputs)
    #print('label -',label)
    if label == correct_label:
        score.append(1)
    else:
        score.append(0)
        pass
    pass

print(score)
n_val = np.asfarray(score)
num = n_val.sum()/n_val.size
print('performence - ',num)#performence/accuracy