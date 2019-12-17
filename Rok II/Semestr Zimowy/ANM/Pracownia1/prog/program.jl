function fac(n)
    fact = one(n)
    for m in 1:n
        fact *= m
    end
    fact
end

function Tn32malkwodwrwykres(n)
    sum::Float32 = 0
    i::Int64 = 0
    k::Int64 = 1
    inc::Float32 = 0
    while i <= n
        if i != 0
            k = k * i
        end
        inc = k * k
        inc = 1/inc
        sum = sum + inc
        i = i + 1
    end
    return sum
end 

function Tn32malkwodwr(n)
    sum::Float32 = 0
    i::Int64 = 0
    k::Int64 = 1
    inc::Float32 = 0
    while i <= n
        if i != 0
            k = k * i
        end
        println("iterator: ",i,"  silnia: ", k)
        inc = k * k
        inc = 1/inc
        if sum == sum + inc
            println("Następny wyraz już nic nie zmienia: Koniec ")
        end
        sum = sum + inc
        println(sum)
        i = i + 1
    end
end    

Tn32malkwodwr(8)

function Tn32malodwrkw(n)
    sum::Float32 = 0
    i::Int64 = 0
    k::Int64 = 1
    inc::Float32 = 0
    while i <= n
        if i != 0
            k = k * i
        end
        println("iterator: ",i,"  silnia: ", k)
        inc = 1/k
        inc = inc * inc
        if sum == sum + inc
            println("Następny wyraz już nic nie zmienia: Koniec ")
        end
        sum = sum + inc
        println(sum)
        i = i + 1
    end
end    

Tn32malodwrkw(8)

function Tn32rosnkwodwr(n)
    sum::Float32 = 0
    i::Int64 = n
    k::Int64 = fac(n)
    inc::Float32 = 0
    first::Float32 = 1
    while i >= 0
        if i == 0
            sum = sum + first
            println("iterator: ",i,"  silnia: ", k)
            println(sum)
            i = i - 1
        else
            println("iterator: ",i,"  silnia: ", k)
            inc = k * k
            inc = 1/inc
            sum = sum + inc
            println(sum)
            k = k / i
            i = i - 1
        end
    end
end   

println("7 składników")
println("")
Tn32rosnkwodwr(7)
println("")
println("6 składników")
println("")
Tn32rosnkwodwr(6)
println("")
println("5 składników")
println("")
Tn32rosnkwodwr(5)
println("")

function Tn32rosnodwrkw(n)
    sum::Float32 = 0
    i::Int64 = n
    k::Int64 = fac(n)
    inc::Float32 = 0
    first::Float32 = 1
    while i >= 0
        if i == 0
            sum = sum + first
            println("iterator: ",i,"  silnia: ", k)
            println(sum)
            i = i - 1
        else
            println("iterator: ",i,"  silnia: ", k)
            inc = 1/k
            inc = inc * inc
            sum = sum + inc
            println(sum)
            k = k / i
            i = i - 1
        end
    end
end  

println("7 składników")
println("")
Tn32rosnodwrkw(7)
println("")
println("6 składników")
println("")
Tn32rosnodwrkw(6)
println("")
println("5 składników")
println("")
Tn32rosnodwrkw(5)
println("")

function Tn64malkwodwr(n)
    sum::Float64 = 0
    i::Int64 = 0
    k::Int64 = 1
    inc::Float64 = 0
    while i <= n
        if i != 0
            k = k * i
        end
        println("iterator: ",i,"  silnia: ", k)
        inc = k * k
        inc = 1/inc
        if sum == sum + inc
            println("Następny wyraz już nic nie zmienia: Koniec ")
        end
        sum = sum + inc
        println(sum)
        i = i + 1
    end
end    

Tn64malkwodwr(13)

