# Calculator Project / 電卓プロジェクト

A small command-line calculator built while learning Python program structure and Git.

Python のプログラム構成と Git を学ぶために作成した、コマンドライン電卓です。

## Features / 機能

- Addition, multiplication, and division / 加算・乗算・除算
- Division-by-zero handling / ゼロ除算のエラー処理
- Calculation history saved to `history.txt` / `history.txt` への計算履歴保存
- Commands for help, history, clearing history, and quitting / ヘルプ・履歴表示・履歴削除・終了コマンド
- Separate calculator, input, command, and storage responsibilities / 計算・入力・コマンド・保存処理の分離

## Run / 実行方法

Requires Python 3. No third-party packages are needed.

Python 3 が必要です。外部パッケージは使用していません。

```bash
python3 main.py
```

At the prompt, press Enter to calculate or use one of these commands:

プロンプトで Enter を押すと計算できます。次のコマンドも使用できます。

| Command | Action / 動作 |
| --- | --- |
| `help` | Show available commands / コマンド一覧を表示 |
| `history` | Show saved calculations / 保存した計算履歴を表示 |
| `clear` | Clear the history file / 履歴ファイルを消去 |
| `q` | Quit / 終了 |

## Project structure / 構成

- `main.py`: command loop and result display / コマンドループと結果表示
- `calculator.py`: arithmetic operations / 計算処理
- `utils.py`: input, history, and command handling / 入力・履歴・コマンド処理
- `history.txt`: local calculation history / ローカルの計算履歴

## Current limitations / 現在の制限

- Number input is limited to integers. / 数値入力は整数に限定されています。
- The project has no automated tests or graphical interface. / 自動テストと GUI はまだありません。
- History is stored in a local text file. / 履歴はローカルのテキストファイルに保存されます。

## Provenance / 制作情報

The application source code is Kanata Araki's original learning work. The bilingual README organization and editing were prepared with AI assistance. No open-source license is granted.

アプリケーションのソースコードは、荒木奏多が学習の過程で作成したオリジナル作品です。このバイリンガル README の構成と編集には AI の支援を利用しています。オープンソースライセンスは付与していません。
