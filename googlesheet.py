import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import date
import os
from dotenv import load_dotenv

load_dotenv()

JSON_FILE_NAME = os.environ.get('JSON_FILE_NAME')
SPREAD_SHEET_KEY = os.environ.get('SPREAD_SHEET_KEY')

googlesheeturl = ["https://spreadsheets.google.com/feeds"]
credentials = ServiceAccountCredentials.from_json_keyfile_name(JSON_FILE_NAME, googlesheeturl)
googlesheetclient = gspread.authorize(credentials)
spreadsheet = googlesheetclient.open_by_key(
    SPREAD_SHEET_KEY
)
worksheet = spreadsheet.get_worksheet(0)

# 取得所有資料表資料
# data = worksheet.get_all_values()


# 收入
def earn(money):
    """
    記錄收入到工作表

    Parameters:
    - money (int): 金額

    Returns:
    - str: 回傳訊息
    """

    worksheet.append_row([date.today().isoformat(), money, 0])
    return f"已添加您今天的收入，恭喜！!"


# 支出
def loss(money):
    """
    記錄支出到工作表

    Parameters:
    - money (int): 金額

    Returns:
    - str: 回傳訊息
    """

    worksheet.append_row([date.today().isoformat(), 0, money])
    return f"輸了沒關係，明天再加油！!"


def total():
    """
    從工作表取得計算後的總盈餘

    Returns:
    - str: 回傳總盈餘訊息
    """

    total_profit = worksheet.cell(1, 4).value
    return f"總盈餘:{total_profit}"
