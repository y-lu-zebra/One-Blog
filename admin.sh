# ======================================================================================
# One Blog Management Shell
# ======================================================================================

# 処理名の配列（初期化 ユーザー作成 サーバーの起動 リントチェック 単体試験 ビルド）
process=("init" "adduser" "start" "lint" "ut" "build")
# オプションの配列
mode=("--dev" "--prod" "--back" "--front")

function check_array() {
    arr=$2
    echo "${arr[@]}" | xargs -n 1 | grep -E "^${1}$" > /dev/null
    return $?
}

# タイトルを出力する関数
function printProcess {
  case $1 in
    "${process[0]}" )
      if [ "$2" = "app" ]; then
        printf "Initializing\033[33m%s\033[m Application" "$3"
      else
        case $4 in
          "purple" )
            printf " in \033[35m%s\033[m Mode\n" "$3"
          ;;
          "blue" )
            printf " in \033[34m%s\033[m Mode\n" "$3"
          ;;
        esac
      fi
      ;;
  esac
}

# 処理結果（成功・失敗）を出力する関数
function printResult {
  printf "\t"
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

    # オプションによるモード判定
    is_back=$(echo "$@" | grep "${mode[2]:2}")
    is_front=$(echo "$@" | grep "${mode[3]:2}")
    is_prod=$(echo "$@" | grep "${mode[1]:2}")

    init_back=0
    init_front=0

    # アプリ・情報の出力
    if [ "$is_back" ] && [ "$is_front" = "" ]; then
      printProcess "$1" "app" " Backend"
      init_back=1
    elif [ "$is_front" ] && [ "$is_back" = "" ]; then
      printProcess "$1" "app" " Frontend"
      init_front=1
    else
      printProcess "$1" "app"
      init_back=1
      init_front=1
    fi
    # モード・情報の出力
    if [ "$is_prod" ] ; then
      printProcess "$1" "mode" "Production" "purple"
    else
      printProcess "$1" "mode" "Development" "blue"
    fi

    # バックエンドの初期化
    if [ $init_back -eq 1 ]; then
      # バックエンドの依存パッケージをインストール
      if [ "$is_prod" ]; then
        file="prod"
      else
        file="dev"
      fi
      printf "\tInstalling python requirements\n"
      cd backend || exit
      python -m pip install --upgrade pip > /dev/null
      python -m pip install -r "requirements/${file}.txt" > /dev/null
      printResult $?

      # マイグレーション
      printf "\tRunning database migrations\n"
      python manage.py makemigrations --noinput > /dev/null
      python manage.py migrate --noinput > /dev/null
      printResult $?

      # 言語パッケージをコンパイル
      printf "\tCompiling messages\n"
      python manage.py compilemessages > /dev/null
      printResult $?

      # 開発モードのみで実行する処理
      if [ "$is_prod" = "" ]; then
        # 静的ファイルを収集
        printf "\tCollecting static files\n"
        python manage.py collectstatic --noinput > /dev/null
        printResult $?

        # Git プレコミットをインストール
        printf "\tInstalling pre-commit hooks\n"
        pre-commit install > /dev/null
        printResult $?
      fi
    fi

#    # フロントエンド初期化
#    if [ "$2" = "${mode[0]}" ] || [ "$2" = "" ] || [ "$3" = "${mode[3]}" ]; then
#      # フロントエンドの依存パッケージをインストール
#      echo " Installing npm requirements"
#      if [ "$3" = "${mode[3]}" ]; then
#        cd frontend || exit
#        npm install > /dev/null
#      else
#        cd ../frontend || exit
#        npm install > /dev/null
#      fi
#      printResult $?
#
#      # フロントエンドをビルド
#      if [ "$3" = "${mode[3]}" ]; then
#        echo " Building frontend application"
#        npm run build > /dev/null
#        printResult $?
#      fi
#    fi
    ;;

  # ユーザー作成
  "${process[1]}" )
    cd backend || exit
    python manage.py createsuperuser
    ;;

#  # サーバーの起動
#  "${process[2]}" )
#    if [ "$2" = "${mode[2]}" ]; then
#      cd backend || exit
#      gunicorn one.wsgi:application --bind 0.0.0.0:8000
#    elif [ "$2" = "${mode[3]}" ]; then
#      cd frontend || exit
#      npm start
#    else
#      printError
#      printf "\033[31mUnknown option '%s'!\033[m\n" "$2"
#      exit 1
#    fi
#    ;;
#  # リントチェック
#  "${process[3]}" )
#    pre-commit run --all-files
#    ;;

  # 単体試験
  "${process[4]}" )
    cd backend || exit
    if coverage run manage.py test; then
      coverage report;coverage html
    fi
#    cd ../frontend || exit
#    npm run test
    ;;

#  # ビルド
#  "${process[5]}" )
#    # バックエンド・メッセージをビルド
#    echo " Compile backend messages"
#    python backend/manage.py compilemessages > /dev/null
#    printResult $?
#    ;;
#  * )
#    printError
#    printf "\033[31mUnknown process '%s'!\033[m\n" "$1"
#    ;;
esac
