credit-scoring-exercise
===========================

# Exercise 1

Once the model is activated, Portfolio A’s owner will evaluate its performance using only loans repayment information collected AFTER the model was activated. I am assuming that this is how the TEST set is collected.

The above evaluation criteria is not reliable because it introduces selection bias, as we would only know the repayment results of those clients whom the model has accepted. There could be credit-worthy clients that the model has rejected but there will be no way of knowing this result. This problem is also known as partial feedback.

I will assess the models based on validation set only, using Area Under the ROC curve as the evaluation metric for binary classification. Model 1 is the best model.

validation auc: model1=0.647, model2=0.638

Code: [ex1.ipynb](ex1.ipynb) 

# Exercise 2

Code: [ex2.ipynb](ex2.ipynb)
               
## Models
Tree-based methods; LightGBM is a boosting ensemble designed to reduce bias, whereas Random Forest is a bagging ensemble designed to reduce variance.

Advantages of tree-based methods: Cheap to build and make inference (cost grows with tree depth). Non-parametric: does not assume any probability distribution type. Robust to noise and redundant features because outliers are unlikely to be the split point. Unlike linear models and neural nets, we do not need to perform standardisation or attempt to map the features to a normal distribution.

Tune the following hyperparameters to avoid overfitting: minimum number of examples in leaf, number of features to consider for splitting, number of examples available to grow each tree. 

## Feature Engineering
Encode categorical variables with frequency encoding which is better for decision trees as compared to one-hot encoding. It is difficult for decision trees to look for a good split point where there are very few split points available (such as binary 0/1 in the case of one-hot encoding).

To ensure no leaks from the test set, frequencies are obtained only from the training set.

Feature crosses to create interaction terms for important features, which are obtained from the model (goodness of a split point, how much impurity is reduced). This helps to model non-linearities in feature space by combining two or more features together.

## Feature Selection
KS Test to test whether two samples are drawn from the distribution. Both samples are drawn from the training set (ensure no data leaks from the test set).

Drop features where p value is less than or equals level of significance alpha (10%). These features are dropped because they exhibit too much variance across different samples.

Drop 7 features={'Var77', 'Var82_Var83', 'Var130', 'Var9', 'Var83_Var7', 'Var29', 'Var30'}

## Evaluation
Stratified 5-fold cross validation is important because we have a class imbalance problem (positive class is present at 2% of training set, 1% of test set). K-folds allows all examples to be used for validation once and for training (k - 1) times. We reduce the risk of the result having a heavy dependency on the membership of the training and validation sets.

CV results
- LGBM best score=0.710, std=0.087
- Random Forest best score=0.715, std=0.072

(Important to indicate the standard deviation so that we can assess how the models will fare on unseen data)

Based on the validation results, RF seems to be the better model because it has a slightly higher score and smaller standard deviation. 

The test set shows that the LGBM Model is able to generalize slightly better than random forest.
auc_lgbm=0.635, auc_rf=0.615

## Notes
I tried a simple blend of the two models but the ensemble did not outperform the best single model which is LGBM. Adding more models (different machine learning methods) to the blend may improve its performance by reducing variance. All models learn from noise but they may partially cancel out each other’s errors.

The evaluation metric did not have good results for both validation and test, so we have an underfitting problem. To reduce model bias, I would first invest my time in feature engineering as this has the most significant effect on improving the model. After getting good enough result from a single model, I will then look into ensembles.
