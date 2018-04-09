

## The original idea for this dataset was to grab the KRAKEN's data on Ethereum/USD transactions for the first quarter of 2018. That was done using the following GET request.

```
https://rest.coinapi.io/v1/trades/KRAKEN_SPOT_ETH_USD/history?
time_start=2018-01-01T00:00:00&
time_end=2018-04-01T00:00:00&
limit=100000&
output_format=csv

Headers:

"X-CoinAPI-Key" = D2A074B9-26AE-4DA6-BB24-5C6BDEE9691C
```

## However


even though this worked perfectly fine using postman, this single large request drained my free API key, and i am not interested in paying to get more request (yes i tried making another free one with a different email but they are not stupid :D ) and of course i did not save the postman response. typical.

## Sooo..

 this assignment will now be executed on the provided dataset of bitcoin/usd transactions from Bitstamp. The one from the assignment creators repo.


## RESULTS:

What is the transaction with the highest volume in the timespan?

*- The transaction with the highest volume is: 29.37650126*

What is the average number of transactions per hour ?

*The average number of transactions per hour is: 1111*

What is the most favourite; selling or buying?

*- Most favourite was: BUY with 5075*
