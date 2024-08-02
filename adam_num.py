n=int(input())
rev=int(str(n)[::-1])
sqaure=n*n
revn=int(str(sqaure)[::-1])
revns=rev*rev
if revns== revn:
    print("It's Adam Number")
else:
    print("It's not Adam Number")

# n=int(input())
# r=int(str(n)[::-1])
# square=n*n
# rev=r*r
# revnumsquare=int(str(square)[::-1])
# if revnumsquare==rev:
#     print("Adam number.")
# else:
#     print("not an Adam number.")