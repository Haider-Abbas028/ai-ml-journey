import os
import csv
from collections import defaultdict

def read_csv(filename: str)->list:
    """Read CSV and convert it into a list of dictionaries"""
    if not os.path.exists(filename):
        print(f"File '{filename}' nahi mili!")
        return []
    
    rows=[]
    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            row['age'] = int(row['age'])
            row['salary'] = int(row['salary'])
            rows.append(row)
    print(f"{len(rows)} rows loaded successfully!")
    return rows

def filter_by_age(rows:list , min_age:int=25)->list:
    "filtered rows where age > min_age"
    filtered=[row for row in rows if row['age'] > min_age]
    print(f"After filter (age > {min_age}): {len(filtered)} rows")
    return filtered

def group_by_city(rows:list)->dict:
    "group rows by city using defaultdict"
    grouped=defaultdict(list)
    for row in rows:
        grouped[row['city']].append(row)
    print(f" Grouped into {len(grouped)} cities")
    return dict(grouped)

def calculate_average_salary(grouped_data:dict)->dict:
    salary_averages={}
    for city, employees in grouped_data.items():
        salaries=[emp['salary'] for emp in employees]
        salary_averages[city]=sum(salaries)/len(salaries)
    print(f"Average salaries by city: {salary_averages}")
    return salary_averages

def sort_cities_by_salary(averages:dict)->list:
    "Sort cities by average salary (descending)"
    sorted_cities=sorted(averages.items(), key=lambda x: x[1], reverse=True)
    print(f"Cities sorted by average salary: {sorted_cities}")
    return sorted_cities

def write_results(sorted_cities:list, grouped_data:dict, filename:str='results.csv'):
    "Write results to CSV"
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['City', 'Average Salary', 'Total Employees'])
        for city, avg_salary in sorted_cities:
            writer.writerow([city, round(avg_salary, 2), len(grouped_data[city])])  

def print_summary(grouped_data:dict, averages:dict, sorted_cities:list):
    "Print summary of results"
    print("\n" + "="*50)
    print("Summary of Results:")
    print("="*50)
    for city, avg_salary in sorted_cities:
        total_employees = len(grouped_data[city])
        print(f"City: {city}, Average Salary: {round(avg_salary, 2)}, Total Employees: {total_employees}")
    print("="*50)


def main():
    filename = 'employees.csv'
    rows = read_csv(filename)
    if not rows:
        return

    filtered_rows = filter_by_age(rows, min_age=25)
    grouped_data = group_by_city(filtered_rows)
    averages = calculate_average_salary(grouped_data)
    sorted_cities = sort_cities_by_salary(averages)
    write_results(sorted_cities, grouped_data, filename='results.csv')
    print_summary(grouped_data, averages, sorted_cities)

if __name__ == "__main__":
    main()