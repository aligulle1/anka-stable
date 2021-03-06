#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import kde4
from pisi.actionsapi import get

WorkDir = "."

def setup():
    shelltools.cd("calligra-l10n-ca-2.5.94")
    kde4.configure()
    shelltools.cd("../calligra-l10n-da-2.5.94")
    kde4.configure()
    shelltools.cd("../calligra-l10n-de-2.5.94")
    kde4.configure()
    shelltools.cd("../calligra-l10n-et-2.5.94")
    kde4.configure()
    shelltools.cd("../calligra-l10n-en_GB-2.5.94")
    kde4.configure()
    shelltools.cd("../calligra-l10n-es-2.5.94")
    kde4.configure()
    shelltools.cd("../calligra-l10n-et-2.5.94")
    kde4.configure()
    shelltools.cd("../calligra-l10n-fi-2.5.94")
    kde4.configure()
    shelltools.cd("../calligra-l10n-fr-2.5.94")
    kde4.configure()
    shelltools.cd("../calligra-l10n-gl-2.5.94")
    kde4.configure()
    shelltools.cd("../calligra-l10n-hu-2.5.94")
    kde4.configure()
    shelltools.cd("../calligra-l10n-it-2.5.94")
    kde4.configure()
    #shelltools.cd("../calligra-l10n-ja-2.5.94")
    #kde4.configure()
    shelltools.cd("../calligra-l10n-kk-2.5.94")
    kde4.configure()
    shelltools.cd("../calligra-l10n-nb-2.5.94")
    kde4.configure()
    shelltools.cd("../calligra-l10n-nds-2.5.94")
    kde4.configure()
    shelltools.cd("../calligra-l10n-nl-2.5.94")
    kde4.configure()
    shelltools.cd("../calligra-l10n-pl-2.5.94")
    kde4.configure()
    shelltools.cd("../calligra-l10n-pt-2.5.94")
    kde4.configure()
    shelltools.cd("../calligra-l10n-pt_BR-2.5.94")
    kde4.configure()
    shelltools.cd("../calligra-l10n-ru-2.5.94")
    kde4.configure()
    shelltools.cd("../calligra-l10n-sk-2.5.94")
    kde4.configure()
    shelltools.cd("../calligra-l10n-sv-2.5.94")
    kde4.configure()
    #shelltools.cd("../calligra-l10n-tr-2.5.94")
    #kde4.configure()
    shelltools.cd("../calligra-l10n-uk-2.5.94")
    kde4.configure()
    shelltools.cd("../calligra-l10n-zh_CN-2.5.94")
    kde4.configure()
    shelltools.cd("../calligra-l10n-zh_TW-2.5.94")
    kde4.configure()

def build():
    shelltools.cd("calligra-l10n-ca-2.5.94")
    kde4.make()
    shelltools.cd("../calligra-l10n-da-2.5.94")
    kde4.make()
    shelltools.cd("../calligra-l10n-de-2.5.94")
    kde4.make()
    shelltools.cd("../calligra-l10n-et-2.5.94")
    kde4.make()
    shelltools.cd("../calligra-l10n-en_GB-2.5.94")
    kde4.make()
    shelltools.cd("../calligra-l10n-es-2.5.94")
    kde4.make()
    shelltools.cd("../calligra-l10n-et-2.5.94")
    kde4.make()
    shelltools.cd("../calligra-l10n-fi-2.5.94")
    kde4.make()
    shelltools.cd("../calligra-l10n-fr-2.5.94")
    kde4.make()
    shelltools.cd("../calligra-l10n-gl-2.5.94")
    kde4.make()
    shelltools.cd("../calligra-l10n-hu-2.5.94")
    kde4.make()
    shelltools.cd("../calligra-l10n-it-2.5.94")
    kde4.make()
    #shelltools.cd("../calligra-l10n-ja-2.5.94")
    #kde4.make()
    shelltools.cd("../calligra-l10n-kk-2.5.94")
    kde4.make()
    shelltools.cd("../calligra-l10n-nb-2.5.94")
    kde4.make()
    shelltools.cd("../calligra-l10n-nds-2.5.94")
    kde4.make()
    shelltools.cd("../calligra-l10n-nl-2.5.94")
    kde4.make()
    shelltools.cd("../calligra-l10n-pl-2.5.94")
    kde4.make()
    shelltools.cd("../calligra-l10n-pt-2.5.94")
    kde4.make()
    shelltools.cd("../calligra-l10n-pt_BR-2.5.94")
    kde4.make()
    shelltools.cd("../calligra-l10n-ru-2.5.94")
    kde4.make()
    shelltools.cd("../calligra-l10n-sk-2.5.94")
    kde4.make()
    shelltools.cd("../calligra-l10n-sv-2.5.94")
    kde4.make()
    #shelltools.cd("../calligra-l10n-tr-2.5.94")
    #kde4.make()
    shelltools.cd("../calligra-l10n-uk-2.5.94")
    kde4.make()
    shelltools.cd("../calligra-l10n-zh_CN-2.5.94")
    kde4.make()
    shelltools.cd("../calligra-l10n-zh_TW-2.5.94")
    kde4.make()

