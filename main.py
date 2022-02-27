import mysql.connector as mqt
        
def make_bill():
    name = input("Give customer name: ")
    ph_no = int(input("Give customer phone number: "))
    details = []
    n = int(input("Total Number of products: "))
    sum_ = 0
    for i in range(n):
        code = int(input("Give Code of Shoe: "))
        try:
            cursor.execute(f"select * from data where code = {code}")
            result = cursor.fetchall()[0]
            details.append([result[2],result[1],result[0]])
            sum_ += result[2]
        except:
            print("Code does not exist!")
    make_table(details,name,ph_no)    
    cursor.execute(f"insert into user_data(name,phone_no,total_money) values('{name}','{ph_no}','{sum_}')")
    mydb.commit()

def add_db():
    details = []
    cursor.execute(f"select * from data")
    last_code = cursor.fetchall()[-1][0]
    x = int(input("How many product you want to add?: "))
    for i in range(x):
        name = input("\nGive the product name: ")
        price = int(input("Give the product price: "))
        cursor.execute(f"INSERT INTO data (code, name, price) VALUES ('{last_code+1+i}','{name}','{price}')")
        mydb.commit()
        details.append([price,name,last_code+1+i])

    make_table(details,total=False)
    print("Data added!")
        
def remove_db():
    x = int(input("How many product you want to remove?: "))
    for i in range(x):
        code = int(input("\nGive Code of Shoe: "))
        cursor.execute(f"select price,name,code from data where code = {code}")
        data = cursor.fetchall()#[0]
        make_table(data,total=False)

        confermation = input("Are you sure you want to remove these data? (Y/N): ").lower()
        if confermation == "y":
            try:
                cursor.execute(f"delete from data where code = '{code}'")
                mydb.commit()
            except:
                print("Code does not exist!")
            print("Data erased!")

def make_table(details,name='Python',ph_no=1234567890,total=True):
    
    print(f"\n{'*'*30}\n")
    
    if name != 'Python' and ph_no != 1234567890:
        print(f"Name - {name}")
        print(f"Phone Number - {ph_no}")
    price_max = int()
    word_max = int()
    for i in details:
        if len(str(i[0])) >= price_max:
            price_max = len(str(i[0]))
        if len(i[1]) >= word_max:
            word_max = len(i[1])
    #slno = 1
    print(f"+{'-'*9}+{'-'*9}+-{'-'*word_max}-+-{'-'*price_max}-+")
    print(f"| Sl. No. |  Code   |{' '*((word_max-2)//2)}Name{' '*((word_max-2)//2 if ((word_max-2)/2).is_integer() else int(((word_max-2)/2)+0.5))}| Price |")
    print(f"+{'-'*9}+{'-'*9}+-{'-'*word_max}-+-{'-'*price_max}-+")
    

    sum_ = 0
    for i in range(len(details)):
        print(f"|    {i+1}    |   {details[i][2]}   |{' '*((word_max-(len(details[i][1])-2))//2)}{details[i][1]}{' '*((word_max-(len(details[i][1])-2))//2 if ((word_max-(len(details[i][1])-2))/2).is_integer() else int(((word_max-(len(details[i][1])-2))/2)+0.5))}|{' '*((price_max+2)-(len(str(details[i][0])))-1)}{details[i][0]} |")
        sum_ += details[i][0]
        
    print(f"+{'-'*9}+{'-'*9}+-{'-'*word_max}-+-{'-'*price_max}-+")
    
    if total:
        print(f"|{' '*((16+word_max+price_max)-(len(str(sum_))))}Total | {sum_} |")
        print(f"+{'-'*((21+word_max+price_max)-(len(str(sum_))))}-+-{'-'*(len(str(sum_)))}-+")
    
    print(f"\n{'*'*30}")
    
def main():
    database_login()
    val =  0 
    while val <4 and val >= 0:
        print("\nChoose the number for action")
        print("1) Make a Bill")
        print("2) Add product in database")
        print("3) Remove product from database")
        print("4) EXIT!\n")
        val = int(input("Give Val: "))
        #print("\n")
        if val == 1:
            make_bill()
        elif val == 2:
            add_db()
        elif val == 3:
            remove_db()
        elif val == 4:
            print("Shutting Down")
                
def database_login():
    global mydb,cursor
    while True:
        psdw = (input("Give your MySQL password: "))  # It is 1234
        try:
            mydb = mqt.connect(host='localhost',user='root',password=psdw,database="shoe_database")
            cursor = mydb.cursor()
            break
        except:
            print("wrong Password, try again\n")


if __name__ == "__main__":
    main()
    