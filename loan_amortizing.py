from datetime import datetime, timedelta
import calendar
import pandas as pd
import openpyxl


##
# EMI will pe applied from next month of loan issue
# ##
def prepare_loan_details(principal: int, issue_date, emi: int, rate_per_cent: float, emi_day: int, book_entries,
                         execute_from_start=True):
    issue_dt = datetime.strptime(issue_date, '%Y-%m-%d')
    if execute_from_start:
        nu_day_in_month = calendar.monthrange(issue_dt.year, issue_dt.month)[1]
        nu_day_for_interest = nu_day_in_month - issue_dt.day + 1  # 31(nu Of Day in Month) - 1(date) + 1
        nu_of_days_in_year = {True: 366, False: 365}[calendar.isleap(issue_dt.year)]
        interest = round(principal * rate_per_cent * nu_day_for_interest / nu_of_days_in_year)
        month_last_day_entry_date = issue_dt + timedelta(days=nu_day_for_interest - 1)
        book_entries.append(
            {"date": datetime.strftime(month_last_day_entry_date, '%Y-%m-%d'), "principal": principal,
             "interest": interest,
             "interest_days": nu_day_for_interest,
             "amount": principal + interest,
             "total_interest_of_month": interest})
        new_principal = principal + interest
        monthly_emi_details(new_principal, month_last_day_entry_date + timedelta(days=1), emi, rate_per_cent, emi_day,
                            book_entries)
    else:
        monthly_emi_details(principal, issue_dt + timedelta(days=1), emi, rate_per_cent, emi_day,
                            book_entries)


def monthly_emi_details(principal: int, emi_month_first_day: datetime, emi: int, rate_per_cent: float, emi_day: int,
                        book_entries):
    nu_of_days_in_year = {True: 366, False: 365}[calendar.isleap(emi_month_first_day.year)]
    interest_till_emi_day = round(principal * rate_per_cent * (emi_day - 1) / nu_of_days_in_year)

    book_entries.append(
        {"date": datetime.strftime(emi_month_first_day + timedelta(days=emi_day - 1), '%Y-%m-%d'),
         "principal": principal,
         "interest": interest_till_emi_day,
         "interest_days": emi_day - 1,
         "amount": principal - emi,
         "emi": emi
         })

    new_principal = principal - emi

    nu_day_in_month = calendar.monthrange(emi_month_first_day.year, emi_month_first_day.month)[1]
    nu_day_for_interest_after_emi = nu_day_in_month - emi_day + 1
    interest_after_emi_day = round(
        new_principal * rate_per_cent * nu_day_for_interest_after_emi / nu_of_days_in_year)
    book_entries.append(
        {"date": datetime.strftime(emi_month_first_day + timedelta(days=nu_day_in_month - 1), '%Y-%m-%d'),
         "principal": new_principal,
         "interest": interest_after_emi_day,
         "interest_days": nu_day_for_interest_after_emi,
         "amount": new_principal + interest_till_emi_day + interest_after_emi_day,
         "total_interest_of_month": interest_till_emi_day + interest_after_emi_day})
    if new_principal <= emi:
        return
    else:
        monthly_emi_details(new_principal + interest_till_emi_day + interest_after_emi_day,
                            emi_month_first_day + timedelta(days=nu_day_in_month),
                            emi, rate_per_cent, emi_day, book_entries)


books = []
prepare_loan_details(1300000, "2021-10-13", 47500, 7.5 / 100, 10, books, execute_from_start=True)
dataList = map(
    lambda entry: [entry['date'], entry['principal'], entry['interest'], entry['interest_days'], entry['amount'],
                   entry.get('total_interest_of_month', ''), entry.get('emi', '')], books)
df = pd.DataFrame(dataList,
                  columns=['date', 'principal', 'interest', 'interest_days', 'amount', 'total_interest_of_month',
                           'emi'])
df.to_excel("loan_schedule.xlsx", sheet_name="loan details", index=False, freeze_panes=(1, 7))
print(df)
