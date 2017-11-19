# FDA-Decision-Stock-Predictor
This is my capstone project for [the Data Incubator Fellowship](https://www.thedataincubator.com/fellowship.html). 
My goal is to take this project from initial concept to a usable application. 
### So Far:
1. I have found and scraped several investor news sites for past and upcoming FDA PDUFA (Prescription drug user fee act) action dates
1. I have munged the FDA announcement dates and joined them to stock price time-series for the relevant companies
1. I have sliced the relevant data into 120-day long preceding and following periods for data annotation and model training
1. I have annotated the data
1. I have calculated and selected important features from my training data
1. I have selected and trained a classification model (Support Vector Classifier)
1. I have cross validated the model, and verified it preforms better than random or majority case guessing
1. I have made a basic visualizaton showing how the model can trade better than a lay person
### Upcoming:
* Make a server (new repo) to constantly monitor the market and make trade decisions
* Learn webapp development the hard way
* Make a real project with a real repository on GitHub so I have something to demonstrate my skills beyond the lackluster scripts I wrote in graduate school
