# pythonic-functional-programming
Pythonic Functional Programming: List Comprehensions

# What functional programming is?
In computer science, functional programming is a programming paradigm where programs are constructed by applying and composing functions.

[Wikipedia article](https://en.wikipedia.org/wiki/Functional_programming)
## Map
Map is a high-order function that receives another function and a collection as input and applies that function to each element in the collection, returning a new collection.

[Wikipedia article](https://en.wikipedia.org/wiki/Map_(higher-order_function))

## Filter
Filter is a higher-order function that processes a collection in some order to produce a new collection containing exactly those elements of the original data structure for which a given predicate returns the boolean value true.

[Wikipedia article](https://en.wikipedia.org/wiki/Filter_(higher-order_function))

## Reduce
Reduce is a high-order function that receives another function, a collection and a initial value as input, and recursively applies that function to the initial value and to each element of the collection, ultimately reducing it to a single value.

[Wikipedia article](https://en.wikipedia.org/wiki/Fold_(higher-order_function))

# What list comprehensions are?

According to [official Python documentation](https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions):

```
“A list comprehension consists of brackets containing an expression followed by a for clause, then zero or more for or if clauses. The result will be a new list resulting from evaluating the expression in the context of the for and if clauses which follow it.”
```

## Why Python favors list comprehensions over map, filter and reduce?
Guido van Rossum doesn't like functional programming a lot:

```
Guido: I'm not a fan of religiously taking some idea to the extreme, and I try to be pragmatic in my design choices (but not *too* pragmatic, see the start of this sentence :-). I value readability and usefulness for real code. There are some places where map() and filter() make sense, and for other places Python has list comprehensions. I ended up hating reduce() because it was almost exclusively used (a) to implement sum(), or (b) to write unreadable code. So we added builtin sum() at the same time we demoted reduce() from a builtin to something in functools (which is a dumping ground for stuff I don't really care about :-).
```

[Source](https://developers.slashdot.org/story/13/08/25/2115204/interviews-guido-van-rossum-answers-your-questions)

## Why are list comprehensions faster in Python?
We have several sources on the reasons why list comprehensions outperform `map()` and might outperform `for` loops. Please check them out:

* [Which is Faster: List Comprehension or Map Function in Python?](https://blog.finxter.com/which-is-faster-list-comprehension-or-map-function-in-python/)
* [Are list-comprehensions and functional functions faster than "for loops"?](https://stackoverflow.com/questions/22108488/are-list-comprehensions-and-functional-functions-faster-than-for-loops)
* [For Loop vs. List Comprehension](https://switowski.com/blog/for-loop-vs-list-comprehension/)
* [SURPRISE BUT LIST COMPREHENSION IS 10X FASTER THAN LOOPS IN PYTHON – 9](https://innovationyourself.com/list-comprehension-in-python/)
* [List Comprehensions vs. For Loops: It Is Not What You Think](https://towardsdatascience.com/list-comprehensions-vs-for-loops-it-is-not-what-you-think-34071d4d8207)

