# Jung-Talents
This include 3 tasks for different skills including SQL, Tableau, Python.
## Part 1:
This load is a multi-step process, firstly identifying valid securites, then uploading attributes for these, and then answering questions provided by the client. Securities may not be valid for numerous reasons such as no longer being traded on an exchange, and we are unable to load these securities. 

* Loading Securities into the platform (30%)
- To load the securities into the platform you need the following identifiers: MIC, QUEUESIP, Symbol, RequestId where one of QUEUESIP or Symbol must be populated. 
- The client wants to minimise the number of null values in QUEUESIP and Symbol.
- Provide us with your generated upload in a csv format, named {firstName}_{lastName}_section1.csv.
*Uploading Attributes (25%)
_ The attributes the client want are "Asset Class", "Inception Date", "Exchange Name", "Exchange Location", "Security Name", "Strong Oak Identifier", and "Return Since Inception". T
- The EulerId should correspond to the values generated from the first response.
- Exchange location should be given as the combination of Exchange Country and City (i.e. {country} - {city}).
- Provide us with your generated upload in a csv format, named {firstName}_{lastName}_section2.csv.
## Part 2: SQL & Power BI
1. Percentage Distribution
Total Sales by Product Category and the contribution against total sales.
2. Required to spread a fixed value of 2,000 across all products based on this distribution percentage. However, the spread of these number needs to be in whole number and not decimal point. The sum of all this product must add up to exactly 2,000.
3. Basket Data
What are the 2 most common products purchased together in an order?
4. Basket Data
With the dataset, develop a PowerBI dashboard that support strategic decision making.
## Part 3: SQL & Tableau
Data overview:
Payments: Each line represents a transaction payment for a contract
• TransactionID -> primary key / unique identifier
• ContractID -> a contract will have multiple repayments
• ClientID -> the client of the contract
• TransactionDate -> This is date in a EPOCH format - you will have to figure out how to convert it
• Amount -> Repayment amount
• Payment Code -> DEFAULT means a payment was not made
Clients: Each line represents a client and their information
• ClientID
• Entity Type -> Business type
• Entity Year Established -> First year the business was open
1. Business question:
Payment defaults are detrimental to the business and are a significant cost factor (Tableau)
Are there any key trends in the data which can help me avoid default-prone customers in the future?
https://public.tableau.com/app/profile/nhu.mai.nguyen/viz/Keytrendspaymentcode/Paymentcodespent
2. SQL
The business would like to understand what the overlap is between 2018 payment totals for their biggest clients and the rank of the overall payment totals within each entity. Note defaults do not count as payments. 
Please provide a csv containing the client IDs for 2018's top 20 clients when sorted on payment amount, as well as the entity type, 2018's total payment amount, and their overall (across all years) payment amount rank within the entity they belong to. Also include your SQL code. 