function Tn64malodwrkw(n)
    sum::Float64 = 0
    i::Int64 = 0
    k::Int64 = 1
    inc::Float64 = 0
    while i <= n
        if i != 0
            k = k * i
        end
        println("iterator: ",i,"  silnia: ", k)
        inc = 1/k
        inc = inc * inc
        if sum == sum + inc
            println("Następny wyraz już nic nie zmienia: Koniec ")
        end
        sum = sum + inc
        println(sum)
        i = i + 1
    end
end   

Tn64malodwrkw(13)

function Tn64rosnkwodwr(n)
    sum::Float64 = 0
    i::Int64 = n
    k::Int64 = fac(n)
    inc::Float64 = 0
    first::Float64 = 1
    while i >= 0
        if i == 0
            sum = sum + first
            println("iterator: ",i,"  silnia: ", k)
            println(sum)
            i = i - 1
        else
            println("iterator: ",i,"  silnia: ", k)
            inc = k * k
            inc = 1/inc
            sum = sum + inc
            println(sum)
            k = k / i
            i = i - 1
        end
    end
end   

Tn64rosnkwodwr(12)
println("")
println("11 składników")
println("")
Tn64rosnkwodwr(11)
println("")
println("10 składników")
println("")
Tn64rosnkwodwr(10)
println("")

function Tn64rosnodwrkw(n)
    sum::Float64 = 0
    i::Int64 = n
    k::Int64 = fac(n)
    inc::Float64 = 0
    first::Float64 = 1
    while i >= 0
        if i == 0
            sum = sum + first
            println("iterator: ",i,"  silnia: ", k)
            println(sum)
            i = i - 1
        else
            println("iterator: ",i,"  silnia: ", k)
            inc = 1/k
            inc = inc * inc
            sum = sum + inc
            println(sum)
            k = k / i
            i = i - 1
        end
    end
end   

println("12 składników")
println("")
Tn64rosnodwrkw(12)
println("")
println("11 składników")
println("")
Tn64rosnodwrkw(11)
println("")
println("10 składników")
println("")
Tn64rosnodwrkw(10)
println("")

function Sn32malkwodwr(n)
    sum::Float32 = 0
    i::Int64 = 0
    k::Int64 = 1
    inc::Float32 = 0
    while i <= n
        if i != 0
            k = k * i
        end
        println("iterator: ",i,"  silnia: ", k)
        inc = k * k
        inc = 1/inc
        if i % 2 == 1
            inc = -1 * inc
        end
        if sum == sum + inc
            println("Następny wyraz już nic nie zmienia: Koniec ")
        end
        sum = sum + inc
        println(sum)
        i = i + 1
    end
end   

Sn32malkwodwr(9)

function Sn32malodwrkw(n)
    sum::Float32 = 0
    i::Int64 = 0
    k::Int64 = 1
    inc::Float32 = 0
    while i <= n
        if i != 0
            k = k * i
        end
        println("iterator: ",i,"  silnia: ", k)
        inc = 1/k
        inc = inc * inc
        if i % 2 == 1
            inc = -1 * inc
        end
        if sum == sum + inc
            println("Następny wyraz już nic nie zmienia: Koniec ")
        end
        sum = sum + inc
        println(sum)
        i = i + 1
    end
end   

Sn32malodwrkw(9)

function Sn32rosnkwodwr(n)
    sum::Float32 = 0
    i::Int64 = n
    k::Int64 = fac(n)
    inc::Float32 = 0
    first::Float32 = 1
    while i >= 0
        if i == 0
            sum = sum + first
            println("iterator: ",i,"  silnia: ", k)
            println(sum)
            i = i - 1
        else
            println("iterator: ",i,"  silnia: ", k)
            inc = k * k
            inc = 1/inc
            if i % 2 == 1
                inc = -1 * inc
            end
            sum = sum + inc
            println(sum)
            k = k / i
            i = i - 1
        end
    end
end   

