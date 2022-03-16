import statistics
import random
import pandas as pd
import plotly.figure_factory as ff
import plotly.graph_objects as go

df = pd.read_csv("C109/PRO-C109/StudentsPerformance.csv")
scores = df["reading score"].to_list()

mean = sum(scores)/len(scores)
std_deviation = statistics.stdev(scores)
median = statistics.median(scores)
mode = statistics.mode(scores)

print(mean)
print(median)
print(mode)
print(std_deviation)

std1_start, std1_end = mean-std_deviation, mean+std_deviation
std2_start, std2_end = mean-(2*std_deviation), mean+(2*std_deviation)
std3_start, std3_end = mean-(3*std_deviation), mean+(3*std_deviation)

list_within_1_std = [result for result in scores if result>std1_start and result<std1_end]
list_within_2_std = [result for result in scores if result>std2_start and result<std2_end]
list_within_3_std = [result for result in scores if result>std3_start and result<std3_end]

print("% of data within 1st std dev ", len(list_within_1_std)/len(scores)*100,)
print("% of data within 2nd std dev ", len(list_within_2_std)/len(scores)*100,)
print("% of data within 3rd std dev ", len(list_within_3_std)/len(scores)*100,)


fig = ff.create_distplot([scores],["Result"])
fig.add_trace(go.Scatter(x = [mean,mean], y = [0,0.17], mode = "lines", name = "MEAN"))

fig.add_trace(go.Scatter(x = [std1_start,std1_start], y = [0,0.17], mode = "lines", name = "STANDARD DEV 1 START"))
fig.add_trace(go.Scatter(x = [std1_end,std1_end], y = [0,0.17], mode = "lines", name = "STANDARD DEV 1 END"))

fig.add_trace(go.Scatter(x = [std2_start,std2_start], y = [0,0.17], mode = "lines", name = "STANDARD DEV 2 START"))
fig.add_trace(go.Scatter(x = [std2_end,std2_end], y = [0,0.17], mode = "lines", name = "STANDARD DEV 2 END"))

fig.add_trace(go.Scatter(x = [std3_start,std3_start], y = [0,0.17], mode = "lines", name = "STANDARD DEV 3 START"))
fig.add_trace(go.Scatter(x = [std3_end,std3_end], y = [0,0.17], mode = "lines", name = "STANDARD DEV 3 END"))

fig.show()

