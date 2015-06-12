//
//  main.swift
//  swift-example
//
//  Created by patrick zierahn on 09.06.15.
//  Copyright (c) 2015 patrick zierahn. All rights reserved.
//

import Foundation

println("Hello, World!")

var myVariable = 42
myVariable = 50
let myConstant = 42

let explicitDouble: Float = 70

let label = "The width is "
let width = 94

let widthLabel = label + String(width)
println(widthLabel)
println("width is \(width)")

var shoppingList = ["catfish", "water", "tulips", "blue paint"]

shoppingList[1] = "bottle of water"

for x in shoppingList
{
    println(x)
}


println(shoppingList[1])

var occupations =
[
    "Malcolm": "Captain",
    "Kaylee": "Mechanic",
]

occupations["Jayne"] = "Public Relations"
occupations["Kaylee"] = "Public Relations"

println(occupations)

let emptyArray = [String]()
let emptyDictionary = [String: Float]()

var optionalString: String? = "Hallo"
println(optionalString == nil)

var optionalName: String? = "John Appleseed"
var greeting = "Hello!"

if let name = optionalName
{
    greeting = "Hello, \(name)"
}

println(greeting)


let vegetable = "red pepper"
var vegetableComment = ""

switch vegetable
{
    case "celery":
        vegetableComment = "Add some raisins and make ants on a log."
    
    case "cucumber", "watercress":
        vegetableComment = "That would make a good tea sandwich."
    
    case let x where x.hasSuffix("pepper"):
        vegetableComment = "Is it a spicy \(x)?"
    
    default:
        vegetableComment = "Everything tastes good in soup."
}

println("vegetable: \(vegetable) --> vegetableComment: \(vegetableComment)")

let interestingNumbers = [
    "Prime": [2, 3, 5, 7, 11, 13],
    "Fibonacci": [1, 1, 2, 3, 5, 8],
    "Square": [1, 4, 9, 16, 25],
]

var largest = 0

for (kind, numbers) in interestingNumbers
{
    for number in numbers
    {
        if number > largest
        {
            largest = number
        }
    }
}

println(largest)


var n = 2
while n < 100
{
    n = n * 2
}

println(n)

var m = 2

do
{
    m = m * 2
} while m < 100

println(m)


func greet(name: String, day: String) -> String {
    return "Hello \(name), today is \(day)."
}

println(greet("Bob", "Tuesday"))

func calculateStatistics(scores: [Int]) -> (min: Int, max: Int, sum: Int) {
    var min = scores[0]
    var max = scores[0]
    var sum = 0
    
    for score in scores {
        if score > max {
            max = score
        } else if score < min {
            min = score
        }
        sum += score
    }
    
    return (min, max, sum)
}

let statistics = calculateStatistics([5, 3, 100, 3, 9])
println(statistics.sum)
println(statistics.2)

func sumOf(numbers: Int...) -> Int {
    var sum = 0
    for number in numbers {
        sum += number
    }
    return sum
}

sumOf()
sumOf(42, 597, 12)

func makeIncrementer() -> (Int -> Int) {
    func addOne(number: Int) -> Int {
        return 1 + number
    }
    return addOne
}

var increment = makeIncrementer()

println(increment(7))
println(increment(17))


func hasAnyMatches(list: [Int], condition: Int -> Bool) -> Bool {
    for item in list {
        if condition(item) {
            return true
        }
    }
    return false
}

func lessThanTen(number: Int) -> Bool {
    return number < 10
}
var numbers = [20, 19, 7, 12]
println(hasAnyMatches(numbers, lessThanTen))

let mappedNumbers = numbers.map({ number in 3 * number })
println(mappedNumbers)

let sortedNumbers = sorted(numbers) { $0 < $1 }
println(sortedNumbers)

class NamedShape {
    var numberOfSides: Int = 0
    var name: String
    
    init(name: String) {
        self.name = name
    }
    
    func simpleDescription() -> String {
        return "A shape with \(numberOfSides) sides."
    }
}

class Square: NamedShape {
    var sideLength: Double
    
    init(sideLength: Double, name: String) {
        self.sideLength = sideLength
        super.init(name: name)
        numberOfSides = 4
    }
    
    func area() ->  Double {
        return sideLength * sideLength
    }
    
    override func simpleDescription() -> String {
        return "A square with sides of length \(sideLength)."
    }
}

let test = Square(sideLength: 5.2, name: "my test square")
test.area()
println(test.simpleDescription())

class EquilateralTriangle: NamedShape {
    var sideLength: Double = 0.0
    
    init(sideLength: Double, name: String) {
        self.sideLength = sideLength
        super.init(name: name)
        numberOfSides = 3
    }
    
