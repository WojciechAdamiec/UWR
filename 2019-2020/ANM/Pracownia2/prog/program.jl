function aprox(X, Y)
    Yl = Float64[]
    m = size(X, 1)
    sumX = Float64
    sumX2 = Float64
    sumYl = Float64
    sumYlX = Float64
    for value in Y
        push!(Yl, log(value))
    end
    sumX = 0
    for value in X
        sumX = sumX + value
    end
    sumX2 = 0
    for value in X
        sumX2 = sumX2 + value * value
    end
    sumYl = 0
    for value in Yl
        sumYl = sumYl + value
    end
    sumYlX = 0
    for i in eachindex(X)
        sumYlX = sumYlX + X[i] * Yl[i]
    end
    print("===")
    print("\n", m,"\n", sumX,"\n", sumX2,"\n", sumYl,"\n", sumYlX, "\n")
    W = m * sumX2 - sumX * sumX
    WA = sumYl * sumX2 - sumX * sumYlX 
    WB = m * sumYlX - sumYl * sumX
    print("W: ", W, "\n")
    print("Wa: ", WA, "\n")
    print("Wb: ", WB, "\n")
    A = WA/W
    B = WB/W
    print("A: ", A, "\n")
    print("B: ", B, "\n")
    e = 2.71828182845904523536
    a = e^A
    b = e^B
    print("a: ", a, "\n")
    print("b: ", b, "\n")
end

X = [1.0, 2, 3, 4, 5]
Y = [2.0, 4, 8, 16, 32]
aprox(X, Y)

X = [1.0, 2, 3, 4, 5]
Y = [5.87, 18.05, 54.1, 162.6, 487.1]
aprox(X, Y)

X = [12.5677, 23.2512, 44.1234]
Y = [2104.556, 255724.457, 3023070299.5619]
aprox(X, Y)

X = [12.56, 23.25, 44.12]
Y = [2102, 255725, 3023070315]
aprox(X, Y)

X = [12.56, 16.2,  23.25, 25.5, 44.12]
Y = [2102, 10760, 255725, 702365, 3023070315]
aprox(X, Y)


