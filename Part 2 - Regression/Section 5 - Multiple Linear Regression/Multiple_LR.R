#Importing Dataset
dataset = read.csv('50_Startups.csv')

#Encoding Categorical values
dataset$State = factor(dataset$State,
                       levels = c('New York','California','Florida'),
                       labels = c(1,2,3))

#Spliting dataset to training sets and testing sets
library(caTools)
set.seed(123)
split = sample.split(dataset$Profit,SplitRatio=0.8)
training_set = subset(dataset,split == TRUE)
test_set = subset(dataset,split == FALSE)

#Fitting MLR to Training Set
regressor = lm(formula = Profit ~ .,data = training_set)

#Predicting the Test set results
y_pred = predict(regressor, newdata = test_set)

#Building the optimal model using Backward elimination
regressor_opt = lm(formula = Profit ~ R.D.Spend + Administration + Marketing.Spend + State,data = dataset)
summary(regressor_opt)

regressor_opt = lm(formula = Profit ~ R.D.Spend + Administration + Marketing.Spend ,data = dataset)
summary(regressor_opt)

regressor_opt = lm(formula = Profit ~ R.D.Spend  + Marketing.Spend ,data = dataset)
summary(regressor_opt)

regressor_opt = lm(formula = Profit ~ R.D.Spend ,data = dataset)
summary(regressor_opt)

