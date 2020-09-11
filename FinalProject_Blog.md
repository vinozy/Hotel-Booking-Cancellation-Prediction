title: "Predicting Cancellation Helps Hotels Improve Revenue"
author: "Shiling Chen, Wenyu Han, Yumeng Tian, Jiaming Xie, Yuxuan Zhang, Ziyang Zhang"
date: "2020/4/26"

---



<center><font size = 6>Predicting Cancellation Helps Hotels Improve Revenue</font></center>

<p align="right"><font size = 4> -- Machine Learning Application in the Hospitality Industry</font></p>

### Cancellation at the Last Minute Steal Hotels’ Revenue

Nowadays, some hotels offer refundable rates and non-refundable rates to guests; some hotels require deposits to book the room. Recently, there is increasing interest in refundable rates and fewer deposit requirements, where guests have the possibility to cancel at the last minute. Whereas guests value the flexibility, hotels are dealing with the risk of empty rooms, leading to loss of revenue.

How can hotels save millions of dollars by making use of available online-booking information of each customer? As many of us have experienced, sometimes we would be told that the hotels we booked decided to upgrade our rooms. That’s usually because the hotel tends to oversell their rooms to maximize profit. Then when a certain type of room is in short, the hotel has to compensate the customers by upgrading their rooms. Thus, determining the overselling rate is important for hotels. In order to determine the overselling rate, the hotel needs to estimate the cancellation rate first. That’s what our project focuses on, to predict whether the guests would cancel their booking or not based on the booking information of each customer and how much the hotel can make profits from this. 

### Orders Likely to be Canceled Have Specific Patterns

#### Lead Time

For lead time, there is a significant difference between canceled and not canceled orders. For not canceled bookings, the majority of them are ordered within 100 days, while for canceled bookings, the distribution is not so concentrated, the majority is among 40-200 days before the arrival date. Canceled orders, in general, have longer lead time than not canceled orders. It’s intuitive because the more ahead of time, the higher probability the order will be canceled.

<img src="C:\Users\Ricky's Installation\AppData\Roaming\Typora\typora-user-images\image-20200427003524575.png" alt="image-20200427003524575" style="zoom: 50%;" />

#### Previous Cancel Rate and Previous Cancellation

For not canceled bookings, the majority of the previous cancel rate is 0, but for canceled orders, the distribution for the previous cancellation rate is not so concentrated and there is even a peak around 0.5.

<img src="C:\Users\Ricky's Installation\AppData\Roaming\Typora\typora-user-images\image-20200427003546554.png" alt="image-20200427003546554" style="zoom:50%;" />

For canceled orders, a higher proportion of guests have previous cancellation records, compared with not canceled orders. Even 100 guests have more than 20 previous cancellations, while this number for not canceled orders is zero. It’s also intuitive because those guests who have canceled many orders before may have this habit and also cancel this time.

<img src="C:\Users\Ricky's Installation\AppData\Roaming\Typora\typora-user-images\image-20200427003610126.png" alt="image-20200427003610126" style="zoom:50%;" />

#### Total Special Requests

For special requests, below is the pie chart for percentage of different numbers of special requests, left is for cancelled orders and right is for not cancelled orders. The right one has significantly more special requests, which suggests that when guests put forward special requirements, the hotel should not regard them as troublesome guests but as more trustworthy ones.

<img src="https://lh3.googleusercontent.com/ZgMNe6ct4kV7--kmYw9ng9egLXClNXhyIvlGi2etFJrBEzPQOQd2xEcF0bY6gDq-E3Mw71x0xHBNfGURr8dlZpPO46dgTPKu9kKLTnrPUZehmDZS__tgwf4PPFYQ3NaN4eMi3zyDzCk" alt="img" style="zoom: 50%;" />

####  Booking Changes

Changed bookings take up a higher percentage in not cancelled orders than in cancelled orders, which shows orders with more than one booking changes tends to have lower cancellation probability. So if a guest frequently changes his booking, perhaps the hotel could help him patiently instead of putting him in the blacklist.

<img src="C:\Users\Ricky's Installation\AppData\Roaming\Typora\typora-user-images\image-20200427003626804.png" alt="image-20200427003626804" style="zoom: 50%;" />

### Cancellation Predictions Effectively Save Revenues

