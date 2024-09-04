import pandas as pd
import requests
import matplotlib.pyplot as plt
import japanize_matplotlib

urlPrefix = "https://gbfdata.com/ja/guild/"
myId = "1794561"
myUrl = urlPrefix + myId
opositeId = "1466159"
opositeUrl = urlPrefix + opositeId
headerNum = 0
header = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36",
    "X-Requested-With": "XMLHttpRequest",
}
r = requests.get(myUrl, headers=header)
myTable = pd.read_html(r.text)[0]
r = requests.get(opositeUrl, headers=header)
opositeTable = pd.read_html(r.text)[0]
concatTable = pd.concat([myTable, opositeTable], axis=1)
concatTable = concatTable[["回", "日付", "名前", "順位", "日速", "貢献度"]]
concatTable = concatTable.set_axis(
    [
        "回",
        "回2",
        "日付",
        "日付2",
        "自団名",
        "対戦団名",
        "自団順位",
        "対戦団順位",
        "自団日速",
        "対戦団日速",
        "自団累計貢献度",
        "対戦団累計貢献度",
    ],
    axis="columns",
)
concatTable = concatTable[
    [
        "回",
        "日付",
        "自団名",
        "対戦団名",
        "自団順位",
        "対戦団順位",
        "自団日速",
        "対戦団日速",
        "自団累計貢献度",
        "対戦団累計貢献度",
    ]
]
concatTable = concatTable[concatTable["回"] == concatTable["回"].max()]


def format_with_commas(value):
    return "{:,d}".format(value)


format_columns = [
    "自団順位",
    "対戦団順位",
    "自団日速",
    "対戦団日速",
    "自団累計貢献度",
    "対戦団累計貢献度",
]

for column in format_columns:
    concatTable[column] = concatTable[column].apply(format_with_commas)


fig, ax = plt.subplots(figsize=(30, 3))
ax.axis("off")
ax.axis("tight")
ax.table(
    cellText=concatTable.values,
    colLabels=concatTable.columns,
    bbox=[0, 0, 1, 1],
)

plt.show()
# print(concatTable)
