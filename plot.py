from matplotlib import pyplot as plt
import numpy as np

languages = [
        "Python",
        "Shell",
        "Go",
        "Ruby",
        "C",
        "JavaScript",
        "Puppet",
        "Java",
        "PHP",
        "HTML",
        "CSS",
        "C++",
        "Scala",
        "VimL",
        "R",
        "Perl",
        "Makefile",
        "C#",
        "Arduino",
        "Objective-C",
        "XSLT",
        "TeX",
        "Swift",
        "PowerShell",
        "OpenSCAD",
        "Lua",
        "HCL",
        "Emacs",
        "CoffeeScript",
        "Clojure",
        "BitBake"
]

num_lang = [
        259,
        71,
        67,
        53,
        39,
        36,
        32,
        26,
        20,
        17,
        13,
        13,
        8,
        7,
        7,
        7,
        6,
        4,
        3,
        2,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1
]

plt.title("Languages")

# arrange the defualt height of each language
ypos = np.arange(len(languages))*3
#ypos = [i  for i, _ in enumerate(languages)]
plt.barh(ypos, list(reversed(num_lang)), alpha=0.4, height=3.0)
plt.yticks(ypos+1.5, list(reversed(languages)))
plt.xlabel("Number of projects written in language")
plt.title("Cisco Open Source Programming Languages")
plt.show()
