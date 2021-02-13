# React を使用したアプリ開発

# 機能

- Go を使用した API 機能
- Firebase を使用したログイン機能
  - redux による全体共有データの管理
  - .env による API キー隠蔽
- React+Typescript を使用したフロントエンド開発
- MaterialUI を使用したデザイン
- その他
  - .gitignore による Github 管理の調整
  -

# 使用ツール

# 各項目の解説

## ソースコードの構成

- components
  - pages
  - parts
  - templates

## 使用ライブラリの解説

- web-vitals：CreateReactApp でデフォルトで導入される GoogleChrome での計測ツール
- Redux：

## API キーなどの情報を隠すには？

project の root に「.env」

'''
dx = [1, 0, -1, 0];
dy = [0, -1, 0, 1];
R = 0
U = 1
L = 2
D = 3

class State:
def **init**(self, x:int, y:int, ticket:int, cost:int):
self.x = x
self.y = y
self.ticket = ticket
self.cost = cost

    def hashCode(self):
      return (self.x << 16) | self.y;

    def equals(self, other):
        return (self.x == other.x) and (self.y == other.y) and (self.ticket == other.ticket)

    def compareTo(self, other):
        return (self.cost - other.cost)

def dijkstra(h:int, w:int, t, n:int, sx:int, sy:int, gx:int, gy:int):
#q = queue.PriorityQueue()
q = list()
closed = []
initialState = State(sx, sy, n, t[sy][sx])
q.append(initialState)

    count = 0
    while not len(q) == 0:
        st = q.pop()
        print(len(q))
        print(f"(x, y) = ({st.x}, {st.y})")
        if st.x == gx and st.y == gy:
            return st.cost
        if st in closed:
            continue

        closed.append(st)

        for i in range(4):
            nx = st.x + dx[i]
            ny = st.y + dy[i]

            if (0 <= nx < w) and (0 <= ny < h):
                print(f"(nx, ny) = ({nx}, {ny}, チケット:{n})")
                ncost1 = st.cost + t[ny][nx]

                #同じ状態がなければ追加する
                next_state = State(nx, ny, st.ticket, ncost1)
                is_add = True
                for state in q:
                    if state == next_state:
                        is_add = False
                if is_add:
                    q.append(next_state)

                if st.ticket > 0:
                    ncost2 = st.cost
                    #q.put(State(nx, ny, st.ticket - 1, ncost2))

        count += 1
        if count >10:
            break

    print("抜けました")

if **name** == '**main**':
input_line = input()

    #盤面の縦横を取得
    h = int(input_line.split(" ")[0])
    w = int(input_line.split(" ")[1])

    t = []
    for y in range(h):
        input_line = input()
        row = []
        for x in range(w):
            item = int(input_line.split(" ")[x])
            row.append(item)
        t.append(row)

    input_line = input()
    ticket = int(input_line)
    print(t)
    print(ticket)
    print(" ")

    cost = dijkstra(h, w, t, ticket, 0, 0, w-1, h-1);
    print(cost)

'''
