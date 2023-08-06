import datetime

from .report import send_to_slack


class TerminalText:
    def __init__(self, text):
        self._HEADER = '\033[95m'
        self._BLUE = '\033[94m'
        self._CYAN = '\033[96m'
        self._GREEN = '\033[92m'
        self._YELLOW = '\033[93m'
        self._FAIL = '\033[91m'
        self._END = '\033[0m'
        self._BOLD = '\033[1m'
        self._UNDERLINE = '\033[4m'
        self._TEXT = text
        self._DATETIME = f'{self._BLUE}**|**{self._END}{datetime.datetime.now()}{self._BLUE}**|**{self._END} '

    def header(self):
        """Print purple text """
        print(f'{self._DATETIME} {self._HEADER} - INFO - {self._TEXT} {self._END}')

    def tips(self):
        """Print blue text """
        print(f'{self._DATETIME} {self._GREEN} - TIPS - {self._END}{self._BLUE}{self._TEXT} \n{self._END}')

    def recommend(self):
        """Print cyan text """
        print(f'{self._DATETIME} {self._YELLOW} - RECOMMEND - {self._END}{self._CYAN}{self._TEXT}{self._END}')

    def info(self):
        """Print green text """
        print(f'{self._DATETIME} {self._GREEN} - INFO - {self._TEXT}{self._END}')

    def warning(self):
        """Print yellow text """
        print(f'{self._DATETIME} {self._YELLOW} - WARNING - {self._TEXT}{self._END}')

    def fail(self):
        """Print red text """
        print(f'{self._FAIL}"CRITICAL ==>"{self._END} \n{self._DATETIME} \n {self._FAIL}{self._TEXT}{self._END}')

    def text_error(self):
        """Print bold text """
        print(f'{self._DATETIME} {self._BOLD}{self._TEXT}{self._END}')

    def underline(self):
        """Print underline text """
        print(f'{self._DATETIME} {self._UNDERLINE}{self._TEXT}{self._END}')

    def report_to_slack(self, error):
        error_string = '`' + str(error) + '`'
        date = str(datetime.datetime.now())
        message = f'{date} \n*{self._TEXT}*'
        send_to_slack(message=message, error=error_string)
        text = 'An error was detected! \nThe bug results were sent to the developers, we will fix the problem and contact you shortly'
        print(f'{self._DATETIME} {self._GREEN}{text}{self._END}')

    def report_to_discord(self, error):
        """Report to discord server add later"""


if __name__ == '__main__':
    try:
        int('a')
    except ValueError as VA:
        TerminalText(
            'Тут буде опис проблеми від розробника, далі сама помилка:').report_to_slack(error=VA)
