#!/int/python1.5
#
# notify.py -- notify about web page changes
#
# Keith Waclena <k-waclena@uchicago.edu>
#

__author__ = "Keith Waclena, k-waclena@uchicago.edu"
__version__ = "0.2"
__patchlevel__ = "0"
__production__ = 0

CHUNKSIZE = 16 * 1024

import sys, shelve, urllib, md5
from urlparse import urlparse, urlunparse
from string import join
import main

class summary:
    def __init__(self, digest, size):
        self.digest, self.size = digest, size

def summarize(fp):
    """Return an MD5 message digest (checksum) of all the data on open file fp.
    """
    m = md5.new()
    size = 0
    while 1:
        chunk = fp.read(CHUNKSIZE)
        if not chunk: break
        m.update(chunk)
        size = size + len(chunk)
    return summary(m.digest(), size)

def normalize(url):
    """Normalize url by stripping any query and fragment parts; also,
    if original url was of the form `www.foo.com', convert this to
    `http://www.foo.com'.
    """
    (scheme, netloc, path, _, _, frag) = urlparse(url, "http")
    if not netloc and path:
        return urlunparse((scheme, path, "", "", "", ""))
    else:
        return urlunparse((scheme, netloc, path, "", "", ""))

class Main(main.main):
    Usage = "-[vqadscu] database [url ...]"

    try:
        options = [main.opt("v", doc="set VERBOSITY level to 1"),
           main.opt("q", doc="quiet mode; no output, only exit status"),
           main.opt("a", doc="add urls to database, don't check"),
           main.opt("d", doc="delete urls from database, don't check"),
           main.opt("s", doc="show urls in database"),
           main.opt("c", doc="list urls that have changed"),
           main.opt("u", doc="autoupdate of checksums of urls that have"
                " changed"), ]
    except main.opt, o:
        main.dryrot("%s: %s" % (o, o.error))

    def main(self):
        ((self.verbose.verbosity, self.quiet, adding, deleting, showing,
        self.changed, self.updating),
        self.args) = main.opts(self.options).getopt("v", "q", "a",
                             "d", "s", "c", "u")
        self.db = None
        if self.args:
            self.database = self.args[0]
            self.db = shelve.open(self.database)
            self.args = self.args[1:]
        try:
            if adding:
                self.add()
            elif deleting:
                self.delete()
            elif showing:
                self.show()
            else:
        # checking...
                if self.args:
            # check all urls in database
                    allswell = self.check(self.args)
                else:
            # check named urls only
                    allswell = self.check(self.db.keys())
                if allswell or self.changed:
                    sys.exit(0)
                else:
                    sys.exit(1)
        finally:
            if self.db: self.db.close()

    def check(self, urls):
        """Check all URLs in urls (a sequence of strings).
        """
        from operator import __and__
        results = []
        for url in urls:
            url = normalize(url)
            self.verbose.partial(1, "%s, " % url)
            try:
                fp = urllib.urlopen(url)
            except IOError, (_, msg):
                self.verbose.finish(1, "%s" % msg)
                continue
            else:
                self.verbose.finish(1, "done")
            try:
                previous = self.db[url].digest
            except KeyError:
                self.warning("%s not in database" % url)
                continue
            s = summarize(fp)
            if s.digest == previous:
                results.append(1)
                if self.quiet:
                    pass
                elif self.changed:
                    pass
                else:
                    print "same\t%s" % url
            else:
                results.append(0)
                if self.quiet:
                    pass
                elif self.changed:
                    print url
                else:
                    print "DIFFER\t%s" % url
                if self.updating:
                    self.verbose(1, "updating %s" % url)
                    self.db[url] = s
        return reduce(__and__, results, 1)

    def add(self):
        """Add urls in self.args to database.
        """
        for url in self.args:
            url = normalize(url)
            self.verbose.partial(1, "adding %s, " % url)
            try:
                fp = urllib.urlopen(url)
            except IOError, (_, msg):
                self.verbose.finish(1, "%s" % msg)
                continue
            else:
                self.verbose.finish(1, "done")
            self.db[url] = summarize(fp)

    def delete(self):
        """Delete urls in self.args from database.
        """
        for url in self.args:
            url = normalize(url)
            try:
                del self.db[url]
                self.verbose(1, "deleted %s" % url)
            except KeyError:
                self.warning("%s not in database" % url)

    def show(self):
        """Show all urls in database in a parsable form on stdout.
        """
        def md5repr(digest):
            return join(map(lambda c: "%x" % ord(c), digest), "")
        for key in self.db.keys():
            s = self.db[key]
            print "%s\t%s\t%s" % (md5repr(s.digest), s.size, key)

Main(production=__production__)()

# Local Variables:
# py-indent-offset: 4
# fill-column: 76
# End:
