# Hotel-Booking-Cancellation-Prediction
Applying Machine Learning to Hotel Booking Cancellation Prediction

1.Background
Nowadays, many hotels oversell rooms as part of their revenue management strategy.
While overselling rooms has some advantages including increasing revenue and mitigating loss, it may lead to bad guest experience and may raise additional costs for hotels to compensate guests, like additional coupons or upgrading their rooms.
To ensure that the number of hotel overbooking stays at the optimal number, hotels need to take the number of cancelled rooms into account, and make a strategy in place through analyzing canceling-room guests’ behaviors.

2.Project Overview
2.1 Hypothesis
If the cancellation probability of a client can be more accurately calibrated, a hotel can have a better plan to organize an oversell or better design charging fees (deposits).
2.2 Goal
Develop a predictive model of the probability of hotel booking cancellation.
2.3 Modeling and insights
Using models like logistic regression, decision tree, random forest, we can find out the most important features leading to cancellation. Based on that, we can figure out which kind of customers, what time period (season, how many days ahead of arrival, etc.), what kind of booking (hotel type, room type, booking channel, etc.) are prone to cancellation. Hotels can utilize this to design heterogeneous and customized strategies to reduce the cost brought by a cancellation. For example, if a single customer has a higher probability of cancellation, hotels can charge more deposit or cancellation fee for them to counter loss.

3.Data sources
Our data comes from two sources, Kaggle and other data we may find by ourselves after making some assumptions.
From Kaggle, we obtained a list of approximately 120,000 booking records with 32 features, including hotel category, booking date, arriving date, canceled or not, have children or not, booking room types, etc.
Kaggle data address: https://www.kaggle.com/jessemostipak/hotel-booking- demand#hotel_bookings.csv
Other data will only be added after we finish analyzing the Kaggle data. ScienceDirect: https://www.sciencedirect.com/science/article/pii/S2352340918315191
