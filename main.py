from timeit import timeit
import matplotlib.pyplot as plt


time_func = []
time_lambda = []

for i in range(100):
    function_ = timeit(f"_function.function_({i})", setup="import _function", number=1000)
    lambda_ = timeit(f"_lambda.lambda_({i})", setup="import _lambda", number=1000)
    time_func.append(function_)
    time_lambda.append(lambda_)

plt.plot([x for x in range(len(time_func))], time_func)
plt.plot([x for x in range(len(time_lambda))], time_lambda)
plt.legend(["Function", "Lambda"])
plt.show()
