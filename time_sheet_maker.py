import hour_scraper
import openpyxl as xl
from datetime import datetime, timedelta

hours = hour_scraper.main()
now = datetime.now()
desired_date = now + timedelta(days = 1)
month = desired_date.strftime("%m")
day = desired_date.strftime("%d")

raw_date = '{}/{}/{}'.format(month,day,"2021")
create_date = r'{}.{}.{}'.format("2021",month,day)

book = xl.load_workbook(r"C:\Users\e2008233\Desktop\Scrapper\Timesheet.xlsx")
sheet = book['Sheet1']

sheet["I2"] = raw_date

j = 0
for col in range(3, 8):
    sheet.cell(14, col).value = hours[j]
    j += 1

book.save(r"C:\Users\e2008233\Desktop\Scrapper\ " + create_date + r" - Weekly Timesheet - J. Xu.xlsx")