# =========================
# One Blog Management Shell
# =========================

# 処理名の配列（初期化 ユーザー作成 サーバーの起動 リントチェック 単体試験 言語メッセージ更新 ビルド）
process=("init" "create-user" "start" "lint" "ut" "message" "build")
# オプションの配列
mode=("--dev" "--prod" "--back" "--front")

# タイトルを出力する関数
function printProcess {
  case $1 in
    "${process[0]}" )
      printf "Initializing\033[35m%s\033[m Application" "$3"
      printf "in \033[35m%s\033[m Mode\n" "$2";;
  esac
}

# 処理結果（成功・失敗）を出力する関数
function printResult {
  printf " "
  printf ".%0.s" {0..30}
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
    if [ "$2" = "${mode[0]}" ] || [ "$2" = "" ]; then
      if [ "$3" != "" ]; then
        printError
        printf "\033[31mDon't need an option '%s'!\033[m\n" "$3"
        exit 1
      else
        printProcess "$1" "Development"
      fi

    elif [ "$2" = "${mode[1]}" ]; then
      if [ "$3" = "${mode[2]}" ] || [ "$3" = "" ]; then
        printProcess "$1" "Production" " Backend"
      elif [ "$3" = "${mode[3]}" ]; then
        printProcess "$1" "Production" " Frontend"
      else
        printError
        printf "\033[31mUnknown option '%s'!\033[m\n" "$3"
        exit 1
      fi
    else
      printError
      printf "\033[31mUnknown option '%s'!\033[m\n" "$2"
      exit 1
    fi

    # バックエンド初期化
    if [ "$3" != "${mode[3]}" ]; then
      # バックエンドの依存パッケージをインストール
      echo " Installing python requirements"
      if [ "$2" = "" ]; then
        file="dev"
      else
        file=${2:2}
      fi
      python -m pip install -r "backend/requirements/${file}.txt" > /dev/null
      printResult $?

      # Git プレコミットをインストール
      if [ "$2" != "${mode[1]}" ]; then
        echo " Installing pre-commit hook"
        pre-commit install > /dev/null
        printResult $?
      fi

      # マイグレーション
      echo " Running database migrations"
      cd backend || exit
      python manage.py makemigrations --noinput > /dev/null
      python manage.py migrate --noinput > /dev/null
      printResult $?

      # 言語パッケージをコンパイル
      echo " Compiling messages"
      python manage.py compilemessages > /dev/null
      printResult $?

      # 静的ファイルを収集
      if [ "$2" = "${mode[1]}" ]; then
        echo " Collecting static files"
        python manage.py collectstatic --noinput > /dev/null
        printResult $?
      fi
    fi

    # フロントエンド初期化
    if [ "$2" = "${mode[0]}" ] || [ "$2" = "" ] || [ "$3" = "${mode[3]}" ]; then
      # フロントエンドの依存パッケージをインストール
      echo " Installing npm requirements"
      if [ "$3" = "${mode[3]}" ]; then
        cd frontend || exit
        npm install > /dev/null
      else
        cd ../frontend || exit
        npm install > /dev/null
      fi
      printResult $?

      # フロントエンドをビルド
      if [ "$3" = "${mode[3]}" ]; then
        echo " Building frontend application"
        npm run build > /dev/null
        printResult $?
      fi
    fi
    ;;
  # ユーザー作成
  "${process[1]}" )
    cd backend || exit
    python manage.py createsuperuser
    ;;
  # サーバーの起動
  "${process[2]}" )
    if [ "$2" = "${mode[2]}" ]; then
      cd backend || exit
      gunicorn one.wsgi:application --bind 0.0.0.0:8000
    elif [ "$2" = "${mode[3]}" ]; then
      cd frontend || exit
      npm start
    else
      printError
      printf "\033[31mUnknown option '%s'!\033[m\n" "$2"
      exit 1
    fi
    ;;
  # リントチェック
  "${process[3]}" )
    pre-commit run --all-files
    ;;
  # 単体試験
  "${process[4]}" )
    cd backend || exit
    if coverage run manage.py test; then
      coverage report;coverage html
    fi
    cd ../frontend || exit
    npm run test
    ;;
  # 言語メッセージ更新
  "${process[5]}" )
    cd backend || exit
    python manage.py makemessages -l ja
    ;;
  # ビルド
  "${process[6]}" )
    # バックエンド・メッセージをビルド
    echo " Compile backend messages"
    python backend/manage.py compilemessages > /dev/null
    printResult $?
    ;;
  * )
    printError
    printf "\033[31mUnknown process '%s'!\033[m\n" "$1"
    ;;
esac
