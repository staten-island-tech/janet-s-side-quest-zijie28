## This function opens the CSV for You!
def csv_to_list(file_path):
    data_list = []
    
    with open(file_path, 'r') as file:
        for line in file:
            row = line.strip().split(',')
            row = [int(value) if value.isdigit() else value for value in row]
            data_list.append(row)

    return data_list


file_path = "SalesData.csv"  
data = csv_to_list(file_path)
  # Output the list
""" def func():
    for stores in data[1:]:
        store_name=stores[0]
        sale=map(int, stores[1:])
        sales=sum(sale)
        avg=sales/len(stores)
        print(f"{store_name}: {round(avg)}" )
func() """

""" def func():
    store={}
    most_money=[]
    money={}
    for stores in data[1:]:
        store_name=stores[0]
        sale=map(int, stores[1:])
        sales=sum(sale)
        avg=round(sales/len(stores))
        store[avg] = store_name
        money[store_name]= avg
        most_money.append(store[avg])
        most_money.sort(reverse=True)
    print(f"The store with the most money is {most_money[0]} with {money[most_money[0]]}$")

func()
 """
    
""" def func():
    total=0
    for stores in data[1:]:
        sale=map(int, stores[1:])
        sales=sum(sale)
        avg=sales/len(stores)
        total+= avg
    whole_avg = total/len(data[1:])
    print(f"The total average is {round(whole_avg)}")
func() """

def func():
    total=0
    for stores in data[1:]:
        sale=map(int, stores[1:])
        sales=sum(sale)
        avg=sales/len(stores)
        total+= avg
    whole_avg = total/len(data[1:])
    under_80=whole_avg*0.8
    for stores in data[1:]:
        store_name=stores[0]
        sale=map(int, stores[1:])
        sales=sum(sale)
        avg=sales/len(stores)
        if avg < under_80:
            print(f"The {store_name} location is at risk of closing!")
func()