def install():
    shelltools.cd("calligra-l10n-ca-2.5.94")
    kde4.install("DESTDIR=%s" % get.installDIR())
    shelltools.cd("../calligra-l10n-da-2.5.94")
    kde4.install("DESTDIR=%s" % get.installDIR())
    shelltools.cd("../calligra-l10n-de-2.5.94")
    kde4.install("DESTDIR=%s" % get.installDIR())
    shelltools.cd("../calligra-l10n-et-2.5.94")
    kde4.install("DESTDIR=%s" % get.installDIR())
    shelltools.cd("../calligra-l10n-en_GB-2.5.94")
    kde4.install("DESTDIR=%s" % get.installDIR())
    shelltools.cd("../calligra-l10n-es-2.5.94")
    kde4.install("DESTDIR=%s" % get.installDIR())
    shelltools.cd("../calligra-l10n-et-2.5.94")
    kde4.install("DESTDIR=%s" % get.installDIR())
    shelltools.cd("../calligra-l10n-fi-2.5.94")
    kde4.install("DESTDIR=%s" % get.installDIR())
    shelltools.cd("../calligra-l10n-fr-2.5.94")
    kde4.install("DESTDIR=%s" % get.installDIR())
    shelltools.cd("../calligra-l10n-gl-2.5.94")
    kde4.install("DESTDIR=%s" % get.installDIR())
    shelltools.cd("../calligra-l10n-hu-2.5.94")
    kde4.install("DESTDIR=%s" % get.installDIR())
    shelltools.cd("../calligra-l10n-it-2.5.94")
    kde4.install("DESTDIR=%s" % get.installDIR())
    #shelltools.cd("../calligra-l10n-ja-2.5.94")
    #kde4.install("DESTDIR=%s" % get.installDIR())
    shelltools.cd("../calligra-l10n-kk-2.5.94")
    kde4.install("DESTDIR=%s" % get.installDIR())
    shelltools.cd("../calligra-l10n-nb-2.5.94")
    kde4.install("DESTDIR=%s" % get.installDIR())
    shelltools.cd("../calligra-l10n-nds-2.5.94")
    kde4.install("DESTDIR=%s" % get.installDIR())
    shelltools.cd("../calligra-l10n-nl-2.5.94")
    kde4.install("DESTDIR=%s" % get.installDIR())
    shelltools.cd("../calligra-l10n-pl-2.5.94")
    kde4.install("DESTDIR=%s" % get.installDIR())
    shelltools.cd("../calligra-l10n-pt-2.5.94")
    kde4.install("DESTDIR=%s" % get.installDIR())
    shelltools.cd("../calligra-l10n-pt_BR-2.5.94")
    kde4.install("DESTDIR=%s" % get.installDIR())
    shelltools.cd("../calligra-l10n-ru-2.5.94")
    kde4.install("DESTDIR=%s" % get.installDIR())
    shelltools.cd("../calligra-l10n-sk-2.5.94")
    kde4.install("DESTDIR=%s" % get.installDIR())
    shelltools.cd("../calligra-l10n-sv-2.5.94")
    kde4.install("DESTDIR=%s" % get.installDIR())
    #shelltools.cd("../calligra-l10n-tr-2.5.94")
    #kde4.install("DESTDIR=%s" % get.installDIR())
    shelltools.cd("../calligra-l10n-uk-2.5.94")
    kde4.install("DESTDIR=%s" % get.installDIR())
    shelltools.cd("../calligra-l10n-zh_CN-2.5.94")
    kde4.install("DESTDIR=%s" % get.installDIR())
    shelltools.cd("../calligra-l10n-zh_TW-2.5.94")
    kde4.install("DESTDIR=%s" % get.installDIR())
