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
all_sales=0
print(data)
def func():
    for stores in data:
        sales=stores[0:]
        print(sales)
        for daily_sales in sales:
            all_sales+=daily_sales
            length=len(sales)
            avg=all_sales/length
            print(f"{data[0]}: {avg}")

func()

    

