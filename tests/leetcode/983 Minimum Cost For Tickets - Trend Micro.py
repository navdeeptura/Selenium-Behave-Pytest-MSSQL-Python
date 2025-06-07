"""
Problem 3: Minimum Cost for Travel
Description:
You are given a list of days when you need to travel.
You can purchase travel passes:
1-day pass costs 2
7-day pass costs 7
30-day pass costs 25
if day is 29 or 30, but cost 2 pass
The goal is to find the minimum cost to cover all travel days.
"""


def min_cost_travel(travel_days):

    basic_ticket = 2
    bundle_ticket = 7
    bundle_days = 7
    big_bundle_cost = 25
    big_bundle_ticket = 30
    end_days_array = [28, 29, 30]

    # creating a blank array with 2 cost on travel days
    cost_array = [0] * big_bundle_ticket

    # Buying basic_cost ticket for all travel days
    for i in travel_days:
        cost_array[i-1] = basic_ticket
    print(f"After Basic_Ticket: Cost  Array: {cost_array}")

    current_day = 1
    # creating a while look to buy a bundle_ticket
    # if cost of consecutive days exceeds bundle_ticket
    while current_day <= 30:
        i = current_day - 1 #array index for cost for that day
        #print (f"Day: {current_day}, {bundle_days} days travel cost array is {cost_array[i:i+bundle_days]}")
        #print(f"Sum of 7 from Day {i} to Day {i+7}: ", sum(cost_array[i:i+7]))

        # do not buy ticket, if not travelling on current day
        if cost_array[i] == 0:
            current_day += 1

        # ignoring cost update for last few days, basic_ticket is already bought previously
        elif current_day in end_days_array:
            current_day += 1

        # if sum of bundle_days cost exceeds bundle_ticket,
        # buy bundle_ticket and update remaining bundle days cost to zero
        elif sum(cost_array[i:i+bundle_days]) > bundle_ticket:
            cost_array[i] = bundle_ticket
            cost_array[i+1 : i+bundle_days] = [0] * (bundle_days - 1)
            #print (f"cost of array after updating: {cost_array}")
            current_day += bundle_days
        else:
            current_day += 1
    print (f"After Bundle_Ticket: Cost Array: {cost_array}")
    print (f"After Bundle_Ticket: Total Cost: {sum(cost_array)}")
    return min(big_bundle_cost, sum(cost_array))


if __name__ == '__main__':
    cost = min_cost_travel([1, 15, 29])
    print (cost)


def test_find_min_cost_1():
    assert min_cost_travel([1, 4, 6, 7, 8, 20]), 11

def test_find_min_cost_2():
    assert min_cost_travel([1, 2, 3, 4, 5, 6, 7]), 7

def test_find_min_cost_3():
    assert min_cost_travel([1, 8, 15, 22]), 8

def test_find_min_cost_sample_1():
    assert min_cost_travel([1, 4, 6, 7, 8, 20]) == 11

def test_find_min_cost_sample_2():
    assert min_cost_travel([1, 2, 3, 4, 5, 6, 7]) == 7

def test_find_min_cost_sample_3():
    assert min_cost_travel([1, 8, 15, 22]) == 8

def test_one_day_travel():
    assert min_cost_travel([15]) == 2

def test_two_days_far_apart():
    assert min_cost_travel([1, 30]) == 4

def test_consecutive_two_weeks():
    assert min_cost_travel(list(range(1, 15))) == 14  # two 7-day passes

def test_all_days_in_month():
    assert min_cost_travel(list(range(1, 31))) == 25  # use 30-day pass

def test_sparse_days_in_month():
    assert min_cost_travel([1, 10, 20, 30]) == 8  # four 1-day passes or two 7-days

def test_alternate_days():
    assert min_cost_travel(list(range(1, 31, 2))) == 25  # best with 30-day

def test_every_5_days():
    assert min_cost_travel([5, 10, 15, 20, 25, 30]) == 12

def test_last_7_days_of_month():
    assert min_cost_travel([24, 25, 26, 27, 28, 29, 30]) == 7

def test_first_week_only():
    assert min_cost_travel([1, 2, 3, 4, 5, 6, 7]) == 7

def test_days_span_two_weeks():
    assert min_cost_travel([1, 2, 3, 8, 9, 10]) == 12

def test_travel_on_every_3rd_day():
    assert min_cost_travel([3, 6, 9, 12, 15, 18, 21, 24, 27, 30]) == 20

def test_only_last_day():
    assert min_cost_travel([30]) == 2

def test_full_week_and_one_more():
    assert min_cost_travel([1, 2, 3, 4, 5, 6, 7, 8]) == 9

def test_mixed_coverage_periods():
    assert min_cost_travel([1, 2, 3, 10, 11, 12, 13, 25, 26, 27]) == 19

def test_back_to_back_seven_day_ranges():
    assert min_cost_travel([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), 13

def test_random_non_consecutive_days():
    assert min_cost_travel([2, 5, 8, 15, 18, 21, 29]) == 14

def test_large_gap_between_days():
    assert min_cost_travel([1, 15, 29]) == 6  # 3 one-day passes or better with 7-days

