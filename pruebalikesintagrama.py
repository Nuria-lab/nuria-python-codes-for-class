likes=[[
            "2020-11-12T02:31:34+00:00",
            "pauladesalvo"
        ],
        [
            "2020-11-12T01:02:42+00:00",
            "lacopecope"
        ],
        [
            "2020-11-12T00:47:59+00:00",
            "sauvage.showroom"
        ]]

cantidad_de_likes=len(likes)
print(cantidad_de_likes)

personaquelikeo="sauvage.showroom"
likesalapersonaquelikeo=0

x=0
while x<cantidad_de_likes:
    print(likes[x][1])
    
    if likes[x][1]==personaquelikeo:
        likesalapersonaquelikeo=likesalapersonaquelikeo+1
    
    x=x+1

print(likesalapersonaquelikeo)