mobiles = {
    'Samsung Galaxy S21' : 80999,
    'iPhone 12' : 79990,
    'Realme 7 Pro' : 35000,
    'Oppo A12' : 29780,
    'Moto G' : 45560
}
laptops = {
    'Lenovo Ideapad' : 30990,
    'HP 15s': 23990,
    'Asus TUF Gaming' : 64990,
    'Acer Aspire 7' :54960,
    'Dell Inspiron':61990
}
home_appliances = {
    'Pureit filter': 13000,
    'Bajaj fan': 1800,
    'Philips G7 Iron': 1125,
    'Dyson room air purifier': 38000,
    'Eureka vaccum cleaner': 4000
}
audio = {
    'Realme buds 2': 600,
    'boAt rockerz': 1299,
    'JBL Headset': 1100,
    'Ubon Bluetooth Headset': 1500,
    'Motorola Pulse 3': 2500
}
cameras = {
    'Canon EOS' : 25999,
    'Fujifilm XT3': 59000,
    'Sony B9': 66999,
    'Nikon D535': 44699,
    'Panasonic Lumix': 52650
}
categories = [mobiles, laptops, home_appliances, audio, cameras]
user_name=''
user_cart=[]
user_wishlist=[]
def get_user():
    global user_name
    user_name=input('Enter your name:')

def greet_user():
    global user_name
    print(f'\nHello!{user_name}.\nWelcome to FlipKart...')

def cart_or_wishlist(prod,price):
    global categories,user_cart,user_wishlist
    print('\n*** Choose one option***')
    print('1.Add to Wishlist')
    print('2.Add to Cart')
    print('0.Go back to main menu')
    choice=int(input('Enter your chioce'))
    if choice==0:
        show_menu()
    elif choice==1:
        user_wishlist.append({'name':prod,'price':price})
        print(f'\n{prod} is added to Wishlist')
        show_wishlist()
    else:
        user_cart.append({'name':prod,'price':price})
        print(f'\n{prod} is added to Cart')
        show_cart()

def show_categories():
    global categories
    category_name=['Mobiles','Laptops','Home Appliances','Audio','Cameras']
    num=1
    print('\n***Categories***')
    for i in range(len(category_name)):
        print(f'{i+1}.{category_name[i]}')
    print('0.Go to main menu')
    choice=int(input('Enter your choice'))
    if choice==0:
        show_menu()
    for prod_name,prod_price in categories[choice-1].items():
        print(f'\n{num}.{prod_name}\nPrice:Rs.{prod_price}')
        num+=1
    choice_prod=int(input("Choose any product:"))
    selected_prod_name=list(categories[choice-1])[choice_prod-1]
    selected_prod_price=categories[choice-1][selected_prod_name]
    cart_or_wishlist(selected_prod_name,selected_prod_price)

def show_cart():
    global user_cart
    if len(user_cart)==0:
        print('\nYour cart is Empty')
    else:
        for i,cart_item in enumerate(user_cart):
            print('{}.{}--Rs.{}/-'.format(i+1,cart_item['name'],cart_item['price']))
    show_menu()
def show_wishlist():
    global user_wishlist
    if len(user_wishlist) == 0:
        print('\nYour wishlist is Empty')
    else:
        for i, wish_item in enumerate(user_wishlist):
            print('{}.{}--Rs.{}/-'.format(i + 1, wish_item['name'], wish_item['price']))
    show_menu()

def show_menu():
    options=['Categories','My Cart','My Wishlist','Exit']
    print("\n***Choose any option***")
    for i in range(len(options)):
        print(f'{i+1}.{options[i]}')
    choice=int(input('Enter your choice:'))
    if choice==1:
        show_categories()
    elif choice==2:
        show_cart()
    elif choice==3:
        show_wishlist()
    elif choice==4:
        exit(0)
    else:
        print('\nInvaliad Input!!!.Please try again')
        show_menu()

get_user()
greet_user()
show_menu()