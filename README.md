# Magic Methods

Magic methods (formally known as special methods) are:

> [...] called implicitly by Python to execute a certain operation on a type, such as addition. Such methods have names starting and ending with double underscores.
>
> &mdash; [Glossary &ndash; Python 3 documentation][specialmethod]

5 line example:

```
>>> class MyObj:
...     def __add__(self, other):
...         print(self, other)  # return something sensible
...
>>> MyObj() + 42
<__main__.MyObj object at 0x7f3637f8ea90> 42
```

## Links

* Slides
    * [PyCon Ireland 2019][slides-pyconie19]
    * [ChiPy 2018][slides-chipy18]
* [Notebook](MagicMethods.ipynb)

---

## Licenses

* Notebook: &copy; Nick Timkovich, All rights reserved. Licensed under the [MIT License][license-mit].
* Slide text, figures (excluding trademarks and logos), and source listings, excluding style elements &copy; Nick Timkovich, All rights reserved. Licensed under [CC-BY-SA 4.0][license-ccbysa4]
* Typeset slides and styles: &copy; Telnyx, LLC, All rights reserved. Licensed under [CC-BY-NC-ND 4.0][license-ccbyncnd4].
* Duck cutout is a derivative of [a photo by Bengt Nyman](https://commons.wikimedia.org/wiki/File:Birds_of_Sweden_2016_52.jpg), and licensed under [CC-BY-SA 4.0][license-ccbysa4]


[slides-pyconie19]: https://docs.google.com/presentation/d/1Jus7lDXD2h_TdcE5nnXcJuAO_mEGfWMXLADNnSeNHgs/edit?usp=sharing
[slides-chipy18]: https://docs.google.com/presentation/d/13rnvQ7w2YT3WQKgDDAEd7Unlf67WcgzYVN3uGt-vJP8/edit?usp=sharing

[license-ccbyncnd4]: https://creativecommons.org/licenses/by-nc-nd/4.0/
[license-ccbysa4]: https://creativecommons.org/licenses/by-sa/4.0/
[license-mit]: https://opensource.org/licenses/MIT

[specialmethod]: https://docs.python.org/3/glossary.html#term-special-method
