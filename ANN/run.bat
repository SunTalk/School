@echo off

cls
echo.
echo A2 : Two-neuron perceptron, dataset 2, two components
pause
py perceptronLearning.py 2N2C

echo A1 : Two-neuron perceptron, dataset 1
pause
py perceptronLearning.py 2N2C 1000

echo A3 : Two-neuron perceptron, dataset 2, three components
pause
py perceptronLearning.py 2N 1000

echo B2 : Four-neuron perceptron, dataset 2, two components
pause
py perceptronLearning.py 4N2C

echo B1 : Four-neuron perceptron, dataset 1
pause
py perceptronLearning.py 4N2C 1000

echo B3 : Four-neuron perceptron, dataset 2, three components
pause
py perceptronLearning.py 4N 1000

