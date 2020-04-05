#Random Forest Regression

#Importing Dataset
dataset = read.csv('Position_Salaries.csv')
dataset = dataset[2:3]



#Fitting RTR  to the dataset
library(randomForest)
set.seed(1234)
regressor = randomForest(x = dataset[1],
                         y = dataset$Salary,
                         ntree = 500)

#Predicting a new result with RTR 
y_pred  = predict(regressor, data.frame(Level = 6.5))


#Visulaizing the RTR results with higher resolution
library(ggplot2)
x_grid = seq(min(dataset$Level),max(dataset$Level),0.01)
ggplot() +
  geom_point(aes(x = dataset$Level , y = dataset$Salary),
             color = 'red') +
  geom_line(aes(x = x_grid  , y = predict(regressor, newdata = data.frame(Level = x_grid))),
            color = 'blue') +
  ggtitle('Truth or Bluff (RTR)') +
  xlab('Level') +
  ylab('Salary')

