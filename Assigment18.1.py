
# coding: utf-8

# In[ ]:


# Blodd glucose levels for obese patients have a mean of 100 with a standard deviation of 15. A resercher thinks that a diet hight 
# in raw cornstarchwill have a positive effect on blood glucose levels. A sample of 36 patients who have tried the raw conrnstarch diet
# diet have a mean glucose level of 108. Test the hypothesis that the raw cornstarch had an effect or not.


# In[ ]:


M = 100
SDP = 15
M = 108
Sample = 36
Significance level assumed (.05) 

Ho - Mean blood glucose <= 100
H1 - Mean blood glucose > 100

z_alpha(.05) c.v. = 1.645
z_score = (108 - 100) / (15/sqrt(36)) = 48/15 = 3.2
z_score > critcal value z_alpha, no reject 

