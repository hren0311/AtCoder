 
#int '1' => 1
a = int(input())

#int　複数 '1 2' => a=1,b=2
a,b = map(int,input().split())

#int 複数　リスト化 '1 2' => [1,2]
num_list = list(map(int,input().split()))
#ただし要素数が1になる可能性がある場合使えない
#以下を使用
num_list = [int(x) for x in input().split()]

#str '1' => '1'
a = input()

#str 一文字ずつ 'abc' => ['a','b','c']
a = list(input())

#str 複数 'a b' => a='a' b='b'
a,b = input().split()

#str 複数　リスト化 'a b' = ['a','b']
str_list = input().split()

#n行 文字列　リスト 一文字ずつ
"""
'###'     [['#','#','#'],
'#.#'  ->  ['#','.','#'],
'###'      ['#','#','#']]
"""
n = 3
n_list = [list(input()) for i in range(n)]

#n行　リスト 数字
"""
1 2      [[1,2],
2 3  =>   [2,3],
3 4       [3,4]]
"""
n = 3
n_list = [list(map(int,input().split())) for i in range(n)]
