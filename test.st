func silnia(a: int) : int{
    if(a<=1){
        return 1
    }
    return (a * silnia(a - 1))
    print(a)
}

print(silnia(5))