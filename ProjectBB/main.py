from datetime import datetime

import timestamp as timestamp

from application import salary
from application.db.people import get_employees

if __name__ == '__main__':
    salary.calculate_salary()
    get_employees()
    a = datetime.today()
    print(a)