We use 24 processed variables to predict the cancellation rate with Logistic Regression, Decision Tree, Random Forest, XGBoost, Neural Network.

#### Data Overview

- Date Information: Reservation date, Lead time, Check-out date...
- Booking Information: Room type, Meal, Booking Channel, Market Segment, Deposit Type...
- Personal Information: Number of adults, children

#### Cost Model Construction

In reality, hotels need to balance the trade-off between False Negative and False Positive to optimize their gross profit (= Revenue - Cost). According to [HOTSTATS’s research](https://www.hotstats.com/hotel-industry-trends/u.s.-hotels-finish-out-2019-strong-on-both-revenue-and-profit-fronts), in 2019, US hotels have an average RevPAR of \$141.06 and an average GOPPAR \$71.84. (GOPPAR stands for gross operating profit per available room; RevPAR stands for revenue per available room) Thus, we use ​\$141 as the average rate per room, ​\$71 as the gross profit per room, \$70 (=\$141-$71) as the average cost per empty room.

|                        | Rates |
| ---------------------- | ----- |
| Average Rate per Room  | $141  |
| Average  Cost per Room | $70   |
| Gross  Profit per Room | $71   |

**Assumptions**

- Not consideration of additional consumptions like foods and facilities, etc.

- The opportunity cost of an empty room is equal to the operation cost of an occupied room

- The total gross profit of a hotel follows the equation: 

  $$Total\ gross\ profit = the\ number\ of\ empty\ rooms*(-\$70) + the\ number\ of\ occupied\ rooms * $71$$

**Cost Matrix**

- In True Positive and True Negative cases, the customers who would cancel or not cancel will be predicted correctly. Under these circumstances, no room is left empty and the gross profit for each room is \$71.
- In False Positive case, the customers who don’t cancel their bookings are predicted to cancel. In this case, hotels usually have two options, the first lucky case is to find the customer the same type of room happening to be empty under the hotel chain, the hotel can earn profit from both rooms, which is usually very rare; the second is to book a similar room from a competitor and compensate the customer with future discounts or coupons, the hotel earns a profit from one room and pay the full amount for the other, which occurs quite often. Assuming that the probability of the first case is 20% and 80% for the second, that the coupon is 10% of the average daily rate, that the intangible reputation cost is 5% of the average daily rate
- In False Negative case, the customers who cancel their bookings are not predicted correctly. The cost is raised by leaving rooms empty.

![image-20200426232624866](C:\Users\Ricky's Installation\AppData\Roaming\Typora\typora-user-images\image-20200426232624866.png)

$$Total\ Gross\ Profit = $71*TN-$46*FP-$70*FN+$71*TP$$

#### Results and Conclusions

Using our models (test size = 0.25, test sample size = 29847 obs.), the machine learning results from different models are as below:

 

|                      | Gross Profit from the Conventional Model | Gross Profit from New Model | Improved Amount of Gross Profit | Improved Amount of Gross Profit per Room |
| -------------------- | ---------------------------------------- | --------------------------- | ------------------------------- | ---------------------------------------- |
| Logistic  Regression | $541,412                                 | $1,297,244                  | $758,898                        | $26                                      |
| Decision  Tree       | $546,282                                 | $1,295,580                  | $749,298                        | $25                                      |
| XGBoost              | $556,928                                 | $1,498,121                  | $941,193                        | $32                                      |
| Random  Forest       | $546,282                                 | $1,529,631                  | $983,349                        | $33                                      |
| **Neural  Network**  | $556928                                  | $1,567,845                  | $1,010,917                      | <font color = blue>$34</font>            |

**Advice For Hotels**

- **Overbooking rooms is better than leaving it empty**;
- Use ***Neural Network*** to predict the cancellation rate is the most efficient, which saves <font size = 4.5, color = blue>$34</font> per room for a hotel;
- Properly using the prediction results can **increase the gross profit per room** by around <font size = 4.5, color = blue>47%</font>

### Further Explorations

- This model is a simple version due to lack of data. The columns with codes represents different hotels, countries, which contain significant information. Take them into consideration if available;
- The cost matrix is also simplified. Actually some rooms cancelled will be re-booked afterwards. But in the dataset, a cancelled but re-booked room will not be recorded again.

