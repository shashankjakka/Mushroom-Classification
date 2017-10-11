
# Approach

This data set has **23 coloumns** of which except two features radius and weight are catogorical.So we deal these categorical variables with **LabelEncoder()**.

The data set is pretty straight forward but we could plot some graphs and see which features are more likely to contribute towards the predictions.

**Plotting the correlation matrix**

![matrix](https://s20.postimg.org/r0kguobod/corr.png)

We can see that the feature * veil-type * shows no correlation that is the feature has just one unique value.So we can drop this feature!

