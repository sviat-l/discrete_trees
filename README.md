# Trees
This is our task for the laboratory work on Discrete math clasess.

There were two projects:
1. Compare MST algorithms
2. Decision Tree classifier

## Comparison of Kruskal and Prim's algorithms
   In the first project we had to write algorithms that draw the minimum cost spanning tree.
Then we runned each of them a couple of times and made plots time-(number of nodes) dependency. They can be found in [plots](plots).\
   In modules [kruskal.py](kruskal.py) and [prim.py](prim.py) there are implementions of the corresponding algorithms.
[create_graph.py](create_graph.py) contains functions that creates random graph with different changable parametrs.\
   If you want run comparison of the two algorithms, there are functions in [run_tests.py](run_tests.py) that can calculate average time proceding and plot graphs.\
Example of the plot results:


![plot7](https://user-images.githubusercontent.com/91615606/155042256-7276c580-ab30-46ea-bf71-7149c3e9631f.png)

 More description and analyze of the task you can find in [report.pdf](report.pdf)
 
 ##  Decision Tree classifier
 In the second task we had to implement Machine Learning algorithm, write a Decision classifier by ourselves. The goal was to create a model that predicts the value of a variable by learning simple decision rules inferred from the data features.\
 We trained our model using dataset and evaluated its performance basing on the test dataset. Tree is simple and useful instrument for that, it provedes a good aproximation (more than 90%).
 
 ![8188fc62-2642-4d83-b3f2-c3d2fb064576](https://user-images.githubusercontent.com/91615606/155042511-21955e3b-0cb7-4102-9da2-dfc377c2ef7a.png)

 More detailed information about that task is in jupyter notebook [DecisionTreeClassiffier.ipynb](DecisionTreeClassiffier.ipynb)
