from matplotlib import pyplot as plt
import numpy as np

languages = [
        "Swift",
        "Java",
        "Ruby",
        "Puppet",
        "Arduino",
        "Lua",
        "XSLT",
        "Go",
        "C#",
        "CoffeeScript",
        "C++",
        "Scala",
        "PowerShell",
        "C",
        "Emacs",
        "Python",
        "Shell",
        "Makefile",
        "Objective-C",
        "JavaScript",
        "R",
        "Perl",
        "BitBake",
        "VimL",
        "HTML",
        "Clojure",
        "OpenSCAD",
        "PHP",
        "TeX",
        "CSS",
        "HCL",
]

num_lang = [
        1,
        26,
        53,
        32,
        3,
        1,
        1,
        67,
        4,
        1,
        13,
        8,
        1,
        39,
        1,
        259,
        71,
        6,
        2,
        36,
        7,
        7,
        1,
        7,
        17,
        1,
        1,
        20,
        1,
        13,
        1,
]

plt.title("Languages")

# arrange the defualt height of each language
ypos = np.arange(len(languages))+0.5
#ypos = [i  for i, _ in enumerate(languages)]
plt.barh(np.arange(len(languages)), num_lang, alpha=0.4, height=1.5)
plt.yticks(ypos, languages)
plt.xlabel("Number of projects written in language")
plt.title("Cisco Open Source Programming Languages")
plt.show()
