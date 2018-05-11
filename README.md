# colour_detect-Ankur
Choose the best looking text color (Black or White) for a given set of color backgrounds. *The challenge was originally posted by Jabrils (see credits below)

The whole project is based on a neural network model. Initially the model was created with condition given below (which can be further change if required):-

Input Nodes = 3(R,G,B values)

Output Nodes = 2(Black, White)

Hidden Nodes = 3(Change as per requirement.)

The data set for this project was created by me. To create the dataset i have used pygame interface and python CSV module to write the dataset according to my need*.

The given RGB values were feeded to the neural network. Then the learned neural network, gives a possibility of whether a black or a white color text suits the most for our given background selection. The possibility is given with a floating point number (values in range 0-1), inside a list (Python). For example - if value determined for black color was 0.923, it means that the possibility of the best looking text color to be black is 92.3%. This in itself is a good result.
The Neural network has used sigmoid function as an activation function (which could be changed to ReLu, if needed, but i prefer sigmoid for now.). Learning is done with the help of back propagation method itself.

As of now with the current dataset consist of 153 elements and for the given test dataset (Both self-made). The model is giving an accuracy of 0.93(93%, on test dataset). This is good. But there is a need for further improvement, which i have describe in the end.

*Creation of Dataset:-*
Train Dataset
So the entire test, train dataset was created with the help of *data_create.py*. We have only to specify the name for our CSV file. The interface then pops up. And for selection of a set which suits the most. The set is actually a rectangle box (filled with a color), and a text displayed over it. There are two rectangle boxes, one with white color text (_TEXT 2_) and other with black (_TEXT 1_). You have to choose the one which suits the most, and then click on it with the help of mouse. After that the background color changes. And it keeps on happening for multiple times.
Test Dataset-
Same procedure is followed with only change in the name of file. 
*Green Button:-*
The green button on the Dataset window is used to update the color manually. so a user can change the color of rectangle as much times he desire.



*How it works:-*
Now to see the program in action. Fire up the file *model_complete.py*. It first executes the training of neural network multiple times. With each time a different weight value. When there is a condition of maximum accuracy the program gets to the next phase. A window pops up. it asks for choosing a best suitable color. With a black button** over one of the rectangle box.
*Black Button:-*
The black button displays the current situation of our neural net (Prediction). Which means it is the decision of our neural network. The color of text which it thinks most suitable with the given background. And it keeps on changing given the person hits the rectangle or the green button.


*Things to be improved upon:-*
1. First and foremost, the code should be cleaner. As i really wanted to upload these file quickly, i haven’t really looked on the code in much detail. As it gets my job done. But there should be more readability with the code. And i will do it for the mean time.
2. The Sigmoid function should be changed with something much better like ReLu.
3. To get more accurate results following things should be looked upon:-
    i) Dataset is not up to the mark, and more emphasis should be provided to it.
    ii) Proper learning rate and epoch value should be selected, with more learning on the dataset.
    iii) There are a lot of instances in which the network determines the value incorrectly. Proper supervision should be done to find out          the real issue behind it.
4. Interface, Program can be made into a more intact program.
5. *More errors which i haven’t found yet.*




Thanks to Jbrils for putting up this challenge. i have learned a lot by just working on it. Check out his videos they are really nice and entertaining.
Challenge video - https://www.youtube.com/watch?v=I74ymkoNTnw