println("7 składników")
println("")
Sn32rosnkwodwr(7)
println("")
println("6 składników")
println("")
Sn32rosnkwodwr(6)
println("")
println("5 składników")
println("")
Sn32rosnkwodwr(5)

  function Sn32rosnodwrkw(n)
    sum::Float32 = 0
    i::Int64 = n
    k::Int64 = fac(n)
    inc::Float32 = 0
    first::Float32 = 1
    while i >= 0
        if i == 0
            sum = sum + first
            println("iterator: ",i,"  silnia: ", k)
            println(sum)
            i = i - 1
        else
            println("iterator: ",i,"  silnia: ", k)
            inc = 1/k
            inc = inc * inc
            if i % 2 == 1
                inc = -1 * inc
            end
            sum = sum + inc
            println(sum)
            k = k / i
            i = i - 1
        end
    end
end   

println("7 składników")
println("")
Sn32rosnodwrkw(7)
println("")
println("6 składników")
println("")
Sn32rosnodwrkw(6)
println("")
println("5 składników")
println("")
Sn32rosnodwrkw(5)

function Sn64malkwodwr(n)
    sum::Float64 = 0
    i::Int64 = 0
    k::Int64 = 1
    inc::Float64 = 0
    while i <= n
        if i != 0
            k = k * i
        end
        println("iterator: ",i,"  silnia: ", k)
        inc = 1/k
        inc = inc * inc
        if i % 2 == 1
            inc = -1 * inc
        end
        if sum == sum + inc
            println("Następny wyraz już nic nie zmienia: Koniec ")
        end
        sum = sum + inc
        println(sum)
        i = i + 1
    end
end 

Sn64malkwodwr(13)

function Sn64malodwrkw(n)
    sum::Float64 = 0
    i::Int64 = 0
    k::Int64 = 1
    inc::Float64 = 0
    while i <= n
        if i != 0
            k = k * i
        end
        println("iterator: ",i,"  silnia: ", k)
        inc = 1/k
        inc = inc * inc
        if i % 2 == 1
            inc = -1 * inc
        end
        if sum == sum + inc
            println("Następny wyraz już nic nie zmienia: Koniec ")
        end
        sum = sum + inc
        println(sum)
        i = i + 1
    end
end 

Sn64malodwrkw(13)

function Sn64rosnkwodwr(n)
    sum::Float64 = 0
    i::Int64 = n
    k::Int64 = fac(n)
    inc::Float64 = 0
    first::Float64 = 1
    while i >= 0
        if i == 0
            sum = sum + first
            println("iterator: ",i,"  silnia: ", k)
            println(sum)
            i = i - 1
        else
            println("iterator: ",i,"  silnia: ", k)
            inc = k * k
            inc = 1/inc
            if i % 2 == 1
                inc = -1 * inc
            end
            sum = sum + inc
            println(sum)
            k = k / i
            i = i - 1
        end
    end
end   

println("12 składników")
println("")
Sn64rosnkwodwr(12)
println("")
println("11 składników")
println("")
Sn64rosnkwodwr(11)
println("")
println("10 składników")
println("")
Sn64rosnkwodwr(10)

  function Sn64rosnodwrkw(n)
    sum::Float64 = 0
    i::Int64 = n
    k::Int64 = fac(n)
    inc::Float64 = 0
    first::Float64 = 1
    while i >= 0
        if i == 0
            sum = sum + first
            println("iterator: ",i,"  silnia: ", k)
            println(sum)
            i = i - 1
        else
            println("iterator: ",i,"  silnia: ", k)
            inc = 1/k
            inc = inc * inc
            if i % 2 == 1
                inc = -1 * inc
            end
            sum = sum + inc
            println(sum)
            k = k / i
            i = i - 1
        end
    end
end   

println("12 składników")
println("")
Sn64rosnodwrkw(12)
println("")
println("11 składników")
println("")
Sn64rosnodwrkw(11)
println("")
println("10 składników")
println("")
Sn64rosnodwrkw(10)

using Plots
plotly()
x = 0:9; y = map((x) -> Tn32malkwodwrwykres(x), 0:9);
plot(x,y, label = "Tn", title="Wartości wyrazów Tn (float32, malejąca kolejność)")

#Wykresy przy tak małych danych są nieczytelne





