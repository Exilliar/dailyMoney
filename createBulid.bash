echo "Starting"

rm -rf build
mkdir build
zip -r build/dailyMoney.zip *
cd build/
echo '#!/usr/bin/env python3' | cat - dailyMoney.zip > dailyMoney
chmod 777 dailyMoney