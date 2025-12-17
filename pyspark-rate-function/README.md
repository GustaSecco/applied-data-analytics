# Implementing the RATE Function in PySpark (French Amortization / Price System)

## Context
In large-scale credit datasets, it is common to calculate implicit interest rates
from installment value, number of periods, and present value (French amortization / Price system).

While many analytical tools provide a RATE function, PySpark does not include a built-in
implementation suitable for large distributed datasets.

## Objective
Provide a scalable approach to computing interest rates using PySpark, enabling
rate calculation across millions of records in a distributed environment.

## Approach
- Implement a numerical method to approximate the interest rate
- Use PySpark UDFs to apply the calculation at scale
- Keep the implementation simple and readable

## When this is useful
- Back-testing Loan Portfolios: Analyzing historical performance and verifying interest rates across massive legacy datasets.
- Loan Renegotiation & Refinancing: Creating new operations by calculating the necessary rate given
  a specific Present Value ($PV$),
  a desired installment ($PMT$),
  and a set number of periods ($NPER$) that fits the client’s budget.
- Expected rentability analysis: Calculating the internal rate of return for different client segments to identify high-yield or high-risk behaviors within large datasets.
