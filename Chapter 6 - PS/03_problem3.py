a = "Make a lot of money"
b = "buy now"  
c = "subscribe this"  
d = "click this"

message = input("Enter your comment: ")

if((a in message) or (b in message )or (c in message) or (d in message)):
    print("This comment is a spam")

else:
    print("This comment is not a spam")



# a = "make a lot of money"
# b = "buy now"
# c = "subscribe this"
# d = "click this"

# message = input("Enter your comment: ").lower()

# spam_keywords = [a, b, c, d]

# if any(keyword in message for keyword in spam_keywords):
#     print("This comment is a spam")
# else:
#     print("This comment is not a spam")