    var perimeter: Double {
        get {
            return 3.0 * sideLength
        }
        set {
            sideLength = newValue / 3.0
        }
    }
    
    override func simpleDescription() -> String {
        return "An equilateral triangle with sides of length \(sideLength)."
    }
}

var triangle = EquilateralTriangle(sideLength: 3.1, name: "a triangle")
println(triangle.perimeter)
triangle.perimeter = 9.9
println(triangle.sideLength)


class TriangleAndSquare {
    var triangle: EquilateralTriangle {
        willSet {
            square.sideLength = newValue.sideLength
        }
    }
    
    var square: Square {
        willSet {
            triangle.sideLength = newValue.sideLength
        }
    }

    init(size: Double, name: String) {
        square = Square(sideLength: size, name: name)
        triangle = EquilateralTriangle(sideLength: size, name: name)
    }
}

var triangleAndSquare = TriangleAndSquare(size: 10, name: "another test shape")
println(triangleAndSquare.square.sideLength)
println(triangleAndSquare.triangle.sideLength)
triangleAndSquare.square = Square(sideLength: 50, name: "larger square")
println(triangleAndSquare.triangle.sideLength)

class Counter {
    var count: Int = 0
    func incrementBy(amount: Int, numberOfTimes times: Int) {
        count += amount * times
    }
}

var counter = Counter()
counter.incrementBy(2, numberOfTimes: 7)

println(counter.count)

let optionalSquare: Square? = Square(sideLength: 2.5, name: "optional square")
let sideLength = optionalSquare?.sideLength

println(sideLength)



enum Suit {
    case Spades, Hearts, Diamonds, Clubs
    func simpleDescription() -> String {
        switch self {
        case .Spades:
            return "spades"
        case .Hearts:
            return "hearts"
        case .Diamonds:
            return "diamonds"
        case .Clubs:
            return "clubs"
        }
    }
}
let hearts = Suit.Diamonds
let heartsDescription = hearts.simpleDescription()

println(heartsDescription)


struct Card {
    var rank: String
    var suit: String
    
    func simpleDescription() -> String {
        return "The \(rank) of \(suit)"
    }
}

let threeOfSpades = Card(rank: ".Three", suit: ".Spades")
let threeOfSpadesDescription = threeOfSpades.simpleDescription()

println(threeOfSpadesDescription)




enum ServerResponse {
    case Result(String, String)
    case Error(String)
}

let success = ServerResponse.Result("6:00 am", "8:09 pm")
let failure = ServerResponse.Error("Out of cheese.")

switch success {
    case let .Result(sunrise, sunset):
        let serverResponse = "Sunrise is at \(sunrise) and sunset is at \(sunset)."
        println("Sunrise is at \(sunrise) and sunset is at \(sunset).")
    case let .Error(error):
        let serverResponse = "Failure...  \(error)"
        println("Failure...  \(error)")
}


protocol ExampleProtocol {
    var simpleDescription: String { get }
    mutating func adjust()
}

class SimpleClass: ExampleProtocol {
    var simpleDescription: String = "A very simple class."
    var anotherProperty: Int = 69105
    func adjust() {
        simpleDescription += "  Now 100% adjusted."
    }
}
var a = SimpleClass()
a.adjust()
let aDescription = a.simpleDescription

struct SimpleStructure: ExampleProtocol {
    var simpleDescription: String = "A simple structure"
    mutating func adjust() {
        simpleDescription += " (adjusted)"
    }
}

var b = SimpleStructure()
b.adjust()
let bDescription = b.simpleDescription

println(bDescription)
println(aDescription)


extension Int: ExampleProtocol {
    var simpleDescription: String {
        return "The number \(self)"
    }
    
    mutating func adjust() {
        self += 42
    }
}
println(7.simpleDescription)


let protocolValue: ExampleProtocol = a
println(protocolValue.simpleDescription)
// println(protocolValue.anotherProperty)  // Uncomment to see the error


func repeat<Item>(item: Item, times: Int) -> [Item] {
    var result = [Item]()
    for i in 0..<times {
        result.append(item)
    }
    return result
}

println(repeat("knock", 4))
println(repeat(4, 4))


for x in 0..<100 {
//    println(x)
}


func anyCommonElements <T, U where T: SequenceType, U: SequenceType, T.Generator.Element: Equatable, T.Generator.Element == U.Generator.Element> (lhs: T, rhs: U) -> Bool {
    for lhsItem in lhs {
        for rhsItem in rhs {
            if lhsItem == rhsItem {
                return true
            }
        }
    }
    return false
}

anyCommonElements([1, 2, 3], [3])


println(UInt.max)
println(UInt8.max)
println(UInt16.max)
println(UInt32.max)
println(UInt64.max)

































