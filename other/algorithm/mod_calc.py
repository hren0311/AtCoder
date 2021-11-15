#modの計算

a = 3
b = 5
mod = 10

#いつmodをとっても同じ結果
#足し算
print("足し算",(a+b)%mod,((a%mod)+(b%mod)) % mod)

#引き算
print("引き算",(a-b)%mod,((a%mod)-(b%mod)) % mod)

#掛け算
print("掛け算",(a*b)%mod,((a%mod)*(b%mod)) % mod)

#割る数divがmod mと互いに素
#div*a==div*b (mod m) <=> a==b (mod m)


### mod同士の割り算 逆元をかける ###

#bとmが互いに素である場合のみ有効
#mが素数であれば，常にbとmは互いに素
m=7

#(1//b) == (b)^(m-2) (mod m)
inv = pow(b,m-2,m)
#(a/b) (mod m)
ans = (a*inv) % m

#pow 2^5 (mod 7)
pow(2,5,7)
