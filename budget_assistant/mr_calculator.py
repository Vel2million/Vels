# INCOME, SAVING, FIXED EXPENSE, TRAVEL, HEALTH
# FOR TEST INHERITANCE

import hashlib
import logging

logging.basicConfig(level=logging.INFO)

SALT = 'GenshinImpact'
LINE_DECORATOR = "-" * 50


class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name


class SalaryMan(Person):
    def __init__(self, first_name, last_name, salary, classified=False):
        super().__init__(first_name, last_name)
        self.salary = salary
        self.is_classified = classified
        self.last_name = self.verify_data(self.last_name)
        self.salary = int(self.verify_data(str(self.salary)))
        self.provident_fund = (self.salary * 15) / 100
        self.tax = 6269.17
        self.soc_sec = 300
        self.net_pay = self._get_net_pay()
        
        # below are fixed expenses
        self.exps_family = 3000
        self.exps_apt_rental = 6000
        self.exps_ais_bill = 747.93
        self.exps_true_bill = 800
        self.exps_bts = 1300
        self.exps_water_bill = 50
        self.exps_elec_bill = 500
        self.fixed_expense = self._get_fixed_expense()

        self.sal_after_fixed = self.net_pay - self.fixed_expense

    def _get_net_pay(self):
        return self.salary - self.provident_fund - self.tax - self.soc_sec

    def _get_fixed_expense(self):
        fixed_exp = (
            self.exps_family +
            self.exps_apt_rental +
            self.exps_ais_bill +
            self.exps_true_bill +
            self.exps_bts +
            self.exps_water_bill +
            self.exps_elec_bill
        )
        return fixed_exp

    def verify_data(self, data):
        return self.classify_data(data) if self.is_classified else data

    def classify_data(self, data):
        sha_obj = hashlib.sha256()
        sha_obj.update(str.encode(SALT + data))
        return sha_obj.hexdigest()

    def show_initial_info(self):
        logging.info(LINE_DECORATOR + " Run Mode " + LINE_DECORATOR)
        logging.info(f" Secured Mode: {self.is_classified}")
        logging.info(LINE_DECORATOR + " Person Info " + LINE_DECORATOR)
        logging.info(f" First Name: {self.first_name}")
        logging.info(f" Last Name: {self.last_name}")
        logging.info(LINE_DECORATOR + " Income " + LINE_DECORATOR)
        logging.info(f" Salary: {self.salary}")
        logging.info(f" PF 15%: {self.provident_fund}")
        logging.info(f" TAX: {self.tax}")
        logging.info(f" SOC-SEC: {self.soc_sec}")
        logging.info(f" Net Pay: {self.net_pay}")

        logging.info(LINE_DECORATOR + " Fixed Expense " + LINE_DECORATOR)
        logging.info(f" After fixed expenses: {self.sal_after_fixed}")

        logging.info(LINE_DECORATOR + " What if you save 20k a month " + LINE_DECORATOR)
        money_left = self.sal_after_fixed - 20000
        logging.info(f" After saving: {money_left}")

        logging.info(LINE_DECORATOR + " What if you eat 12k a month " + LINE_DECORATOR)
        money_left = money_left - 12000
        logging.info(f" You still have: {money_left}")

        logging.info(LINE_DECORATOR + " Summarize " + LINE_DECORATOR)
        logging.info(f" Total Income: {self.salary * 12}")
        logging.info(f" Total PF: {self.provident_fund * 12}")
        logging.info(f" Total SOC: {self.soc_sec * 12}")
        logging.info(f" Total TAX : {self.tax * 12}")
        logging.info(f" Total Net : {self.net_pay * 12}")
        logging.info(f" Saving Total : {self.provident_fund * 12 + 120000}")
        logging.info(" Travel Budget : 120000")
        logging.info(f" Total fixed expenses: {self.sal_after_fixed * 12}")
        logging.info(f" Total money left: {money_left * 12}")


if __name__ == "__main__":
    # chopper = SalaryMan('Chopper', 'Tonytony', 99000000, classified=True)
    # chopper.show_initial_info()

    zoro = SalaryMan('Peter', 'Quill', 92000, classified=False)
    zoro.show_initial_info()
