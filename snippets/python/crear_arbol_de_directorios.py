try:
    import sys
    import os
    import lipsum
    from random import randint, randrange, choice
except ImportError:
    # Checks the installation of the necessary python modules
    print((os.linesep * 2).join(["An error found importing one module:",
    str(sys.exc_info()[1]), "You need to install it", "Stopping..."]))
    sys.exit(-2)


def test_tree(path, min_dirs=7, max_dirs=79):
    """make a fake directory hierarchy with files for test purposes."""

    def latin_words(generator):
        """Generate a list of latin words"""
        words = generator.generate_paragraphs_plain(9).lower()
        return list(set(words.replace('.', '').replace(',', '').split()))

    def check_path(path):
        """If no exists a path, make it."""
        if not os.path.exists(path):
            os.mkdir(path)

    lorem = lipsum.MarkupGenerator()
    latins = latin_words(lorem)

    dirs = latins[:randrange(min_dirs, max_dirs)]
    files = [f for f in latins if f not in dirs][:len((dirs) * 3) - 3]

    check_path(path)
    for directory in dirs:
        check_path(os.path.join(path, directory))

    for fil in files:
        filename = os.path.join(path, choice(dirs), '{0}.txt'.format(fil))
        text = ''
        size = randint(3, 524288) # Files not bigger than 512 Kbytes
        sample = lorem.generate_paragraphs_plain(randrange(3, 9))
        while len(text) < size:
            text += sample + os.linesep * 2
        with open(filename, 'w') as out:
            out.write(text[:size])

    return dirs, files
