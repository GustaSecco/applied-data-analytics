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
- Credit pricing analysis
- Back-testing loan portfolios or renegotiating a loan by creating a
  new operation given present value of the former one and
  new installment value and number of periods that fits best the client's needs.
- Analysis of rentability for segments of clients with caracteristics in data sets.
