from operator import truediv


def middleNum():
    # strIn = input()
    strIn = "3 2 4"
    numList = []
    for iStr in strIn.split():
        iNum = int(iStr)
        numList.append(iNum)

    numList.sort()
    print(numList[1])

def cheeperPath():
    M = 3
    N = 3

    table = [
        [2, 2, 2],
        [3, 3, 3],
        [1, 1, 1]
    ]

    for row in table:
        print(row)

    for i in range(M):
        for j in range(N):
            print(i, j, table[i][j])


def find_min_food_path(grid):
    n = len(grid[1])
    m = len(grid[0])

    dp = [[float('inf')] * m for _ in range(n)]

    dp[0][0] = grid[0][0]

    # Обновляем первый столбец
    for i in range(1, n):
        dp[i][0] = dp[i - 1][0] + grid[i][0]

    # Обновляем первую строку
    for j in range(1, m):
        dp[0][j] = dp[0][j - 1] + grid[0][j]

    # Заполняем остальную часть массива
    for i in range(1, n):
        for j in range(1, m):
            dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]

    return dp[n - 1][m - 1]








def main():
    # middleNum()
    # cheeperPath()

    # Пример использования
    grid = [
        [1, 3, 1, 1],
        [3, 100, 10, 50],
        [1, 7, 9, 11],
        [2, 2, 2, 1]
    ]

    min_weight = find_min_food_path(grid)
    print(min_weight)  # Вывод: 17


if __name__ == '__main__':
    main()