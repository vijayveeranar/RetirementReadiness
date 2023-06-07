import numpy as np
import matplotlib.pyplot as plt

# These are input variables
current_age = 40
retirement_age = 45
current_annual_income = 2000000
savings_per_month = 10000
current_savings_bal = 1000000
roi_savings = 0.07
retire_income_per_month = (0.70 * current_annual_income)/12
monthly_pension = 0
other_income_post_ret = 45000+30000
life_expectancy = 70
roi_change = 0.02
current_annual_income_change = 0.2
savings_per_month_change = 0.2
corpus_from_wealth_dilution = 4500000+8500000

# These are output variables
retirement_conf = 0

def calc_corpus_from_savings(savings_per_month, current_savings_bal, roi_savings):
    savings_per_year = savings_per_month * 12
    remaining_working_years = retirement_age - current_age
    SI_savings_Mon = savings_per_year * remaining_working_years * roi_savings
    corpus_from_saving_mon = savings_per_year + SI_savings_Mon
    SI_savings_current = current_savings_bal * remaining_working_years * roi_savings
    corpus_from_saving_curr = current_savings_bal + SI_savings_current
    total_corpus_from_savings = corpus_from_saving_mon + corpus_from_saving_curr
    return total_corpus_from_savings

def generate_corpus_during_ret(savings_per_month, current_savings_bal, roi_savings):
    corpus_from_savings = calc_corpus_from_savings(savings_per_month, current_savings_bal, roi_savings)
    return corpus_from_savings

def compute_sample(mean, change):
    min = mean - change
    max = mean + change
    std_dev = (max - min) / 6
    sample = np.random.normal(mean, std_dev)
    return sample


def generate_random_samples(roi_savings, roi_change, current_annual_income, \
                            current_annual_income_change, savings_per_month, \
                            savings_per_month_change):
    roi_sample = compute_sample(roi_savings, roi_change)
    annual_income_sample = compute_sample(current_annual_income, current_annual_income_change)
    saving_month_sample = compute_sample(savings_per_month, savings_per_month_change)
    #print(roi_sample)
    #print(annual_income_sample)
    #print(saving_month_sample)
    return roi_sample, annual_income_sample, saving_month_sample


def generate_monthly_income_during_ret(return_from_savings_mon, monthly_pension, other_income_post_ret):
    monthly_income_ret = return_from_savings_mon + monthly_pension + other_income_post_ret
    return monthly_income_ret

def return_from_savings_month(corpus_from_wealth_dilution, corpus_from_savings, roi_savings):
    ret_corpus_interest = (corpus_from_wealth_dilution + corpus_from_savings) * roi_savings
    return_from_savings_mon = ret_corpus_interest / 12
    return return_from_savings_mon

def tot_income_per_month_post_ret(return_from_savings_mon, monthly_pension, other_income_post_ret):
    total_income_mon_ret = return_from_savings_mon + monthly_pension + other_income_post_ret
    return total_income_mon_ret

def calculate_certainty(outcomes, target):
    num_success = np.sum(outcomes >= target)
    probability = num_success / len(outcomes)
    return probability

def simulate_income_post_ret(iterations):

    tot_income_per_month_ret_arr = np.empty((0,))
    #print(tot_income_per_month_ret_arr)
    for i in range(iterations):
        roi_savings_sample, current_annual_income_sample, savings_per_month_sample  = generate_random_samples(roi_savings, roi_change, \
                                                                current_annual_income, current_annual_income_change,\
                                                                savings_per_month, savings_per_month_change)
       
        corpus_from_savings = generate_corpus_during_ret(savings_per_month_sample, current_savings_bal, roi_savings_sample)
        return_from_savings_mon = return_from_savings_month(corpus_from_wealth_dilution, corpus_from_savings, roi_savings_sample)
        #print(f"return from savings: {return_from_savings_mon}")
        tot_income_per_month_ret = tot_income_per_month_post_ret(return_from_savings_mon, monthly_pension, \
                                                                other_income_post_ret)
        #print(tot_income_per_month_ret)
        tot_income_per_month_ret_arr = np.append(tot_income_per_month_ret_arr, tot_income_per_month_ret)

    # print(tot_income_per_month_ret_arr)
    # Plot a histogram
    # plt.hist(tot_income_per_month_ret_arr, bins='auto', color='skyblue', alpha=0.7, rwidth=0.85)
    # plt.xlabel('Value')
    # plt.ylabel('Frequency')
    # plt.title('Histogram')
    # plt.grid(True)
    # plt.show()

    certainty = calculate_certainty(tot_income_per_month_ret_arr, retire_income_per_month)
    return certainty
    #print(f"The certainty of meeting the target is: {certainty * 100}%")

#simulate_income_post_ret(1000)

       

