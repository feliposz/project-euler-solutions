#include <iostream>
#include <ctime>
#include <cstdlib>

using namespace std;

// This program is ok, but unfortunatley it overflows when reaching values beyond

int main()
{
    time_t start = time(NULL);

    long long total, blue, red, improve_num, improve_den;
    long double num, den;

    blue = 15;
    red = 6;

    while (total <= 1000000000000LL) {
        while (true) {
            total = blue + red;

            num = (long double) blue * (blue - 1);
            den = (long double) total * (total - 1);

            if (num <= 0 || den <= 0) {
                cerr << "Overflow!" << endl;
                exit(1);
            }

            if (num * 2 == den) {
                improve_num = red;
                improve_den = blue;
                cout << "Blues: " << blue << " Reds: " << red;
                cout << " Total: " << total << " Time: " << (time(NULL) - start);
                cout << endl;
                break;
            } else if (num * 2 > den)
                red++;
            else
                break;
        }
        blue++;
        red = blue * improve_num / improve_den;
    }
    return 0;
}


/*

Values ok:
Blues: 15 Reds: 6 Total: 21 Time: 0
Blues: 85 Reds: 35 Total: 120 Time: 0
Blues: 493 Reds: 204 Total: 697 Time: 0
Blues: 2871 Reds: 1189 Total: 4060 Time: 0
Blues: 16731 Reds: 6930 Total: 23661 Time: 0
Blues: 97513 Reds: 40391 Total: 137904 Time: 0
Blues: 568345 Reds: 235416 Total: 803761 Time: 0
Blues: 3312555 Reds: 1372105 Total: 4684660 Time: 0
Blues: 19306983 Reds: 7997214 Total: 27304197 Time: 2
Blues: 112529341 Reds: 46611179 Total: 159140520 Time: 12
Blues: 655869061 Reds: 271669860 Total: 927538921 Time: 69

These values might be wrong:
Blues: 3822685023 Reds: 1583407981 Total: 5406093004 Time: 405

*/
