from pyspark.sql import SparkSession
from pyspark.sql.functions import col, udf
from pyspark.sql.types import DoubleType
import math
from scipy.optimize import newton




def rate_finder(periods, period_amount, principal, final_amount, type=0, guess=0.10):
    """
    Solves for the interest rate per period (RATE).

    The function sets up the annuity equation to be equal to zero,
    and then uses the Newton-Raphson method (via scipy.optimize.newton)
    to find the root (the rate).
    """
    try:
        # The annuity equation that must equal zero to find the rate
        def financial_equation(rate):
            if rate == 0:
                return principal + period_amount * periods + fv
            else:
                return principal * (1 + rate)**periods + \
                       period_amount * (1 + rate * type) * (((1 + rate)**periods - 1) / rate) + final_amount

        # Use scipy.optimize.newton to find the root (the rate)
        rate = newton(financial_equation, guess, maxiter=100)
        return float(rate)
    except RuntimeError:
        # Return None or a placeholder if the root is not found
        return None
        
# Register as UDFs
rate_finder_udf = udf(rate_finder, DoubleType())

#Initialize Spark
spark = SparkSession.builder \
    .appName("LoanRateCalculation") \
    .getOrCreate()

# Read the CSV file
df = spark.read.csv("loans.csv", header=True, inferSchema=True)

# Apply calculations using UDFs
result_df = df \
    .withColumn("finance_interest_rate",
                rate_finder_udf(col("periods"), col("period_amount"), col("principal_value"), col("final_amount")))
result_df.show()
