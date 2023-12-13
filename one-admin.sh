# =========================
# One Blog Management Shell
# =========================

# 処理名の配列
process=("init" "start")
# オプションの配列
mode=("--dev" "--prod")

# タイトルを出力する関数
function printProcess {
  case $1 in
    "${process[0]}" )
      printf "Initializing Application in \033[35m%s\033[m Mode\n" "$2";;
  esac
}

# 処理結果（成功・失敗）を出力する関数
function printResult {
  if [ "$1" -eq 0 ]; then
    printf "\033[32m Success \033[m\n"
  else
    printf "\033[31m Failed! \033[m\n"
  fi
}

# エラーを出力する関数
function printError {
  printf "\033[41m[ERROR]\033[m "
}

# 引数（処理名）の数をチェック
if [ $# -eq 0 ]; then
  printError
  printf "\033[31mNeeds at least one process!\033[m\n"
  exit 1
fi

# メイン処理
case $1 in
  # 初期化処理
  "${process[0]}" )
    # オプションバリデーション処理
    if [ "$2" = "${mode[0]}" ]; then
      printProcess "$1" "Development"
    elif [ "$2" = "${mode[1]}" ] || [ "$2" = "" ]; then
      printProcess "$1" "Production"
    else
      printError
      printf "\033[31mUnknown option '%s'!\033[m\n" "$2"
      exit 1
    fi

    # バックエンドの依存パッケージをインストール
    printf " Installing python requirements...\t"
    if [ "$2" = "" ]; then
      file="prod"
    else
      file=${2:2}
    fi
    python -m pip install -r "backend/requirements/${file}.txt" > /dev/null
    printResult $?

    # Git プレコミットをインストール
    if [ "$2" = "${mode[0]}" ]; then
      printf " Installing pre-commit hook...\t\t"
      pre-commit install > /dev/null
      printResult $?
    fi

    # マイグレーション
    printf " Running database migrations...\t\t"
    python backend/manage.py makemigrations > /dev/null
    python backend/manage.py migrate > /dev/null
    printResult $?
    ;;
  # 開発環境の起動
  "${process[1]}" )
    ;;
  * )
    printError
    printf "\033[31mUnknown process '%s'!\033[m\n" "$1"
    ;;
esac
