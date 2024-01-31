# ===================================
# One Blog Automated Deployment Shell
# ===================================

PASSWORD=github
DATETIME="$(date '+%Y%m%d%H%M%S')"

echo "===== Update source code =========================="
cd One-Blog || exit
git pull

echo "===== Delete docker containers ===================="
docker-compose down --rmi all -v

echo "===== Backup database ============================="
mkdir -p ../bk
tar zcf "../bk/db_${DATETIME}.tar.gz" db
rm -Rf front/.next

echo "===== Create docker containers ===================="
docker-compose up -d
