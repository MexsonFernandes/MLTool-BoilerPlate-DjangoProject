
#-Step 1.Integration with web app--------------------------------
args <- commandArgs(trailingOnly=TRUE)
setwd(args[1])

#--------------------------------------------------------------
# Step 2: Variable Declaration
#--------------------------------------------------------------
cat("\nStep 2: Variable Declaration")
modelFileName <- "randomForest-Model.RData"
testFileName = args[2]


#--------------------------------------------------------------
# Step 3: Model Loading
#--------------------------------------------------------------
cat("\nStep 3: Model Loading")
load(modelFileName)



#--------------------------------------------------------------
# Step 4: Data Loading
#--------------------------------------------------------------
cat("\nStep 4: Data Loading")
newTestDataset <- read.csv(testFileName)    # Read the datafile
head(newTestDataset)


#--------------------------------------------------------------
# Step 5: Prediction (Testing)
#--------------------------------------------------------------
cat("\nStep 5: Prediction using -> ", modelName)
library(randomForest)
NewPredicted <- predict(model, newTestDataset)
head(NewPredicted)


#--------------------------------------------------------------
# Step 6: Saving Results
#--------------------------------------------------------------
cat("\nStep 6: Saving Results")

  setwd(args[3])
write.csv(data.frame(newTestDataset,NewPredicted), file=paste("predict_select.csv",sep=''), row.names=FALSE)


cat("\nDone")

#--------------------------------------------------------------
#                           END 
#--------------------------------------------------------------

