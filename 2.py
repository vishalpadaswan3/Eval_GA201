
def max_sal(employee)
    if not employee:
        return None
    
    maxs = float('-inf')
    max_sal_emp = None

    for emp in employee:
        salary = emp.get('salary',0)
        if salary > maxs
            maxs = salary
            max_sal_emp = emp

    return max_sal_emp


max_sal_name = max_sal(employee)
print(max_sal_name)