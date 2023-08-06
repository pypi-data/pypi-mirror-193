# [WIP] shortscale

[![CI](https://github.com/jldec/shortscale-py/workflows/CI/badge.svg)](https://github.com/jldec/shortscale-py/actions)  

Python module to convert integers into English words.

This is the Python port of the shortscale function, originally written in [JavaScript](https://github.com/jldec/shortscale) and [Rust](https://github.com/jldec/shortscale-rs), documented [here](https://jldec.me/forays-from-node-to-rust). There is a also a [Go](https://github.com/jldec/shortscale-go) version.

The [short scale](https://en.wikipedia.org/wiki/Long_and_short_scales#Comparison), has different words for each power of 1000.

This implementation expresses positive and negative numbers from zero to thousands, millions, billions, trillions, quadrillions etc, up to 10**33 - 1.

### Function
```python
def shortscale(num: int) -> str
```

### Example
```python
import shortscale

// ==> four hundred and twenty billion nine hundred and ninety nine thousand and fifteen
print(shortscale.shortscale(420_000_999_015))
```

After installing this module, the function can also be called from the commnd line e.g.

```sh
$ shortscale 420_000_999_015
420,000,999,015 => four hundred and twenty billion nine hundred and ninety nine thousand and fifteen

$ shortscale 0xffffffff
4,294,967,295 => four billion two hundred and ninety four million nine hundred and sixty seven thousand two hundred and ninety five
```

### Benchmarks
(TODO)
