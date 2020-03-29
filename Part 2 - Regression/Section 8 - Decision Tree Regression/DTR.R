#Decision Tree Regression

#Importing Dataset
dataset = read.csv('Position_Salaries.csv')
dataset = dataset[2:3]



#Fitting DTR  to the dataset
library(rpart)
regressor = rpart(formula = Salary ~ .,
                  data = dataset,
                  control = rpart.control(minsplit = 1))

#Predicting a new result with DTR 
y_pred  = predict(regressor, data.frame(Level = 6.5))


#Visulaizing the DTR results with higher resolution
library(ggplot2)
x_grid = seq(min(dataset$Level),max(dataset$Level),0.01)
ggplot() +
  geom_point(aes(x = dataset$Level , y = dataset$Salary),
             color = 'red') +
  geom_line(aes(x = x_grid  , y = predict(regressor, newdata = data.frame(Level = x_grid))),
            color = 'blue') +
  ggtitle('Truth or Bluff (DTR)') +
  xlab('Level') +
  ylab('Salary')

