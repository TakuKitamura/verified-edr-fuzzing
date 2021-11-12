#include "ParseDoor.h"
#include "ParseIndicator.h"
#include "ParseSpeed.h"
#include <unistd.h>

// American Fuzzy Lopが標準入力にFuzzを渡してくる
int main()
{
    uint8_t buf[13] = {0};
    if (read(0, buf, 13) != 13)
        return 0; // 渡されたFuzzが13バイト以上でない場合は終了し,先頭13バイトのみをbufに格納

    uint32_t can_id = buf[0] << 8 * 3 | buf[1] << 8 * 2 | buf[2] << 8 * 1 | buf[3]; // bufの先頭4byteをスライス
    uint8_t can_dlc = buf[4];
    uint8_t data[8] = {0}; // bufのindex 5以降の8byteをスライス
    for (int i = 5; i < 13; i++)
        data[i] = buf[i];

    // fuzzing対象のF*で開発した3つの関数
    parseDoor(can_id, can_dlc, data);
    parseIndicator(can_id, can_dlc, data);
    parseSpeed(can_id, can_dlc, data);
    return 0;
}