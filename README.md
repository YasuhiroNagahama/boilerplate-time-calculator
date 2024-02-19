# Name（リポジトリ/プロジェクト/OSSなどの名前）

boilerplate-time-calculator

# DEMO



# Features

与えられた、「12時間制形式の時刻」、「時数と分数で示される経過時間」から**経過後の時間**と**何日後か**を返すプログラムです。オプション引数として、曜日を渡すことができ、その場合の戻り値には経過時間後の曜日が含まれます。

# Requirement

Python

# Installation

Pythonのインストーラーをダウンロード

# Usage

リポジトリをクローン
```bash
git clone https://github.com/YasuhiroNagahama/boilerplate-time-calculator.git
```

main.pyでadd_time関数に引数を渡す。
```python:main.py
print(add_time("3:00 PM", "3:10"))
# Returns: 6:10 PM
```

```bash
python main.py
```

# Note

引数のエラーチェックは行わないため、引数の形式が間違っている場合は、エラーが出るか、正しい値が返ってこないことがあります。

# Author

* 作成者
YasuhiroTakemura
* E-mail
* fnifhubi85h29bddi@gmail.com

# License
ライセンスを明示する

"hoge" is under [MIT license](https://en.wikipedia.org/wiki/MIT_License).

社内向けなら社外秘であることを明示してる

"hoge" is Confidential.
