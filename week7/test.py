# """mod doc"""
# def main():
#     """doc"""
#     times = int(input())
#     promotion = int(input())
#     stamp = int(input())
#     change = int(input())
#     discount = int(input())
#     price = 0
#     total = 0
#     my_stamp = 0
#     price_result = 0
#     for _ in range(times):
#         price = int(input())
#         price_result += price
#         total += price
#         if total >= promotion:
#             my_stamp += (total//promotion)*stamp
#         if my_stamp >= change:
#             price_result -= (my_stamp//change)*discount
#             total -= (my_stamp//change)*discount
#             my_stamp -= (my_stamp//change)*change
#         total -= (total//promotion)*promotion
#     print(price_result)
#     print(my_stamp)
# main()