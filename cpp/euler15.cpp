#include<iostream>
using namespace std;

const int GRIDSIZE = 20;
const int MEMOSIZE = GRIDSIZE + 1;

long long memo[MEMOSIZE][MEMOSIZE] = {0};

// TODO: check if this is really necessary.
// I guess static arrays are initialized with zeros!
void init_memo()
{
    for (int i = 0; i < MEMOSIZE; i++)
        for (int j = 0; j < MEMOSIZE; j++)
            memo[i][j] = 0;
}

long long count_moves(int i, int j)
{
    if (memo[i][j] > 0)
        return memo[i][j];
    if ((i == 0) || (j == 0))
        return memo[i][j] = 1;
    else
        return memo[i][j] = count_moves(i-1, j) + count_moves(i, j-1);
}

/*
long long count_moves(int i, int j)
{
    if ((i == 0) || (j == 0))
        1;
    else
        return count_moves(i-1, j) + count_moves(i, j-1);
}
*/

int main()
{
    /*
    for (int size = 0; size <= GRIDSIZE; size++) {
        cout << "Grid size = " << size << " possible moves = " << count_moves(size, size) << endl;
    }
    */
    int size = GRIDSIZE;
	//init_memo();
    cout << "Grid size = " << size << " possible moves = " << count_moves(size, size) << endl;

    return 0;
}
