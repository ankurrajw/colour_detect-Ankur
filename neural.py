'''Neural Network:-
Neural Network Class is created'''
import numpy as np
import scipy.special


#define a class neural network with appropriate functions
class neural_net:
    
    #initialize the neural network
    def __init__(self, input_nodes , hidden_nodes, output_nodes , learning_rate):
        self.inodes = input_nodes
        self.hnodes = hidden_nodes
        self.onodes = output_nodes
        
        self.lr = learning_rate
        #weights input-hidden , hidden-output
        self.wih = np.random.normal(0.0 , pow(self.hnodes,-0.5) , (self.hnodes, self.inodes))
        self.who = np.random.normal(0.0, pow(self.onodes ,-0.5) , (self.onodes, self.hnodes))
        
        #RelU activation function defination
        self.act_fun = lambda x: scipy.special.expit(x)
        
        pass
    
    #trainning of the neural network
    def training(self, input_list, target_list ):
        
        inputs  =  np.array(input_list, ndmin = 2).T
        targets = np.array(target_list, ndmin = 2).T
        
        hidden_inputs = np.dot(self.wih , inputs)
        hidden_outputs = self.act_fun(hidden_inputs)
        #print(hidden_outputs)
        
        final_inputs = np.dot(self.who, hidden_outputs)
        final_outputs = self.act_fun(final_inputs)
        
        #erros - Simple error calculation(Desired - Actual)
        output_errors = targets - final_outputs
        hidden_errors = np.dot(self.who.T , output_errors)
        
        '''Gradient Descent- to update weights using backpropagation'''
        self.who += self.lr*np.dot((output_errors*final_outputs*(1.0 - final_outputs)), hidden_outputs.T)
        self.wih += self.lr*np.dot((hidden_errors*hidden_outputs*(1.0 - hidden_outputs)), inputs.T)

        pass
    
    #Query function to check the value for any colour
    def query(self ,input_list):
        #inputs array
        inputs = np.array(input_list,ndmin = 2).T
        
        hidden_inputs = np.dot(self.wih , inputs)
        hidden_outputs = self.act_fun(hidden_inputs)
        
        final_inputs = np.dot(self.who, hidden_outputs)
        final_outputs = self.act_fun(final_inputs)
        
        return final_outputs
        pass
    pass