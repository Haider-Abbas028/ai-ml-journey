import os
import csv
from collections import defaultdict

def read_csv(filename):
    """Read CSV and convert to list of dictionaries"""
    if not os.path.exists(filename):
        print(f"File '{filename}' nahi mili!")
        return []
    
    rows = []
    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            row['age'] = int(row['age'])
            row['salary'] = int(row['salary'])
            rows.append(row)
    
    print(f"✅ {len(rows)} rows loaded successfully!")
    return rows

def filter_by_age(rows, min_age=25):
    """Filter rows where age > min_age"""
    filtered = [row for row in rows if row['age'] > min_age]
    print(f"✅ After filter (age > {min_age}): {len(filtered)} rows")
    return filtered

def group_by_city(rows):
    """Group rows by city using defaultdict"""
    grouped = defaultdict(list)
    for row in rows:
        grouped[row['city']].append(row)
    print(f"✅ Grouped into {len(grouped)} cities")
    return dict(grouped)

def calculate_average_salary(grouped_data):
    """Calculate average salary per city"""
    averages = {}
    for city, employees in grouped_data.items():
        salaries = [emp['salary'] for emp in employees]
        averages[city] = sum(salaries) / len(salaries)
    return averages

def sort_cities_by_salary(averages):
    """Sort cities by average salary (descending)"""
    sorted_cities = sorted(averages.items(), key=lambda x: x[1], reverse=True)
    return sorted_cities

def write_results(sorted_cities, grouped_data, filename='results.csv'):
    """Write results to CSV"""
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['City', 'Average Salary', 'Total Employees'])
        for city, avg_salary in sorted_cities:
            writer.writerow([city, round(avg_salary, 2), len(grouped_data[city])])
    print(f"✅ Results saved to '{filename}'")

def print_summary(grouped_data, averages, sorted_cities):
    """Print summary of results"""
    print("\n" + "="*50)
    print("📊 CITY SUMMARY")
    print("="*50)
    
    for city, avg_salary in sorted_cities:
        count = len(grouped_data[city])
        print(f"{city:15} | Avg Salary: {avg_salary:>10,.2f} | Employees: {count:>3}")
    
    print("="*50)

# ==================== MAIN PIPELINE ====================

def main():
    print("\n🚀 Starting Data Processing Pipeline...\n")
    
    # Step 1-2: Read CSV
    data = read_csv('employees.csv')
    if not data:
        return
    
    # Step 3: Filter
    filtered = filter_by_age(data, 25)
    
    # Step 4: Group
    grouped = group_by_city(filtered)
    
    # Step 5: Average
    averages = calculate_average_salary(grouped)
    
    # Step 6: Sort
    sorted_cities = sort_cities_by_salary(averages)
    
    # Step 7: Write
    write_results(sorted_cities, grouped)
    
    # Print summary
    print_summary(grouped, averages, sorted_cities)
    
    print("\n✅ Pipeline Complete!")

if __name__ == "__main__":
    main()