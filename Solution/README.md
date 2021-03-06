
# Approach

This data set has **23 coloumns** of which except two features radius and weight the others are catogorical.We deal with these categorical variables by **Scikit LabelEncoder()**.

The data set is pretty straight forward but we could plot some graphs and see which features are more likely to contribute towards the predictions.

**Plotting the correlation matrix**

![matrix](https://s20.postimg.org/q104yu0pp/corr.png)

We can see that the feature **veil-type** shows no correlation,that is the feature has just one unique value.So we can drop this feature!


Now we can explore the effect of the features on the predicted class a bit further.


![bruises](https://s20.postimg.org/50a3dwx7h/bruises.png)

![odor](https://s20.postimg.org/uhshxiexp/odor.png)

For the case of **Odor** except for the type **'n'** the other odor categories are only linked to one outcome class.This goes to show that Odor could be very important in predicting the right classes.


![gill_size](https://s20.postimg.org/g9y7v4cv1/gill_size.png)

![spore](https://s20.postimg.org/kht03veal/spore-print-color.png)


Now for the model we use **RandomForestClassifier** ,even the basic model without parameter tuning and cross validation would result in a 100% accuracy! The other classifiers would almost give the same outcome too,so the choice of classifier isn't important.

Splitting the data into **Train and Test(0.2)** the model gives an accuracy of **1** on the test data.

Confusion Matrix = array([[593,   0],
       [  0, 545]])
       
![Matrix](https://s20.postimg.org/rdhu0py59/confuse.png)
      


Training the RandomForestClassifier and plotting the features importance.

![Features importance](https://s20.postimg.org/ae8vlgmxp/features.png)

As expected **Odor** seems to be the most relevant feature.

## KEY TAKE AWAYS

Almond and Anise smell mushroom -> You will live!<br />
Odorless green or chocolate or white pore mushrooms -> You will most probably die!<br />
Any other smell -> Certain death!<br />
The rest ones -> Happy eating!<br />


