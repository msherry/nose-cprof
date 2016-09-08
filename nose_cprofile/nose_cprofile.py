import cProfile
import logging
import os

import nose
from nose.plugins.base import Plugin

log = logging.getLogger('nose.plugins')


class cProfiler(Plugin):
    """
    Use this plugin to run tests using the cProfile profiler.
    """

    # attributes required by nose
    enabled = True
    name = 'cprofile'

    pfile_name = None

    def options(self, parser, env):
        """Register commandline options.
        """
        Plugin.options(self, parser, env)
        parser.add_option('--cprofile-stats-file', action='store',
                          dest='profile_stats_file',
                          metavar="FILE",
                          default="stats.dat",
                          help='Output file name; default "stats.dat"')
        parser.add_option("--cprofile-stats-erase", action="store_true",
                          default=env.get('NOSE_PROFILE_STATS_ERASE'),
                          dest="stats_erase",
                          help="Erase previously-collected profiling "
                          "statistics before run")

    def begin(self):
        """Instantiate profiler
        """
        self.prof = cProfile.Profile()

    def configure(self, options, conf):
        """Configure plugin.
        """
        super(cProfiler, self).configure(options, conf)
        if options.profile_stats_file:
            self.pfile_name = options.profile_stats_file
        else:
            self.pfile_name = 'stats.dat'
        self.fileno = None
        if options.stats_erase:
            self._erase_stats_file()

    def prepareTest(self, test):
        """Wrap entire test run in :func:`prof.runcall`.
        """
        log.debug('preparing test %s' % test)

        def run_and_profile(result, prof=self.prof, test=test):
            prof.runcall(test, result)
            prof.dump_stats(self.pfile_name)
        return run_and_profile

    def finalize(self, result):
        pass

    def _erase_stats_file(self):
        if os.path.exists(self.pfile_name):
            os.unlink(self.pfile_name)


if __name__ == '__main__':
    nose.main(addplugins=[cProfiler()])
