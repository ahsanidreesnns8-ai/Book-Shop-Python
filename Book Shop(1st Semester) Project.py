import time
print('Loading...')
for i in range(7):
    print('--',end='\t')
    time.sleep(0.5)
print('Welcome To Our Stationary Shop')
user_name=input("Enter your name: ")
user_ph=int(input("Enter your phone number: "))
user_address=input("Enter your address: ")
book_shop = {
    "notebook": 120,
    "textbook": 500,
    "story_book": 300,
    "dictionary": 450,
    "pen": 50,
    "pencil": 20,
    "eraser": 10,
    "sharpener": 15,
    "ruler": 30,
    "geometry_box": 250,
    "highlighter": 60,
    "marker": 40,
    "sketch_pens": 150,
    "color_pencils": 200,
    "crayons": 180,
    "drawing_book": 100,
    "register": 200,
    "clipboard": 120,
    "sticky_notes": 90,
    "file_folder": 150,
    "stapler": 220,
    "staples": 50,
    "glue": 70,
    "scissors": 180,
    "calculator": 1200,
    "school_bag": 1500,
    "water_bottle": 300,
    "lunch_box": 400,
    "exam_pad": 100,
    "whiteboard_marker": 80
}
company_account_number=1234500
for i,(keys,values) in enumerate(book_shop.items(),1):
    print(f'{i}. {keys} = {values} Rs.')
    time.sleep(0.5)
cart = []
count = 0
while True:
    try:
        user_ask = input("Enter item you want to buy(QUIT to stop): ")
        if user_ask in book_shop:
            cart.append(book_shop[user_ask])
            count+=1
        elif user_ask=='QUIT' or user_ask=='quit' or user_ask=='Quit':
            break
        else:
            print("Please enter that item that are available at shop.")
    except:
        raise 'Oops! You have entered wrong.'
total_price = sum(cart)
price = int(total_price)
user_input=input("You want to give cash or online payment(cash/online): ").lower()
if user_input=='cash':
    print(f"You are required to submit {price} Rs.")
    cash_input=int(input("Please give the amount: "))
    if cash_input>price:
        print(f'You have given {cash_input} and your remaning amount is {cash_input-price} Rs.')
    elif cash_input<price:
        print(f'you are required to give {price-cash_input} Rs more.')
    elif cash_input==price:
        print("You have given all amount.")
        print('Your Bill is here...')
elif user_input=='online':
    print('Here is our Account_number...') 
    print(f'{company_account_number}')
    user_account_number=int(input("Enter your account number: "))
    cash_online_input=input("Have you transferred your amount(Y/N): ").upper()
    if cash_online_input=='Y':
        print("Thanks you have submitted your price.")
        print("Thanks for your services...")
    elif cash_online_input=='N':
        print(f'You are required to share your bill price to our account_no{company_account_number}.')
discount = (price*10)/100
final_price=price-discount
dic = {}
dic['Name'] = user_name
dic['Phone number'] = user_ph
dic['Address'] = user_address
dic['Bill Price'] = final_price
dic['No. of Items']=count
for i in range(7):
    print('--',end='\t')
    time.sleep(0.1)
print("---DICTIONARY SHOP---")
for i,j in dic.items():
    print()
    print(f'{i}: {j}')
for i in range(7):
    print('--',end='\t')
    time.sleep(0.1)
#%%
