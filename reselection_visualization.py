import pickle
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from functions import*

def DataFormation(data):

    data = pd.DataFrame(data, columns = ['SW_1', 'SW_2'])

    SW_1, SW_2 = data['SW_1'], data['SW_2']

    SW_1 = DataExtraction(SW_1)
    SW_2 = DataExtraction(SW_2)

    return SW_1, SW_2

#platform capacity
capacity_unit = 100
capacity_range = 15

data_path = 'data/reselection/latest_reselection_result.p'
data = pickle.load(open(data_path, 'rb'))

#[mere_SW, expected_SW, realized_SW, pre_budget, post_budget, payment, fee, changed_payment, changed_fee, cost, running_time]
SW_1, SW_2 = DataFormation(data)

SW_1 = DataTrimming(SW_1)
SW_2 = DataTrimming(SW_2)

#capacity range
capacity = capacity_unit*np.arange(1, capacity_range + 0.1)

reselection_distribution = np.load('data/reselection/reselection_distribution.npy')

num_requester = reselection_distribution[0].mean(axis = 0)
num_provider = reselection_distribution[1].mean(axis = 0)
print(num_requester)
print(num_provider)

#[mere_SW, expected_SW, realized_SW, pre_budget, post_budget, payment, fee, changed_payment, changed_fee, cost, running_time]
#mere SW
plt.plot(capacity, SW_1[:, 0], 'ko-', markersize = 13, label = 'B.M: NSW')
plt.plot(capacity, SW_2[:, 0], 'k^-', markersize = 13, label = 'ESWM: NSW')
#added
plt.plot(capacity, SW_1[:, 1], 'ro--', markersize = 13, label = 'B.M : ESW')
plt.plot(capacity, SW_2[:, 1], 'g^--', markersize = 13, label = 'ESWM: ESW')
#added

plt.xlim(50, 1050)
plt.xlabel('Platform Capacity', fontsize = 25)
plt.ylabel(r'Social Welfare (x$10^4$)', fontsize = 25)
plt.xticks(fontsize = 25)
plt.yticks(fontsize = 25)
plt.yticks(np.arange(0, 51000, 10000), np.arange(0, 5.1, 1), fontsize = 25)
plt.legend(loc='upper center', bbox_to_anchor=(0.5, 1.05), ncol = 2, fontsize = 18, fancybox = True, framealpha = 0.5)
plt.tight_layout()
plt.show()

#Platform utility: before submission
plt.plot(capacity, SW_1[:, 3], 'r--o', markersize = 13, label = 'B.M:t$\leq t_{sub}$')
plt.plot(capacity, SW_2[:, 3], 'g--^', markersize = 13, label = 'ESWM:t$\leq t_{sub}$')
#added
plt.plot(capacity, SW_1[:, 4], 'r-o', markersize = 13, label = 'B.M:t$>t_{sub}$')
plt.plot(capacity, SW_2[:, 4], 'g-^', markersize = 13, label = 'ESWM:t$> t_{sub}$')
#added

plt.xlim(50, 1050)
plt.xlabel('Platform Capacity', fontsize = 25)
plt.ylabel(r'Platform Utility (x$10^3$)', fontsize = 25)
plt.xticks(fontsize = 25)
plt.yticks(fontsize = 25)
plt.yticks(np.arange(0, 17000, 4000), np.arange(0, 17, 4),fontsize = 25)
plt.legend(loc='upper center', bbox_to_anchor=(0.5, 1.05), ncol = 2, fontsize = 17, fancybox = True, framealpha = 0.5)
plt.tight_layout()
plt.show()

#Q1: In the previous simulation, I divided the summation of requester and provider utility
#with the number of requesters and providers. However, should the avg utility be only for selected winners?
#avg requester utility
plt.plot(capacity, (SW_1[:, 2] + SW_1[:, -2] - SW_1[:, -3]) / num_requester[0], 'ro--', markersize = 13, label = 'B.M')
plt.plot(capacity, (SW_2[:, 2] + SW_2[:, -2] - SW_2[:, -3]) / num_requester[1], 'g^--', markersize = 13, label = 'ESWM')
plt.xlim(50, 1050)
plt.xlabel('Platform Capacity', fontsize = 25)
plt.ylabel('Average Requester Utility', fontsize = 25)
plt.xticks(fontsize = 25)
#plt.yticks(fontsize = 25)
plt.yticks(np.arange(0, 26, 5), fontsize = 25)
plt.legend(loc = 'best', fontsize = 25)
plt.tight_layout()
plt.show()

#avg provider utility
plt.plot(capacity, (SW_1[:, -4] - SW_1[:, -2]) / num_provider[0], 'ro--', markersize = 13, label = 'B.M')
plt.plot(capacity, (SW_2[:, -4] - SW_2[:, -2]) / num_provider[1], 'g^--', markersize = 13, label = 'ESWM')
plt.xlim(50, 1050)
plt.xlabel('Platform Capacity', fontsize = 25)
plt.ylabel('Average provider Utility', fontsize = 25)
plt.xticks(fontsize = 25)
plt.yticks(np.arange(0, 2.1, 0.5), fontsize = 25)
plt.legend(loc = 'best', fontsize = 25)
plt.tight_layout()
plt.show()

#running time
plt.plot(capacity, SW_1[:, -1], 'ro--', label = '[8]')
plt.plot(capacity, SW_2[:, -1], 'g^--', label = 'ESWM')
plt.xlim(50, 1050)
plt.xlabel('Platform Capacity', fontsize = 25)
plt.ylabel('Running Time(s)', fontsize = 25)
plt.xticks(fontsize = 25)
plt.yticks(fontsize = 25)
#plt.yticks(np.arange(0, 61000, 10000), np.arange(0, 61, 10),fontsize = 25)
#plt.legend(loc = 'best', fontsize = 25)
plt.tight_layout()
plt.show()






































#end
