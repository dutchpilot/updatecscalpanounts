# updatecscalpamounts
Программа подключается к бирже FTX или Binance, где получает список инструментов с текущими ценами. 
Исходя из цены инструмента, значений депозита, плеча и пропорций расcчитываются объемы.
Настройки стаканов перезаписываются в папке C:\Users\ИМЯ_ПОЛЬЗОВАТЕЛЯ\AppData\Roaming\CScalp\Visualizer\mvs_cs\
В .tmp-файлах заменяются значения параметров First|Second|Third|Fourth|Fifth_WorkAmount.
Перед перезаписью настройки стаканов сохраняются в папку backup.

FTX: Бессрочные фьючерсы
/api/futures

FTX: Спот
/api/markets

Binance: Бессрочные фьючерсы
/fapi/v1/exchangeInfo
fapi/v1/premiumIndex (цена markPrice)"
